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


# How to use RAG App
step 1 when you open the app you will se below screen 
<img width="956" height="473" alt="1" src="https://github.com/user-attachments/assets/185cd5aa-2956-49f1-bba1-c167d1c3c30a" />

step 2 we need to provide a Youtube video ID form the URL 
for example
https://www.youtube.com/watch?v=FQdaUv95mR8&t=75s
in this url Video id is FQdaUv95mR8 So copy and past this id into the box and click genrate now option 
<img width="956" height="440" alt="2" src="https://github.com/user-attachments/assets/92bc8e93-8042-46f6-83a7-ba4f8fddcc97" />


Step 3 we after you can ask the question regading this video and LLM provide answer form this video
<img width="959" height="440" alt="3" src="https://github.com/user-attachments/assets/e2039d75-4c93-4329-b653-791ea3ab969d" />


