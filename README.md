# AI ERPNext Business Assistant

An AI-powered business assistant that connects with ERPNext and uses **LangGraph Reflection** to analyze and review sales order information.

## Current Implementation

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
* Reflection-based response review
* LangGraph state management
* Conditional routing and retry loop
* Maximum iteration control
* FastAPI API layer
* Local LLM inference using Ollama

## Tech Stack

**Python · FastAPI · LangGraph · LangChain · Ollama · Qwen 2.5 3B · ERPNext**

## Project Structure

```text
ai-erpnext-assistant/
├── app/
│   ├── api/
│   ├── agents/
│   ├── erpnext/
│   └── graph/
├── data/
├── tests/
└── main.py
```

## Reflection Workflow

The Analyzer generates the response, while the Reflector reviews it for **correctness, clarity, and consistency**.

If the response is not approved, the workflow can retry the analysis. A maximum iteration limit prevents infinite loops.

## Learning Focus

This implementation demonstrates practical use of:

**State → Nodes → Edges → Conditional Routing → Reflection → Retry → Termination**
