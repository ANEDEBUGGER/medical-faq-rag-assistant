# backend/rag/embeddings.py


import json
import os
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()

# Initialize local embedding model and Chroma client
embedder = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path=os.getenv("VECTOR_DB_PATH", "./data/vectordb"))
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/vectordb")

def generate_embeddings(text):
    """Generate embeddings using a local transformer model."""
    return embedder.encode(text).tolist()


def build_vector_store():
    """Read clinic_info.json, create embeddings, and store them in ChromaDB."""
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_path = os.path.join(base_dir, "data", "clinic.info.json")

    with open(data_path, "r", encoding="utf-8") as f:
        clinic_data = json.load(f)

    collection = chroma_client.get_or_create_collection(name="clinic_faqs")

    for category, items in clinic_data.items():
        for key, value in items.items():
            doc_id = f"{category}_{key}"
            text = f"{category} - {key}: {value}"
            embedding = generate_embeddings(text)
            collection.add(
                ids=[doc_id],
                embeddings=[embedding],
                documents=[text],
                metadatas=[{"category": category, "topic": key}]
            )

    print("Embeddings generated and stored successfully (local model).")


if __name__ == "__main__":
    build_vector_store()

