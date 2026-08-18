# System Architecture

## Overview

The system consists of five major layers:

1. API
2. Document processing
3. Persistence
4. Retrieval
5. Generation

---

## High-Level Architecture

```text
                         Client
                           │
                           ▼
                       FastAPI
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
        Document API                  Chat API
             │                           │
             ▼                           ▼
      Document Service           Retrieval Service
             │                           │
       ┌─────┴─────┐               ┌─────┴─────┐
       │           │               │           │
       ▼           ▼               ▼           ▼
   Extractor    PostgreSQL     Embedding    Qdrant
                                   │
                                   ▼
                                Context
                                   │
                                   ▼
                                  LLM
