import os
from app.services.chunker import split_documents
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
async def process_documents(session_id: str, documents: list) -> int:
    # Step 1: Split into chunks
    chunks = split_documents(documents)

    # Step 2: Embed chunks
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Step 3: Save to disk
    output_path = f"app/vectorstores/{session_id}"
    os.makedirs(output_path, exist_ok=True)
    vectorstore.save_local(output_path)

    return len(chunks)
