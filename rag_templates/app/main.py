from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chain import load_chain

app = FastAPI(title="Exported RAG App")

# Load RAG chain on startup
qa_chain = load_chain()

class Question(BaseModel):
    query: str

@app.post("/chat")
def ask_question(q: Question):
    response = qa_chain.run(q.query)
    return {"answer": response}
