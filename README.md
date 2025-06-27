

---

````markdown
# 📚 RAG Builder — Document & Web-Based Chatbot Platform

**RAG Builder** is a full-stack application that enables users to create custom chatbots powered by their own documents or scraped website content using **Retrieval-Augmented Generation (RAG)**.

🚀 Built with:
- ⚙️ **FastAPI** (backend)
- 🎨 **HTML/CSS/JS/jQuery** (frontend)
- 🧠 **LangChain** + **FAISS** + **HuggingFace Embeddings**
- 🤖 **ChatGroq** for LLM-powered responses

---

## ✨ Features

- 📄 Upload `.pdf`, `.txt`, or `.docx` files to build document-based RAG chatbots.
- 🌐 Scrape websites (with depth control) and chat with their content.
- 💬 Chat interface powered by your uploaded data.
- 🧠 Embeddings stored in FAISS vectorstores per session.
- 🗂 Project management via localStorage.
- 🗑️ Delete and manage projects easily.

---

## 🔧 Installation

### 1. Clone this repo

```bash
git clone https://github.com/Moulik-23/rag-builder.git
cd rag-builder
````

### 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Create a `.env` file in `/backend`:

```env
GROQ_API_KEY=your_groq_api_key
EMBEDDING_MODEL_NAME=sentence-transformers/all-mpnet-base-v2
LLM_MODEL_NAME=meta-llama/llama-4-scout-17b-16e-instruct
VECTORSTORE_PATH=app/vectorstores
```

### 3. Frontend Setup

Simply open `frontend/index.html` in your browser (or run a local server like Live Server or VSCode’s Go Live).

Make sure backend is running at `http://localhost:8000`.

---

## 🧪 API Endpoints

| Endpoint           | Method | Description                              |
| ------------------ | ------ | ---------------------------------------- |
| `/api/upload-docs` | POST   | Upload a document and create vectorstore |
| `/api/scrape`      | POST   | Scrape website content and build RAG     |
| `/api/chat`        | POST   | Ask questions to the RAG bot             |

---

## 📁 Project Structure

```
rag-builder/
├── backend/
│   ├── app/
│   │   ├── routers/         # FastAPI routers (upload, scrape, chat)
│   │   ├── services/        # Embedding & scraping logic
│   │   ├── utils/           # File handling utilities
│   │   ├── main.py
│   │   ├── config.py
│   │   └── vectorstores/    # Stored FAISS DBs per session
├── frontend/
│   ├── index.html
│   ├── dashboard.css
│   ├── chat.html
│   ├── scrape_script.js
│   ├── upload_script.js
│   └── chat.js
|   
├── rag_templates/
|    ├──app/
|    |  ├──config.py
|    |  ├──main.py
|    |  ├──rag_chain.py
|    |  └──vector_store.py
```

---

## 📸 Screenshots

| Dashboard                              
| --------------------------------------- | ----------------------------- |
| ![Screenshot 2025-06-27 233007](https://github.com/user-attachments/assets/66d057ed-ba33-415d-9fdb-11ebedaaea3c)

| Chat Interface                |
| ![Screenshot 2025-06-27 235551](https://github.com/user-attachments/assets/669c0d40-db50-433c-ad72-af4757d177b0)


---

## 💡 To-Do / Ideas

* Add support for multiple files per project
* User authentication & session syncing
* Store project metadata in a database instead of localStorage
* Add support for summarization

---

## 📃 License

This project is licensed under the MIT License.

---

## 🧠 Credits

* [LangChain](w)
* [FAISS](w)
* [BeautifulSoup](w)
* [HuggingFace Sentence Transformers](w)
* [FastAPI](w)
* [Groq](https://groq.com/)

```

---

🚀 Deploying Soon... Stay Tuned!
```
