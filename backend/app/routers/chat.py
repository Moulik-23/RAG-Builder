from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import os
import logging
from dotenv import load_dotenv
load_dotenv()
router = APIRouter()

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatRequest(BaseModel):
    query: str
    session_id: str

@router.post("/chat")
async def chat(req: ChatRequest):
    try:
        logger.info(f"Received query: {req.query} for session_id: {req.session_id}")
        vector_path = f"app/vectorstores/{req.session_id}"

        if not os.path.exists(vector_path):
            logger.warning("Vectorstore not found.")
            raise HTTPException(status_code=404, detail="Session vectorstore not found")

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        vectorstore = FAISS.load_local(vector_path, embeddings,allow_dangerous_deserialization=True)

        retriever = vectorstore.as_retriever()
        llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct",api_key="your_api_key")
        qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

        answer = qa.run(req.query)
        logger.info(f"Answer generated: {answer}")

        return {"answer": answer}

    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
