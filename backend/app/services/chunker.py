from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(documents: list):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(documents)
