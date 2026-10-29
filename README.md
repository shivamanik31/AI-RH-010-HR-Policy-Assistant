# AI HR Policy Assistant — AI-RH-010

**Student Code:** DAS011046  
**Task:** AI-RH-010 — AI HR Policy Assistant  
**Task brief:** [AI HR Policy Assistant internship task](https://www.freeinternships.in/)

## Overview
A Python and Streamlit conversational chatbot that searches a structured JSON knowledge base to answer common HR-policy questions. It demonstrates text preprocessing, keyword-based intent recognition, TF-IDF retrieval, cosine similarity, and fallback responses.

## Features
- Chat interface with sample question buttons
- JSON knowledge base for leave, working hours, code of conduct, benefits, grievances, and performance reviews
- Text normalization / preprocessing
- Pattern-based intent detection
- TF-IDF policy retrieval and cosine similarity ranking
- Fallback response for unmatched queries
- Expandable panel showing matched policy and retrieval score

## Technology
Python, Streamlit, JSON, scikit-learn, regular expressions, Git/GitHub.

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```
Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Project structure
```text
AI-RH-010-HR-Policy-Assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── hr_policies.json
└── screenshots/
```

## Testing checklist
- Greeting: `Hello`
- Leave: `How many casual leaves are available?`
- Working hours: `What are the standard working hours?`
- Benefits: `Tell me about health insurance and PF`
- Grievance: `How do I file a grievance?`
- Unknown: `What is the cafeteria menu?`

## Limitations and responsible use
The policy content is sample data based on the internship task brief; it is not verified policy for a real employer. Intent recognition is rule-based, and fallback retrieval uses TF-IDF/cosine similarity rather than a trained language model. Confirm real employment decisions and current rules with HR.

## Submission links
- GitHub repository: add your repository URL here.
- YouTube demo: add your video URL here.
- Task ID: AI-RH-010
- Student code: DAS011046
