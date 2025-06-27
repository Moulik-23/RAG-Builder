import os
import tempfile
from langchain.schema import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from fastapi import UploadFile

async def load_file_as_document(file: UploadFile) -> Document:
    filename = file.filename.lower() # type: ignore

    # Step 1: Save uploaded file to a temporary path
    suffix = os.path.splitext(filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file.write(await file.read())
        temp_path = temp_file.name

    # Step 2: Use the appropriate loader
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(temp_path)
    elif filename.endswith(".txt"):
        loader = TextLoader(temp_path, encoding="utf-8")
    elif filename.endswith(".docx"):
        loader = Docx2txtLoader(temp_path)
    else:
        raise Exception("Unsupported file type")

    # Step 3: Load document(s)
    documents = loader.load()

    # Step 4: Clean up temp file (optional but recommended)
    os.remove(temp_path)

    # Return the first document (you can return all if needed)
    return documents[0]
