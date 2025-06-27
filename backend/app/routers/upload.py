# app/routers/upload.py
import os, logging
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.embedder import process_documents
from app.utils.file_handler import load_file_as_document
import uuid

router = APIRouter()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/upload-docs")
async def upload_documents(
    file: UploadFile = File(...),
    session_id: str = Form(None),
    project_name: str = Form(None)
):
    try:
        logger.info(f"Upload started: filename={file.filename}, session_id={session_id}, project_name={project_name}")

        # Step 1: Generate session ID if not provided
        if not session_id:
            session_id = str(uuid.uuid4())
            logger.info(f"No session provided; generated session_id={session_id}")

        # Step 2: Load documents
        document = await load_file_as_document(file)
        documents = [document]
        logger.info(f"Loaded {len(documents)} Document(s)")

        # Step 3: Embed and store
        num_chunks = await process_documents(session_id=session_id, documents=documents)
        logger.info(f"Processed documents into {num_chunks} chunks")

        return {
            "status": "success",
            "session_id": session_id,
            "num_chunks": num_chunks
        }

    except Exception as e:
        logger.exception("❌ upload-docs failed")
        raise HTTPException(status_code=500, detail=str(e))
