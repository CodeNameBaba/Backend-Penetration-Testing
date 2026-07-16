<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:0B132B,50:1C2541,100:3A86FF&text=Banking%20System%20&%20Auth&fontAlign=50&fontAlignY=40&fontSize=38&fontColor=ffffff&animation=fadeIn"/>
</p>

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=1000&color=3A86FF&center=true&vCenter=true&width=800&lines=Authentication+Logic.;JSON+Data+Persistence.;Cross-Module+Imports.;Transactional+State+Management." />
</p>

---

# 🏦 Core Banking & Transfer System

In this session, we transition from basic user creation to managing **relational state and modular execution**. We are simulating a core backend service where a user can authenticate, verify their identity, and execute state-changing operations (fund transfers) safely.

This module introduces structural separation: dividing functional logic (`main.py`) from the execution environment (`bank.py`).

---

## ⚙️ System Architecture & Workflow

To understand how real backends process transactions, we need to map the logical flow. Below is the system diagram for our `transfer()` function to visualize the checks happening before data is committed to our database (`users.json`).

```mermaid
graph TD;
    %% Styling
    classDef default fill:#1C2541,stroke:#3A86FF,stroke-width:2px,color:#fff;
    classDef error fill:#4a1515,stroke:#ff3a3a,stroke-width:2px,color:#fff;
    classDef success fill:#154a22,stroke:#3aff5e,stroke-width:2px,color:#fff;

    A[Start Transfer] --> B{Does Payee Exist?};
    B -- No --> C[Throw: User Not Found];
    B -- Yes --> D{Is Payee == Sender?};
    
    D -- Yes --> E[Throw: Cannot Transfer to Self];
    D -- No --> F[Prompt Confirmation];
    
    F -- Confirm --> G{Sufficient Balance?};
    
    G -- No --> H[Throw: Insufficient Funds];
    G -- Yes --> I[Deduct Sender Balance];
    
    I --> J[Credit Payee Balance];
    J --> K[JSON Dump / Commit State];
    K --> L((Transaction Successful));

    class C,E,H error;
    class L success;