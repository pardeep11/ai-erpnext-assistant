# AI ERPNext Business Assistant

An AI-powered business assistant that connects to **ERPNext** and uses **LangGraph Reflection and Reflexion** to analyze, review, and improve customer-specific sales-order responses.

## Architecture

```text
User
  ↓
Customer
  ↓
Sales Order Service
  ↓
Customer-wise ERPNext Filter
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
* Customer-wise sales-order retrieval
* LLM-based sales-order analysis
* LangGraph Reflection workflow
* Reflexion using feedback, lessons, and previous attempts
* Conditional routing and retry loop
* Maximum iteration control
* FastAPI API layer
* Gradio comparison UI
* Local LLM inference with Ollama

## Customer-wise Sales Order Retrieval

The assistant retrieves sales orders for the requested customer instead of fetching orders from all customers.

For example:

```text
Customer: Sandeep
        ↓
ERPNext Sales Order API
        ↓
Filter: customer = Sandeep
        ↓
Only Sandeep's Sales Orders
```

This ensures that the Analyzer receives only the relevant customer's sales-order data.

## Reflection

The **Analyzer** generates the sales-order summary.

The **Reflector** reviews the response for:

* Correctness
* Clarity
* Consistency
* Unsupported claims or assumptions

If the response is not approved, LangGraph routes the workflow through the improvement process.

```text
Generate
   ↓
Review
   ↓
Decide
   ↓
Retry / Terminate
```

### Reflection Demo

Screenshot showing the Reflection workflow.

<img width="1512" height="883" alt="Reflection workflow" src="https://github.com/user-attachments/assets/43733d76-b632-42d4-8824-a2fb49d8bd93" />

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

A simple list in the LangGraph state is used to store previous attempts. No vector database or long-term memory is used for this implementation.

### Reflexion Demo

Screenshot showing the current Reflexion workflow.

<img width="1578" height="697" alt="Reflexion workflow" src="https://github.com/user-attachments/assets/cc088645-eefe-40ca-87b9-168663b84b28" />

## Gradio Demo

The Gradio UI compares the same customer-specific sales-order analysis:

```text
┌─────────────────────┬────────────────────────┐
│ Without Reflexion   │ With Reflexion         │
│                     │                        │
│ Customer            │ Customer               │
│    ↓                │    ↓                   │
│ Analyzer            │ Analyzer               │
│    ↓                │    ↓                   │
│ First Answer        │ Reflector              │
│                     │    ↓                   │
│                     │ Feedback               │
│                     │    ↓                   │
│                     │ Lesson                 │
│                     │    ↓                   │
│                     │ Analyzer Again         │
│                     │    ↓                   │
│                     │ Final Answer            │
└─────────────────────┴────────────────────────┘
```

The comparison demonstrates the difference between a direct LLM response and a response processed through the Reflexion workflow.

## Reliability Note

During testing, the LLM could still produce factual inconsistencies in some responses, even with the Reflexion workflow.

This demonstrates that Reflexion can improve the analysis and review process but does not guarantee factual correctness.

Future reliability improvements will include deterministic validation and evaluation.

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
* [x] Customer-wise sales-order retrieval
* [x] Analyzer
* [x] Reflection
* [x] Reflexion
* [x] Conditional routing
* [x] Retry loop
* [x] Gradio UI
* [ ] Multi-Agent
* [ ] Multi-Graph / Subgraphs
* [ ] Evaluation
