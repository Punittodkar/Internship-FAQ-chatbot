import streamlit as st
from chatbot import get_best_answer

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Internship FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ------------------ SIDEBAR ------------------
st.sidebar.title("📌 Project Info")
st.sidebar.markdown("""
**Project:** AI-Powered FAQ Chatbot  
**Domain:** NLP / AI  
**Tech Stack:**  
- Python  
- NLTK  
- TF-IDF  
- Cosine Similarity  
- Streamlit  

This chatbot answers internship-related FAQs using NLP.
""")

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Built for AI Internship")

# ------------------ MAIN UI ------------------
st.title("🤖 Internship FAQ Chatbot")
st.caption("Ask questions related to the internship program")

# Input box
user_input = st.text_input(
    "Type your question below 👇",
    placeholder="e.g. How can I apply for the internship?"
)

# ------------------ RESPONSE SECTION ------------------
if user_input:
    response = get_best_answer(user_input)

    st.markdown("---")

    if response["confidence"] < 0.3:
        st.error("❌ " + response["answer"])
        st.markdown("**Confidence:** Low")
    else:
        st.success("✅ " + response["answer"])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Intent:** `{response['intent']}`")
        with col2:
            st.markdown(f"**Confidence:** `{response['confidence']:.2f}`")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("💡 This is an NLP-based chatbot using intent detection and confidence scoring.")
