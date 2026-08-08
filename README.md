# Agentic-AI-Experiments
Applied Agentic AI Assignment
This repository contains the implementations of three Agentic AI laboratory experiments developed using Python and Ollama.

Experiments
EXP1 - Text-to-SQL Workflow
A natural language question is converted into an SQL query and executed on a SQLite database.

Technologies:

Python
SQLite
Ollama
Llama 3.2
SQL
Workflow:

User Question → LLM → SQL Query → SQLite Database → Result

EXP2 - RAG-Based Question Answering System
A knowledge base is used to retrieve relevant information before generating an answer using an LLM.

Technologies:

Python
Ollama
Llama 3.2
Sentence Transformers
Scikit-learn
Workflow:

Knowledge Base → Chunking → Embeddings → Similarity Search → Relevant Context → LLM → Answer

EXP3 - Prompt Chaining for Summarization
A multi-step LLM workflow where the output of one prompt becomes the input to the next prompt.

Technologies:

Python
Ollama
Llama 3.2
Workflow:

Topic → Summary → Key Points → Questions

Requirements
Install Ollama and download the Llama 3.2 model:

ollama pull llama3.2
