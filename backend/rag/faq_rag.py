# backend/rag/faq_rag.py

import os
from dotenv import load_dotenv
from groq import Groq
from backend.rag.vector_store import retrieve_relevant_docs

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query: str):
    """
    Retrieve context from vector store and generate an answer using Groq LLM.
    """
    context_docs = retrieve_relevant_docs(query)
    context_text = "\n".join(context_docs)

    prompt = f"""
    You are a helpful medical clinic assistant. 
    Use the following context to answer the user's question accurately.
    If the answer is not found in the context, say "I'm sorry, I don't have that information."

    Context:
    {context_text}

    Question: {query}

    Answer:
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # or whichever Groq model you want
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("💬 Medical FAQ RAG Chat (Groq Powered)")
    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = generate_answer(query)
        print("Bot:", answer)
