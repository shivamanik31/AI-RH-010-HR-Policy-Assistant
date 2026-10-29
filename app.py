import json
import re
from pathlib import Path

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).parent
POLICY_FILE = ROOT / "data" / "hr_policies.json"

@st.cache_data
def load_policies():
    with POLICY_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def preprocess_text(text):
    """Normalize text for basic NLP matching."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def detect_intent(text):
    """Identify common HR query categories using transparent keyword patterns."""
    query = preprocess_text(text)
    patterns = {
        "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
        "leave_policy": ["leave", "vacation", "holiday", "time off", "sick"],
        "working_hours": ["working hours", "office time", "shift", "overtime", "work from home", "flexible"],
        "code_of_conduct": ["conduct", "ethics", "behavior", "dress code", "harassment", "confidentiality"],
        "benefits": ["benefits", "insurance", "salary", "provident fund", "pf", "gratuity"],
        "grievance": ["grievance", "complaint", "report an issue", "problem", "whistleblower"],
        "performance": ["performance", "appraisal", "review", "rating", "promotion"],
        "help": ["help", "what can you do", "support"]
    }
    for intent, keywords in patterns.items():
        if any(keyword in query for keyword in keywords):
            return intent
    return "unknown"

def build_search_index(policies):
    texts = []
    keys = []
    for key, policy in policies.items():
        texts.append(" ".join([policy["title"], *policy["keywords"], policy["content"]]))
        keys.append(key)
    vectorizer = TfidfVectorizer(preprocessor=preprocess_text, stop_words="english")
    matrix = vectorizer.fit_transform(texts)
    return vectorizer, matrix, keys

def answer_query(query, policies, vectorizer, matrix, keys):
    intent = detect_intent(query)
    if intent == "greeting":
        return ("Hello! Welcome to the AI HR Policy Assistant. Ask me about leave, working hours, "
                "code of conduct, benefits, grievances, or performance reviews."), "Greeting", 1.0
    if intent == "help":
        return ("I can help with these topics: Leave Policy, Working Hours, Code of Conduct, "
                "Benefits & Compensation, Grievance Redressal, and Performance Reviews."), "Help", 1.0

    if intent in policies:
        key = intent
        score = 1.0
    else:
        query_vector = vectorizer.transform([query])
        scores = cosine_similarity(query_vector, matrix)[0]
        best = int(scores.argmax())
        score = float(scores[best])
        key = keys[best] if score >= 0.08 else None

    if key is None:
        return ("I couldn't find a reliable match in this sample knowledge base. Try asking about "
                "leave, working hours, benefits, conduct, grievances, or performance reviews. "
                "Please confirm important details with your actual HR team."), "No match", score

    policy = policies[key]
    response = f"**{policy['title']}**\n\n{policy['content']}\n\n*Note: These are sample policies for this demo, not verified rules for a real employer.*"
    return response, policy["title"], score

st.set_page_config(page_title="AI HR Policy Assistant", page_icon="📋", layout="wide")
st.title("📋 AI HR Policy Assistant")
st.caption("A demo conversational chatbot for searching a structured HR policy knowledge base.")

policies = load_policies()
vectorizer, policy_matrix, policy_keys = build_search_index(policies)

with st.sidebar:
    st.header("Policy topics")
    st.write("Choose a sample question or type your own.")
    examples = [
        "How many casual leaves are available?",
        "What are the standard working hours?",
        "Tell me about health insurance and PF.",
        "How do I file a grievance?",
        "What is the dress code?",
        "When are performance reviews held?"
    ]
    for example in examples:
        if st.button(example, use_container_width=True):
            st.session_state["suggested_question"] = example
    st.divider()
    st.info("Demo only: check official company policy or HR for authoritative answers.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I can help you find information in the sample HR policy knowledge base. What would you like to know?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

suggested = st.session_state.pop("suggested_question", None)
prompt = st.chat_input("Ask an HR policy question...")
if suggested:
    prompt = suggested

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    response, matched_policy, score = answer_query(prompt, policies, vectorizer, policy_matrix, policy_keys)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
        with st.expander("How this query was handled"):
            st.write(f"Detected intent / matched policy: {matched_policy}")
            st.write(f"Retrieval score: {score:.3f}")
            st.write("Intent patterns are checked first; otherwise TF-IDF and cosine similarity rank policy text.")
