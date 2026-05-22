# Huxley Copilot Workflow Diagram

This diagram maps the application's lifecycle from the moment a user submits a prompt, through the dynamic intent checking and data ingestion phases, all the way to the final artifact rendering on the canvas.

```mermaid
graph TD
    %% User Input Phase
    U([User submits prompt in UI]) --> F1["Fetch to /check_intent"]
    
    %% Phase 1: Intent Check
    subgraph Phase 1: Intent & Role Extraction
        F1 --> E["Gemini extracts 'Role' from prompt"]
        E --> C1{"Does rag_data/Data-[role].md exist?"}
    end

    %% Phase 2: Conditional Data Ingestion
    subgraph Phase 2: Dynamic Ingestion Logic
        %% Condition 1: RAG Data Exists
        C1 -- Yes --> R1["Condition 1: RAG Data Exists\n(Return 'Ready' to UI)"]
        
        %% Condition 2: Raw Transcript Exists
        C1 -- No --> C2{"Does raw_data/transcript_[role].md exist?"}
        
        C2 -- Yes --> R2["Condition 2: Raw Transcript Exists\n(Return Notification to UI)"]
        R2 --> P2["Read raw transcript & registry.md schema"]
        P2 --> G2["Gemini structures raw transcript into RAG format"]
        G2 --> S2[("Save to rag_data/Data-[role].md")]

        %% Condition 3: Synthetic Generation Fallback
        C2 -- No --> R3["Condition 3: No Data Exists\n(Return Synthetic Warning to UI)"]
        R3 --> P3["Read registry.md schema"]
        P3 --> G3["Gemini generates Synthetic RAG Data\nfrom training knowledge"]
        G3 --> W3["Prepend > [!WARNING] Banner"]
        W3 --> S3[("Save to rag_data/Data-[role].md")]
    end

    %% UI Interaction
    R1 --> UI{"UI receives intent response"}
    R2 --> UI
    R3 --> UI
    UI -- "If Notification/Warning exists" --> N["Display 🛠️ alert in chat panel"]
    UI --> F2["Fetch to / (Main Generation Route)"]
    N --> F2

    %% Phase 3: Final Generation
    subgraph Phase 3: Artifact Generation
        F2 --> L["Load all files in rag_data/\n(including newly generated files)"]
        L --> B["Bundle Context + User Prompt"]
        B --> G4["Gemini generates Final Artifact\n(Persona, JTBD, Journey Map)"]
    end

    %% Output Phase
    G4 --> O["Backend returns JSON response"]
    O --> M["marked.js parses Markdown to HTML"]
    M --> C(["Canvas updates with generated artifact\n& Loading Spinner hides"])

    %% Styling
    classDef user fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef ai fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef condition fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    
    class U,C user;
    class E,G2,G3,G4 ai;
    class C1,C2 condition;
```

### Flow Breakdown
1. **User Input:** The UI prevents a page reload, shows the loading spinner, and sends the prompt to the backend.
2. **Phase 1 (Intent Check):** The backend quickly uses Gemini to figure out *who* the user is asking about.
3. **Phase 2 (Dynamic Logic):** 
   - **Condition 1:** If the structured RAG file is already there, the backend does nothing extra.
   - **Condition 2:** If it's missing but a raw transcript is found, it automatically structures it using the `registry.md` schema.
   - **Condition 3:** If neither exists, it synthesizes realistic data from its training memory and clearly stamps it with a warning banner.
4. **Phase 3 (Fulfillment):** The application bundles whatever RAG data was found (or newly created), passes it to Gemini along with your original prompt, and generates the final output for the canvas.
