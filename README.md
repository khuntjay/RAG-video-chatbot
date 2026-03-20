# RAG-video-chatbot
# 🎥 YouTube RAG Q&A App 🤖

Turn any YouTube video into an AI-powered question-answering system using Retrieval-Augmented Generation (RAG).

This app allows users to:
1. Input a YouTube video ID
2. Automatically generate the transcript
3. Store transcript chunks in a vector database
4. Ask questions about the video
5. Get accurate answers grounded in the video content

---

## 🚀 Features

- 🔍 Extracts transcript from YouTube videos
- ✂️ Splits transcript into semantic chunks
- 🧠 Creates embeddings using OpenAI
- 📦 Stores data in a FAISS vector database
- 🔎 Performs similarity search
- 🤖 Uses LLM to answer questions from context only
- 🎨 Interactive UI built with Streamlit

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit
- **LLM:** OpenAI (GPT-4o-mini)
- **Embeddings:** OpenAI Embeddings
- **Vector DB:** FAISS
- **Framework:** LangChain
- **Data Source:** YouTube Transcript API

---


---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/your-username/youtube-rag-app.git
cd youtube-rag-app

## 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

## 3. install dependencies
pip install -r requirements.txt


## 4. Setup API Key
export OPENAI_API_KEY="your_api_key_here"
in the code past your OPENAI_API_KEY 


## 5. Run API Key
streamlit run Rag.py


