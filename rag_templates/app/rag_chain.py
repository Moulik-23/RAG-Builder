from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains.retrieval_qa.base import RetrievalQA
from app.config import EMBEDDING_MODEL_NAME, LLM_MODEL_NAME
import os

def load_chain(session_id: str):
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # Dynamically load vectorstore path for the session
    vectorstore_path = os.path.join("app", "vectorstores", session_id)
    if not os.path.exists(vectorstore_path):
        raise ValueError(f"No vectorstore found for session: {session_id}")

    vectorstore = FAISS.load_local(vectorstore_path, embeddings)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    llm = ChatGroq(model=LLM_MODEL_NAME)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    return qa_chain
