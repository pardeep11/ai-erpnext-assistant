# AI ERPNext Business Assistant

An AI-powered business assistant that connects to **ERPNext** and uses **LangGraph Reflection** to analyze, review, and improve sales-order responses.

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
   ├── Retry → Analyzer
   └── Max Iterations → END
```

## Key Features

* ERPNext REST API integration
* LLM-based sales order analysis
* LangGraph Reflection workflow
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

If the response is not approved, LangGraph routes the workflow back to the Analyzer for another attempt.

```text
Generate → Review → Decide → Retry / Terminate
```

## Gradio Demo

The UI compares the same analysis:

```text
┌─────────────────────┬─────────────────────┐
│ Without Reflection  │ With Reflection     │
│                     │                     │
│ Analyzer            │ Analyzer            │
│     ↓               │     ↓               │
│ First Answer        │ Reflector           │
│                     │     ↓               │
│                     │ Final Answer        │
└─────────────────────┴─────────────────────┘
```

*Add screenshot here showing the working Gradio UI.*

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
* [x] Conditional routing
* [x] Retry loop
* [x] Gradio UI
* [ ] Reflexion
* [ ] Multi-Agent
* [ ] Multi-Graph / Subgraphs
* [ ] Evaluation
