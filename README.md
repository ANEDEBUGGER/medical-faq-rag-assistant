#Medical FAQ RAG Assistant

A Retrieval-Augmented Generation (RAG)-based chatbot designed to answer clinic and medical FAQs using context-aware document retrieval and LLM reasoning.
This project follows the exact RAG workflow and implementation described in the assessment PDF, using Groq API, ChromaDB, and FastAPI + Streamlit.

#Project Overview

The Medical FAQ RAG Assistant allows users to ask healthcare-related questions (e.g., insurance, appointments, billing, etc.), retrieves relevant information from a local knowledge base (clinic_info.json), and generates precise answers using the Groq LLM API.

#Features

1. Retrieval-Augmented Generation (RAG) pipeline

2. Uses Groq API for LLM inference

3. ChromaDB for vector-based document search

4.Streamlit frontend for interactive Q&A

5. FastAPI backend for modular design

Project Architecture Diagram:
<img width="660" height="838" alt="flowchar_overview" src="https://github.com/user-attachments/assets/fd5571af-16b8-4f57-8fce-fc8f7fa376ff" />




#PROJECT STRUCTURE 

medical-faq-rag-assistant/
│
├── backend/
│   └── rag/
│       ├── embeddings.py        # Create and store embeddings in vector DB
│       ├── vector_store.py      # Handles retrieval from ChromaDB
│       ├── faq_rag.py           # Main RAG pipeline logic
│       └── main.py              # FastAPI app for serving queries
│
├── data/
│   └── clinic_info.json         # Knowledge base (from assessment PDF)
│
├── app.py                       # Streamlit UI for chatbot
├── requirements.txt             # Project dependencies
├── .env                         # Contains Groq API Key
└── .gitignore

#RAG Workflow

Document Loading:
Loads clinic_info.json containing predefined medical FAQs.

Chunking:
The content is split into small chunks for better semantic search.

Embedding Creation:
Uses Groq embedding model to convert text chunks into vector representations.

Vector Storage:
Stores all embeddings in ChromaDB for similarity retrieval.

Query Processing:
The user’s query is converted into an embedding and compared against stored vectors.

Context Retrieval:
Top matching documents are retrieved as context.

LLM Response Generation:
The context and user query are passed to the Groq API to generate the final answer.


#Setup and Installation
1. Clone the Repository
git clone https://github.com/ANEDEBUGGER/medical-faq-rag-assistant.git
cd medical-faq-rag-assistant

2.Create Virtual Environment

python -m venv venv
venv\Scripts\activate          # (on Windows)

3. Install Dependencies
pip install -r requirements.txt  # Check in requirements.txt

4. Set Up API Key
GROQ_API_KEY=your_groq_api_key_here  # in .env

5. Prepare Data

Ensure your FAQ data file exists at:
data/clinic_info.json

6. Run the Backend (FastAPI)

This hosts the RAG pipeline as an API.
uvicorn backend.rag.main:app --reload

You should see:
INFO:     Application startup complete.
INFO:     127.0.0.1:8000 - "GET /health HTTP/1.1" 200 OK

7. Run the Frontend (Streamlit UI)
   streamlit run app.py


#Future Enhancements

Add PDF/Text document ingestion

Multi-language support

Deploy via Docker + CI/CD

Add memory & chat history

Integrate with LangChain for advanced pipelines

#proof snippets of the project: 
Streamlit UI and fastapi(swagger ui) interface 
<img width="895" height="546" alt="ui1_snippet" src="https://github.com/user-attachments/assets/87ff4e02-6a07-4d60-a4ac-0e399341b3e0" />
<img width="898" height="526" alt="ui_snippet" src="https://github.com/user-attachments/assets/fce9419d-de82-485d-8acb-5a530299cd18" />
<img width="918" height="528" alt="streamlit_ui_ask1" src="https://github.com/user-attachments/assets/a9ed5521-e769-4d82-8f53-20ba15e7d89c" />
<img width="903" height="518" alt="streamlit_ui" src="https://github.com/user-attachments/assets/f55ad098-9f11-457b-b947-aef6c09e8f31" />
<img width="822" height="457" alt="streamlit_ask4" src="https://github.com/user-attachments/assets/571ad3dd-f301-46ea-b323-5d936f834a14" />
<img width="886" height="664" alt="streamlit_ask3" src="https://github.com/user-attachments/assets/0bf11351-681c-419d-bd67-9b0f6fcccf7d" />
<img width="854" height="673" alt="streamlit_ask2" src="https://github.com/user-attachments/assets/e45eac4f-90d1-466c-84ba-b91c74b9605b" />
<img width="716" height="141" alt="medical_rag_snaps" src="https://github.com/user-attachments/assets/8c98f953-92ff-4e14-bf9b-447d6367ff79" />












