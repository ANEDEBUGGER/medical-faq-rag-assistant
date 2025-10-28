# backend/rag/vector_store.py

# backend/rag/vector_store.py

import os
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer

load_dotenv()

# Initialize local embedder and ChromaDB
embedder = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path=os.getenv("VECTOR_DB_PATH", "./data/vectordb"))
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/vectordb")

def get_vector_store():
    """Return the Chroma collection for clinic FAQs."""
    return chroma_client.get_or_create_collection(name="clinic_faqs")


def get_embedding(text: str):
    """Generate embedding for a user query using local model."""
    return embedder.encode(text).tolist()


def retrieve_relevant_docs(query: str, top_k: int = 3):
    """Retrieve top matching FAQ entries from the vector store."""
    collection = get_vector_store()
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    if not results["documents"]:
        return ["Sorry, I couldn't find any relevant information."]

    retrieved_docs = [doc for doc in results["documents"][0]]
    return retrieved_docs


if __name__ == "__main__":
    user_query = input("Ask a question: ")
    answers = retrieve_relevant_docs(user_query)
    print("\n Top Results:")
    for ans in answers:
        print("-", ans)

