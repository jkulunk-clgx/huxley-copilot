import os
import glob
import time
from google import genai

RAG_REGISTRY = {
    "default": "rag_data/registry.md",
    "system_instructions": "rag_data/system_instructions.md",
    "persona_format": "output_formats/persona_format.json",
    "JTBD_format": "output_formats/JTBD_format.json",
    "journey_map_format": "output_formats/journey_map_format.json",
    "data": "rag_data/Data-Real-Estate-Agent-001.md"
}

def generate_content_with_backoff(client, model, contents, config=None, max_retries=5, base_delay=1):
    for attempt in range(max_retries):
        try:
            if config:
                return client.models.generate_content(model=model, contents=contents, config=config)
            else:
                return client.models.generate_content(model=model, contents=contents)
        except Exception as e:
            is_503 = False
            if hasattr(e, 'code') and e.code == 503:
                is_503 = True
            elif "503" in str(e) or "UNAVAILABLE" in str(e):
                is_503 = True
                
            if is_503 and attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)
                print(f"API 503 Error. Retrying in {delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(delay)
            else:
                raise

def extract_role_from_input(user_input, api_key):
    """Fallback intent/role extraction if not provided directly."""
    try:
        client = genai.Client(api_key=api_key)
        extraction_prompt = f"Extract the target user role from this user request: '{user_input}'. Return only the role name in snake_case (e.g. data_scientist, mortgage_lender), or 'None' if no role is specified."
        role_response = generate_content_with_backoff(
            client=client,
            model='gemini-3.5-flash',
            contents=extraction_prompt
        )
        return role_response.text.strip().lower()
    except Exception as e:
        print(f"Error extracting role: {e}")
        return "none"

def generate_ai_response(user_input, role=None, api_key=None, allow_web_search=False, notify_callback=None):
    """
    Core logic for generating AI response. 
    Handles intent extraction, raw data ingestion, and artifact generation.
    Returns: (ai_response, notification_message, error_message, needs_web_search_permission)
    """
    ai_response = None
    notification_message = None
    error_message = None
    needs_web_search_permission = False

    if not api_key or api_key == "your_api_key_here":
        return None, None, "Gemini API key is missing. Please set it in the .env file.", False

    if not user_input:
        return None, None, "User input is required.", False

    try:
        client = genai.Client(api_key=api_key)
        
        # Phase 1: Intent & Role Extraction (Fallback)
        if not role:
            if notify_callback: notify_callback("Analyzing request to extract target user role...")
            role = extract_role_from_input(user_input, api_key)
            if notify_callback and role and role != "none":
                notify_callback(f"Identified target user role: {role.replace('_', ' ').title()}")
            
        # Phase 2: Raw Data Ingestion (Conditional)
        if role and role != "none":
            search_pattern = role.replace("_", "-").lower()
            
            found_rag_file = None
            for file_path in glob.glob("rag_data/Data-*.md"):
                filename = os.path.basename(file_path).lower()
                if search_pattern in filename:
                    found_rag_file = file_path
                    break

            if not found_rag_file:
                expected_rag_file = f"rag_data/Data-{role.replace('_', '-').title()}.md"
                expected_raw_file = f"raw_data/transcript_{role}.md"
                if os.path.exists(expected_raw_file):
                    notification_message = f"I noticed we don't have structured data on {role.replace('_', ' ').title()}. I will now process the raw transcript and add it to our knowledge base. This may take a moment..."
                    if notify_callback: notify_callback(notification_message)
                    with open("rag_data/transcript_ingestion_prompt.md", 'r', encoding='utf-8') as f:
                        ingestion_instructions = f.read()
                    with open("rag_data/rag_template.md", 'r', encoding='utf-8') as f:
                        rag_template = f.read()
                    with open(expected_raw_file, 'r', encoding='utf-8') as f:
                        raw_content = f.read()
                        
                    ingestion_prompt = f"{ingestion_instructions}\n\nSchema/Template:\n{rag_template}\n\n---\n\nRaw Transcript to process:\n{raw_content}"
                    processed_response = generate_content_with_backoff(
                        client=client,
                        model='gemini-3.5-flash',
                        contents=ingestion_prompt
                    )
                    
                    with open(expected_rag_file, 'w', encoding='utf-8') as f:
                        f.write(processed_response.text)
                    if notify_callback: notify_callback(f"Raw transcript processed and knowledge base updated.")
                else:
                    if not allow_web_search:
                        needs_web_search_permission = True
                        notification_message = f"I couldn't find any real data for {role.replace('_', ' ').title()}. Should I proceed with an internet search? Please note that any data returned will not be validated. Reply 'yes' to proceed."
                        if notify_callback: notify_callback(notification_message)
                        return ai_response, notification_message, error_message, needs_web_search_permission

                    notification_message = f"I couldn't find any real data for {role.replace('_', ' ').title()}. I will perform a web-lookup to gather up-to-date information before proceeding."
                    if notify_callback: notify_callback(notification_message)
                    with open("rag_data/rag_template.md", 'r', encoding='utf-8') as f:
                        rag_template = f.read()
                        
                    synthetic_prompt = f"Perform a web-lookup to search for up-to-date information and industry insights regarding the role of a '{role.replace('_', ' ')}'. Using the results of this web-lookup, create highly detailed, realistic user interview insights. You MUST strictly follow the exact Markdown template and schema provided below. IMPORTANT: The schema contains placeholder examples for a real estate context (e.g., CoreLogic, Matrix, transactions). You MUST adapt these sections to fit the ACTUAL context of a '{role.replace('_', ' ')}'. Do not force real estate concepts if the role is unrelated. Adapt the technology stack, daily workflow, pain points, and business metrics to make sense for the requested role. Do not output anything outside the schema.\n\nHere is the schema:\n\n{rag_template}"
                    processed_response = generate_content_with_backoff(
                        client=client,
                        model='gemini-3.5-flash',
                        contents=synthetic_prompt,
                        config={"tools": [{"google_search": {}}]}
                    )
                    
                    warning_banner = "> [!WARNING]\n> ⚠️ **NOT VALIDATED WEB SEARCH DATA** ⚠️\n> This knowledge base was generated using up-to-date web-lookup data because no raw interview transcripts were found for this role. It is NOT VALIDATED.\n\n"
                    
                    with open(expected_rag_file, 'w', encoding='utf-8') as f:
                        f.write(warning_banner + processed_response.text)
                    if notify_callback: notify_callback(f"Web-lookup complete and synthetic data added to knowledge base.")
            else:
                notification_message = f"I am referencing the existing data for {role.replace('_', ' ').title()} to generate this artifact."
                if notify_callback: notify_callback(notification_message)

        # Phase 3: Artifact Generation & Fulfillment
        rag_contexts = []
        for key, rag_file_path in RAG_REGISTRY.items():
            if rag_file_path and os.path.exists(rag_file_path):
                with open(rag_file_path, 'r', encoding='utf-8') as f:
                    rag_contexts.append(f"--- {key} ---\n{f.read()}")
                    
        for file_path in glob.glob("rag_data/Data-*.md"):
            if file_path not in RAG_REGISTRY.values():
                with open(file_path, 'r', encoding='utf-8') as f:
                    rag_contexts.append(f"--- dynamically_loaded_{os.path.basename(file_path)} ---\n{f.read()}")
        
        rag_context = "\n\n".join(rag_contexts)

        if rag_context:
            combined_prompt = f"Context from RAG files:\n{rag_context}\n\nUser Request:\n{user_input}"
        else:
            combined_prompt = user_input

        if rag_context:
            combined_prompt = f"Context from RAG files:\n{rag_context}\n\nUser Request:\n{user_input}"
        else:
            combined_prompt = user_input

        if notify_callback: notify_callback(f"Synthesizing the final artifact...")

        response = generate_content_with_backoff(
            client=client,
            model='gemini-3.5-flash',
            contents=combined_prompt,
            config={"tools": [{"google_search": {}}]}
        )
        ai_response = response.text.strip()
        if ai_response.startswith("```"):
            lines = ai_response.split('\n')
            if lines[0].startswith("```") and lines[-1].strip() == "```":
                ai_response = '\n'.join(lines[1:-1]).strip()
        
        if response.usage_metadata:
            print(f"Input Token Count: {response.usage_metadata.prompt_token_count}")
            print(f"Output Token Count: {response.usage_metadata.candidates_token_count}")
            
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"

    return ai_response, notification_message, error_message, needs_web_search_permission
