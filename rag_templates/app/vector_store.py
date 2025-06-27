from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def get_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vectorstore = FAISS.load_local("app/sample_data/vectorstore", embeddings)
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})