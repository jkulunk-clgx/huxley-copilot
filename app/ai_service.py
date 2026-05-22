import os
import glob
from google import genai

RAG_REGISTRY = {
    "default": "rag_data/registry.md",
    "system_instructions": "rag_data/system_instructions.md",
    "persona_format": "output_formats/persona_format.json",
    "JTBD_format": "output_formats/JTBD_format.json",
    "journey_map_format": "output_formats/journey_map_format.json",
    "data": "rag_data/Data-Real-Estate-Agent-001.md"
}

def extract_role_from_input(user_input, api_key):
    """Fallback intent/role extraction if not provided directly."""
    try:
        client = genai.Client(api_key=api_key)
        extraction_prompt = f"Extract the target user role from this user request: '{user_input}'. Return only the role name in snake_case (e.g. data_scientist, mortgage_lender), or 'None' if no role is specified."
        role_response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=extraction_prompt
        )
        return role_response.text.strip().lower()
    except Exception as e:
        print(f"Error extracting role: {e}")
        return "none"

def generate_ai_response(user_input, role=None, api_key=None, allow_web_search=False):
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
            role = extract_role_from_input(user_input, api_key)
            
        # Phase 2: Raw Data Ingestion (Conditional)
        if role and role != "none":
            expected_rag_file = f"rag_data/Data-{role.replace('_', '-')}.md"
            if not os.path.exists(expected_rag_file):
                expected_raw_file = f"raw_data/transcript_{role}.md"
                if os.path.exists(expected_raw_file):
                    notification_message = f"I noticed we don't have structured data on {role.replace('_', ' ').title()}. I will now process the raw transcript and add it to our knowledge base. This may take a moment..."
                    with open("rag_data/registry.md", 'r', encoding='utf-8') as f:
                        registry_content = f.read()
                    with open(expected_raw_file, 'r', encoding='utf-8') as f:
                        raw_content = f.read()
                        
                    ingestion_prompt = f"{registry_content}\n\n---\n\nRaw Transcript to process:\n{raw_content}"
                    processed_response = client.models.generate_content(
                        model='gemini-3-flash-preview',
                        contents=ingestion_prompt
                    )
                    
                    with open(expected_rag_file, 'w', encoding='utf-8') as f:
                        f.write(processed_response.text)
                else:
                    if not allow_web_search:
                        needs_web_search_permission = True
                        notification_message = f"I couldn't find any real data for {role.replace('_', ' ').title()}. Should I proceed with an internet search? Please note that any data returned will not be validated. Reply 'yes' to proceed."
                        return ai_response, notification_message, error_message, needs_web_search_permission

                    notification_message = f"I couldn't find any real data for {role.replace('_', ' ').title()}. I will perform a web-lookup to gather up-to-date information before proceeding."
                    with open("rag_data/registry.md", 'r', encoding='utf-8') as f:
                        registry_content = f.read()
                        
                    synthetic_prompt = f"Perform a web-lookup to search for up-to-date information and industry insights regarding the role of a '{role.replace('_', ' ')}'. Using the results of this web-lookup, create highly detailed, realistic user interview insights. You MUST strictly follow the exact Markdown template and schema provided below. Do not output anything outside the schema.\n\nHere is the schema:\n\n{registry_content}"
                    processed_response = client.models.generate_content(
                        model='gemini-3-flash-preview',
                        contents=synthetic_prompt,
                        config={"tools": [{"google_search": {}}]}
                    )
                    
                    warning_banner = "> [!WARNING]\n> ⚠️ **NOT VALIDATED WEB SEARCH DATA** ⚠️\n> This knowledge base was generated using up-to-date web-lookup data because no raw interview transcripts were found for this role. It is NOT VALIDATED.\n\n"
                    
                    with open(expected_rag_file, 'w', encoding='utf-8') as f:
                        f.write(warning_banner + processed_response.text)
            else:
                notification_message = f"I am referencing the existing data for {role.replace('_', ' ').title()} to generate this artifact."

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

        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=combined_prompt,
            config={"tools": [{"google_search": {}}]}
        )
        ai_response = response.text
        
        if response.usage_metadata:
            print(f"Input Token Count: {response.usage_metadata.prompt_token_count}")
            print(f"Output Token Count: {response.usage_metadata.candidates_token_count}")
            
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"

    return ai_response, notification_message, error_message, needs_web_search_permission
