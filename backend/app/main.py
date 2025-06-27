from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import upload, scrape, chat

app = FastAPI(title="RAG Builder API")

# CORS config for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(upload.router, prefix="/api")
app.include_router(scrape.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
#app.include_router(export.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the RAG Builder Backend!"}
