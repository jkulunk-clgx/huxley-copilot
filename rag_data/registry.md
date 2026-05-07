# CoreLogic User Research: RAG Document Registry & Ingestion Schema

**Description:** This registry catalogs all processed user interview RAG files and provides the standardized template/system instructions required to transform any _new_ raw interview transcript into our structured RAG format.

---

## 📚 1. Document Index

|**Document ID**|**Title**|**Persona**|**Date Processed**|**Status**|
|---|---|---|---|---|
|**DOC-INT-RAG-001**|User Interview Insights - Jerry|Real Estate Agent|2026-04-21|Active|
|**DOC-INT-RAG-002**|User Interview Insights - Angie|Mortgage Lender|2026-04-21|Active|

---

## ⚙️ 2. New Transcript Ingestion System Prompt

_To process a new interview transcript, apply the following system instructions to the LLM or processing pipeline:_

**System Objective:** You are an expert user researcher and data architect. Your goal is to extract, synthesize, and structure information from the provided raw interview transcript into a highly detailed Markdown file optimized for Retrieval-Augmented Generation (RAG) applications.

**Transformation Rules:**

1. **Do not hallucinate:** Only include information explicitly stated or heavily implied in the transcript.
    
2. **Be comprehensive:** Do not summarize to the point of losing critical nuances, software names, or specific workflows.
    
3. **Use the Exact Schema:** You must map the transcript data strictly to the headers and frontmatter provided in the template below.
    
4. **Identify Gaps:** If a section's topic was not discussed in the interview, include the header but note "N/A - Not discussed in this interview."
    

---

## 📝 3. Standardized RAG Template

Markdown

```
---
document_id: DOC-INT-RAG-[INCREMENT_ID]
title: User Interview Insights RAG File - [Interviewee Name] ([Job Title])
description: Highly detailed structured knowledge extraction from an interview with [Interviewee Name], a [Job Title]. Designed for ingestion by Retrieval-Augmented Generation (RAG) applications to answer questions regarding [Key Topic 1], [Key Topic 2], and [Key Topic 3].
date_recorded: [YYYY-MM-DD]
interviewers: [Comma-separated list of interviewers]
interviewee: [Interviewee Name]
tags: [tag1, tag2, tag3, software_name, persona_type]
---

# 1. Interview & Participant Metadata
- **Interviewee:** [Name]
- **Interviewers:** [Names]
- **Subject:** [1-2 sentences summarizing the core focus of the interview]

# 2. User Persona & Background
- **Demographics:** [Age, generation, relevant personal details]
- **Location:** [Operating region/state]
- **Role:** [Specific title and structural context, e.g., solo agent, team lead, operations manager]
- **Career Timeline:** [Years of experience, previous roles, major career shifts]
- **Working Style:** [Personality traits, organizational methods, general approach to clients]

# 3. Business Performance & Throughput
- **Client Base:** [Target demographic, typical client type]
- **Transaction Types / Volume:** [Sales volume, typical price ranges, active workload capacity]
- **Goals & Metrics of Success:** [What drives the user, how they define a successful outcome/relationship]

# 4. Daily Workflow & Operations
- **Routines:** [Morning routines, daily habits]
- **Process Phases:** [Step-by-step breakdown of how they handle a client from lead to close]
- **Organization:** [How they keep track of tasks, e.g., physical boards, digital planners]

# 5. Technology Stack & Software Usage
- **Core Platform Usage:** [Specifically detail usage of primary tools like CoreLogic, Matrix, HomeBot, etc.]
- **Secondary Tools:** [CRM, forms, communication platforms like Slack/Teams/Salesforce]
- **AI & Automation:** [Usage of tools like ChatGPT, automated marketing platforms]

# 6. Key Pain Points & Frictions
- **Software Frustrations:** [Bugs, bad UI, missing features, lack of customer support]
- **Workflow Bottlenecks:** [Tasks that take too long, manual data entry, lost visibility]
- **Industry/Client Challenges:** [Media narratives, client behavior, market conditions]

# 7. Feature Requests & Product Opportunities
- **Direct Requests:** [Specific tools or toggles the user explicitly asked for]
- **Latent Needs:** [Tools that would solve a described problem, even if the user didn't name a specific feature]
- **Integration Dreams:** [Desired connections between separate tools]

# 8. Branding & Marketing Strategy
- **Marketing Channels:** [Direct mail, TikTok, YouTube, email newsletters]
- **Brand Identity:** [How they want to be perceived by clients, visual consistency]
- **Lead Generation:** [How marketing translates to actual business/referrals]

# 9. Next Steps / Follow-Up Actions
- **User Agreements:** [Did they agree to beta testing or future follow-ups?]
- **Referrals:** [Did they suggest other people to interview?]
```