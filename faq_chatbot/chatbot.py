import json
import nltk
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ------------------ NLTK DOWNLOADS ------------------
nltk.download('punkt')
nltk.download('stopwords')


# ------------------ LOAD FAQ DATA ------------------
with open("faqs.json", "r") as file:
    faqs = json.load(file)


# ------------------ TEXT PREPROCESSING ------------------
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)


# ------------------ PREPROCESS FAQ QUESTIONS ------------------
processed_questions = [preprocess(faq["question"]) for faq in faqs]


# ------------------ VECTORIZE QUESTIONS ------------------
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)


# ------------------ MATCH USER QUESTION ------------------
def get_best_answer(user_question):
    processed_user_question = preprocess(user_question)
    user_vector = vectorizer.transform([processed_user_question])

    similarities = cosine_similarity(user_vector, faq_vectors)
    best_match_index = similarities.argmax()
    best_match_score = similarities[0][best_match_index]

    if best_match_score < 0.3:
        return {
            "answer": "Sorry, I couldn't understand your question.",
            "intent": "unknown",
            "confidence": best_match_score
        }

    return {
        "answer": faqs[best_match_index]["answer"],
        "intent": faqs[best_match_index]["intent"],
        "confidence": best_match_score
    }



# ------------------ CHAT LOOP ------------------
def chat():
    print("\n🤖 Internship FAQ Chatbot")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break

        response = get_best_answer(user_input)

        # Smart confidence handling
        if response["confidence"] < 0.3:
            print("Bot:", response["answer"])
            print("Confidence: Low")
        else:
            print("Bot:", response["answer"])
            print("Intent:", response["intent"])
            print(f"Confidence: {response['confidence']:.2f}")




# ------------------ MAIN ------------------
if __name__ == "__main__":
    chat()
