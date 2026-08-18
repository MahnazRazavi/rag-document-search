# RAG Pipeline

## What is RAG?

Retrieval-Augmented Generation combines information retrieval with large language models.

Instead of asking the LLM to answer using only its internal knowledge, the system retrieves relevant information from an external knowledge base.

```text
User Question
      ↓
Retriever
      ↓
Relevant Documents
      ↓
LLM
      ↓
Answer
