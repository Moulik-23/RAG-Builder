from fastapi import APIRouter, HTTPException, Query
from app.services.scraper import scrape_website
from app.services.embedder import process_documents
import uuid

router = APIRouter()

@router.post("/scrape")
async def scrape(url: str = Query(...), max_depth: int = 1):
    try:
        documents = scrape_website(url, max_depth=max_depth)
        session_id = str(uuid.uuid4())
        num_chunks = await process_documents(session_id=session_id, documents=documents)

        return {
            "status": "success",
            "session_id": session_id,
            "num_chunks": num_chunks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))