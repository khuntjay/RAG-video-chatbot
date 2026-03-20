import streamlit as st
import os

# =========================
# SAME IMPORTS AS NOTEBOOK
# =========================
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="YouTube RAG App 🚀", layout="wide")

st.title("🎥 YouTube Transcript Q&A Bot 🤖")
st.markdown("Turn any YouTube video into an AI-powered searchable assistant ✨")


# =========================
# SET OPENAI KEY
# =========================
os.environ["OPENAI_API_KEY"] = "your API key"


# =========================
# SESSION STATE
# =========================
if "main_chain" not in st.session_state:
    st.session_state.main_chain = None


# =========================
# STEP 1 — VIDEO + TRANSCRIPT
# =========================
st.header("🎬 Step 1: Enter Video ID & Generate Transcript")

video_id = st.text_input("🔎 Enter YouTube Video ID")

# 🎥 VIDEO PREVIEW
if video_id:
    st.markdown("### 🎥 Video Preview")
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    st.video(video_url)


if st.button("🚀 Generate Transcript"):

    if not video_id:
        st.warning("⚠️ Please enter a video ID first.")
    else:
        try:
            # Fun Loading Animation
            loading_placeholder = st.empty()

            with loading_placeholder.container():
                st.markdown("### ⏳ Generating Transcript & Building AI Brain...")
                st.image(
                    "https://media.giphy.com/media/L05HgB2h6qICDs5Sms/giphy.gif",
                    width=200
                )

            # =========================
            # ORIGINAL LOGIC (UNCHANGED)
            # =========================
            ytt_api = YouTubeTranscriptApi()
            transcript_list = ytt_api.fetch(video_id)
            transcript = " ".join(chunk.text for chunk in transcript_list)

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.create_documents([transcript])

            embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
            vector_store = FAISS.from_documents(chunks, embeddings)

            retriever = vector_store.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 4}
            )

            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

            prompt = PromptTemplate(
                template="""
                You are a helpful assistant.
                Answer ONLY from the provided transcript context.
                If the context is insufficient, just say you don't know.

                {context}
                Question: {question}
                """,
                input_variables=['context', 'question']
            )

            def format_docs(retrieved_docs):
                context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
                return context_text

            parallel_chain = RunnableParallel({
                'context': retriever | RunnableLambda(format_docs),
                'question': RunnablePassthrough()
            })

            parser = StrOutputParser()

            main_chain = parallel_chain | prompt | llm | parser

            st.session_state.main_chain = main_chain

            # Remove loading GIF
            loading_placeholder.empty()

            st.success("🎉 Transcript Generated & AI Ready!")

        except Exception as e:
            st.error(f"❌ Error: {e}")


# =========================
# STEP 2 — ASK QUESTIONS
# =========================
st.header("💬 Step 2: Ask Questions From the Video")

question = st.text_input("❓ Enter your question")

if st.button("🤖 Get Answer"):

    if st.session_state.main_chain is None:
        st.warning("⚠️ Please generate transcript first.")
    else:
        try:
            answer_loading = st.empty()

            with answer_loading.container():
                st.markdown("### 🤖 AI is thinking...")
                st.image(
                    "https://media.giphy.com/media/3o7TKTDn976rzVgky4/giphy.gif",
                    width=200
                )

            answer = st.session_state.main_chain.invoke(question)

            answer_loading.empty()

            st.markdown("### 📌 Answer:")
            st.success(answer)

        except Exception as e:
            st.error(f"❌ Error: {e}")