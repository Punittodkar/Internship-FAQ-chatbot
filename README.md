# 🤖 Internship FAQ Chatbot

An AI-powered FAQ chatbot designed to answer internship-related queries. This project uses Natural Language Processing (NLP) techniques to understand user questions and provide relevant answers.

## 🚀 Features

- **Intent Detection:** Uses TF-IDF and Cosine Similarity to match user queries with the best available FAQ.
- **Confidence Scoring:** Displays match confidence to indicate how relevant the answer is.
- **User-Friendly UI:** Built with [Streamlit](https://streamlit.io/) for an interactive experience.
- **Customizable Knowledge Base:** FAQs are stored in a simple `faqs.json` file, making it easy to update.

## 🛠️ Tech Stack

- **Python** (Core Language)
- **NLTK** (Natural Language Toolkit for text preprocessing)
- **Scikit-learn** (TF-IDF Vectorization & Cosine Similarity)
- **Streamlit** (Web Interface)

## 📂 Project Structure

```
faq_chatbot/
│
├── app.py              # Main Streamlit application
├── chatbot.py          # Chatbot logic (NLP & matching)
├── faqs.json           # Knowledge base (JSON format)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd faq_chatbot
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data:**
   The application will automatically download the necessary NLTK data (`punkt`, `stopwords`) on the first run.

## ▶️ Usage

### Run the Web App (Streamlit)
To launch the interactive web interface:
```bash
streamlit run app.py
```

### Run the CLI Chatbot
To test the chatbot in the terminal:
```bash
python chatbot.py
```

## 🧩 How It Works

1. **Preprocessing:** User input is cleaned (lowercased, punctuation removed, stop words removed) using NLTK.
2. **Vectorization:** The input is converted into a numerical vector using TF-IDF (Term Frequency-Inverse Document Frequency).
3. **Similarity Matching:** The system calculates the Cosine Similarity between the user's input vector and the pre-defined FAQ vectors.
4. **Response:** The FAQ with the highest similarity score is returned. If the confidence score is below a threshold (0.3), a fallback message is shown.

## 📝 Customizing the Knowledge Base

To add more questions and answers, simply edit the `faqs.json` file:

```json
[
  {
    "intent": "new_topic",
    "question": "Your new question here?",
    "answer": "Your answer here."
  }
]
```

## 📄 License

This project is open-source and available for educational purposes.
