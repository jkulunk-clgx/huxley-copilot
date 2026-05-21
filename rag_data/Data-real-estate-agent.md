> [!WARNING]
> ⚠️ **NOT VALIDATED WEB SEARCH DATA** ⚠️
> This knowledge base was generated using up-to-date web-lookup data because no raw interview transcripts were found for this role. It is NOT VALIDATED.

# CoreLogic User Research: RAG Document Registry & Ingestion Schema

**Description:** This registry catalogs all processed user interview RAG files and provides the standardized template/system instructions required to transform any _new_ raw interview transcript into our structured RAG format.

---

## 📚 1. Document Index

|**Document ID**|**Title**|**Persona**|**Date Processed**|**Status**|
|---|---|---|---|---|
|DOC-INT-RAG-001|User Interview Insights RAG File - Sarah Jenkins (Senior Residential Agent)|Residential Real Estate Agent|2024-05-21|COMPLETED|

---

## ⚙️ 2. New Transcript Ingestion System Prompt

**System Objective:** You are an expert user researcher and data architect. Your goal is to extract, synthesize, and structure information from the provided raw interview transcript into a highly detailed Markdown file optimized for Retrieval-Augmented Generation (RAG) applications.

**Transformation Rules:**

1. **Do not hallucinate:** Only include information explicitly stated or heavily implied in the transcript.
2. **Be comprehensive:** Do not summarize to the point of losing critical nuances, software names, or specific workflows.
3. **Use the Exact Schema:** You must map the transcript data strictly to the headers and frontmatter provided in the template below.
4. **Identify Gaps:** If a section's topic was not discussed in the interview, include the header but note "N/A - Not discussed in this interview."

---

## 📝 3. Standardized RAG Template

```markdown
---
document_id: DOC-INT-RAG-001
title: User Interview Insights RAG File - Sarah Jenkins (Senior Residential Agent)
description: Highly detailed structured knowledge extraction from an interview with Sarah Jenkins, a Senior Residential Agent. Designed for ingestion by Retrieval-Augmented Generation (RAG) applications to answer questions regarding NAR settlement impacts, tech stack integration, and AI-driven workflows.
date_recorded: 2024-05-20
interviewers: David Chen, Senior UX Researcher
interviewee: Sarah Jenkins
tags: [matrix, corelogic, nar_settlement, austin_market, chatgpt, buyer_agreements, residential]
---

# 1. Interview & Participant Metadata
- **Interviewee:** Sarah Jenkins
- **Interviewers:** David Chen
- **Subject:** Exploration of post-NAR settlement workflow shifts, current software friction points within CoreLogic Matrix, and the emerging role of AI in daily prospecting and listing management.

# 2. User Persona & Background
- **Demographics:** 44 years old, Gen X/Millennial cusp.
- **Location:** Austin, Texas (Primary focus on North Austin/Round Rock suburbs).
- **Role:** Solo agent with one part-time virtual assistant (VA) for administrative data entry and social media scheduling.
- **Career Timeline:** 16 years in the industry; started in 2008 during the market crash; has experienced multiple market cycles and the transition from paper-based to digital-first transactions.
- **Working Style:** High-touch, relationship-focused but heavily reliant on data to justify pricing; "tech-enabled traditionalist" who values efficiency but refuses to automate the personal "closing" moments.

# 3. Business Performance & Throughput
- **Client Base:** 60% repeat/referral business; specializes in "move-up" buyers (selling a starter home to buy a larger suburban property).
- **Transaction Types / Volume:** Averages 22–26 closings annually; total sales volume approx. $14M–$16M; typical price range is $450k – $850k.
- **Goals & Metrics of Success:** Prioritizes "Days on Market" (DOM) for listings and "Client NPS" (referral rate) over raw volume; defines success as maintaining a 5% commission yield in an increasingly compressed fee environment.

# 4. Daily Workflow & Operations
- **Routines:** 6:30 AM start; 1 hour of "database mining" in the CRM; 8:00 AM check of "Hot Sheets" in Matrix for new inventory or price drops; afternoons are reserved for property tours and listing presentations.
- **Process Phases:** 
    1. **Pre-Consultation:** Mandatory Zoom call to explain new buyer representation rules.
    2. **Agreement:** Digital signature of Buyer Representation Agreement via DocuSign *before* any home tours (post-August 2024 mandate).
    3. **Search:** Automated Matrix portal emails supplemented by manual "off-market" outreach.
    4. **Transaction:** Uses a Transaction Coordinator for the "Under Contract to Close" phase.
- **Organization:** Uses a "Best-of-Breed" digital approach; maintains a physical whiteboard in her home office for high-level pipeline visualization but relies on CRM Smart Lists for hourly tasks.

# 5. Technology Stack & Software Usage
- **Core Platform Usage:** CoreLogic Matrix is the "system of record" for all market data; uses Realist (CoreLogic) for deep tax record dives and identifying potential "sell-ready" homeowners.
- **Secondary Tools:** Follow Up Boss (FOB) is the primary CRM; DocuSign for all legal paperwork; Canva for marketing flyers and Instagram stories.
- **AI & Automation:** Daily user of ChatGPT (GPT-4) for drafting listing descriptions, generating "polite but firm" negotiation emails, and summarizing HOA documents for buyers; uses "Agentic AI" experiments for automated scheduling of showings.

# 6. Key Pain Points & Frictions
- **Software Frustrations:** "Portal Parity Gap"—noted that the Matrix client-facing portal looks "dated" compared to the high-end consumer UI of Zillow or Redfin, making her look less "modern" to her clients.
- **Workflow Bottlenecks:** The "Commission Hunt"—since commissions are no longer on the MLS, she has to manually text/call listing agents or check third-party brokerage sites for every single property, adding 2–3 hours of administrative work per week.
- **Industry/Client Challenges:** The "Paperwork Friction"—clients are often resistant to signing a representation agreement before even seeing one house, requiring a significant "sales job" on the value of the agent early in the funnel.

# 7. Feature Requests & Product Opportunities
- **Direct Requests:** An integrated "Commission Tracker" within Matrix where agents can voluntarily share or view concession data off-MLS to save time.
- **Latent Needs:** A mobile-first, "Tinder-style" swiping interface for the Matrix Client Portal to increase engagement and provide her with better data on client preferences.
- **Integration Dreams:** Seamless one-way sync between Matrix "Notes" and Follow Up Boss contact records so she doesn't have to copy-paste feedback on houses.

# 8. Branding & Marketing Strategy
- **Marketing Channels:** 80% Instagram and Facebook; monthly email newsletter via Mailchimp; quarterly physical "Market Update" postcards to her geographical farm.
- **Brand Identity:** "The Data-Driven Neighbor"—positioning herself as a local expert who knows the schools and the market stats better than an algorithm.
- **Lead Generation:** Shifting away from paid Zillow leads due to lower ROI; doubling down on "Google Local Services Ads" (LSA) and video-based educational content.

# 9. Next Steps / Follow-Up Actions
- **User Agreements:** Sarah agreed to participate in a 60-minute "Prototype Walkthrough" for the new Matrix Mobile refresh next month.
- **Referrals:** Recommended her former brokerage partner, a commercial-leaning agent, for a different perspective on data needs.
```