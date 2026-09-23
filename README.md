# AI ERPNext Business Assistant

An AI-powered business assistant that connects to **ERPNext** and uses **LangGraph Reflection and Reflexion** to analyze, review, and improve sales-order responses.

<img width="1527" height="871" alt="image" src="https://github.com/user-attachments/assets/cfb6b8bc-9449-437e-adaf-4b4b3ef59a3e" />

## Architecture

```text
ERPNext
   ↓
Sales Order Service
   ↓
Analyzer
   ↓
Reflector
   ↓
Conditional Routing
   ├── Approved → END
   │
   └── Not Approved
          ↓
       Feedback
          ↓
        Lesson
          ↓
   Previous Attempts
          ↓
       Analyzer
          ↓
      Reflector
```

The workflow can repeat until the response is approved or the maximum iteration limit is reached.

## Key Features

* ERPNext REST API integration
* LLM-based sales order analysis
* LangGraph Reflection workflow
* Reflexion using feedback, lessons, and previous attempts
* Conditional routing and retry loop
* Maximum iteration control
* FastAPI API layer
* Gradio comparison UI
* Local LLM inference with Ollama

## Reflection

The **Analyzer** generates the sales-order summary.

The **Reflector** reviews the response for:

* Correctness
* Clarity
* Consistency

If the response is not approved, the workflow generates feedback and a lesson before trying the analysis again.

```text
Generate
   ↓
Review
   ↓
Feedback
   ↓
Lesson
   ↓
Improve
   ↓
Generate Again
```

## Reflexion

Reflexion extends the Reflection workflow by using information from previous attempts to improve the next attempt.

The workflow stores:

* Previous answer
* Critique
* Feedback
* Lesson

The next Analyzer attempt receives the lesson and previous attempts as additional context.

```text
Attempt
   ↓
Reflection
   ↓
Feedback
   ↓
Lesson
   ↓
Store Previous Attempt
   ↓
Next Attempt
```

The project uses a simple list in the LangGraph state for previous attempts. No vector database or long-term memory is required for this implementation.

## Gradio Demo

The UI compares the same sales-order analysis:

```text
┌─────────────────────┬────────────────────────┐
│ Without Reflexion   │ With Reflexion          │
│                     │                        │
│ Analyzer            │ Analyzer               │
│     ↓               │     ↓                  │
│ First Answer        │ Reflector              │
│                     │     ↓                  │
│                     │ Feedback               │
│                     │     ↓                  │
│                     │ Lesson                 │
│                     │     ↓                  │
│                     │ Analyzer Again         │
│                     │     ↓                  │
│                     │ Final Answer           │
└─────────────────────┴────────────────────────┘
```

The comparison helps demonstrate the difference between a direct LLM response and a response processed through the Reflexion workflow.

## Reliability Note

During testing, the LLM could still produce factual inconsistencies in some responses, even with the Reflexion workflow.

This demonstrates that Reflexion can improve the analysis process but does not guarantee factual correctness.

For future reliability improvements, deterministic operations such as counting and status classification can be handled in Python, while the LLM focuses on generating the natural-language explanation. Evaluation will also be added as a separate milestone.

## Tech Stack

**Python · FastAPI · LangGraph · LangChain · Ollama · Qwen 2.5 3B · ERPNext · Gradio**

## Project Structure

```text
ai-erpnext-assistant/

├── app/
│   ├── agents/
│   ├── api/
│   ├── erpnext/
│   └── graph/
├── data/
├── tests/
├── main.py
└── requirements.txt
```

## Current Status

* [x] ERPNext integration
* [x] Analyzer
* [x] Reflection
* [x] Reflexion
* [x] Conditional routing
* [x] Retry loop
* [x] Gradio UI
* [ ] Multi-Agent
* [ ] Multi-Graph / Subgraphs
* [ ] Evaluation
