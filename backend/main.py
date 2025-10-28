# backend/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.rag.faq_rag import generate_answer

app = FastAPI(
    title="Medical FAQ RAG Assistant",
    description="An intelligent RAG-based assistant that answers medical clinic FAQs using Chroma + SentenceTransformers + Groq LLM.",
    version="1.0"
)

class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "RAG backend is running!"}


@app.post("/ask")
def ask_question(request: QueryRequest):
    try:
        answer = generate_answer(request.query)
        return {
            "query": request.query,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


