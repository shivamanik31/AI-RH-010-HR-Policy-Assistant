# Project Report: AI HR Policy Assistant
**Task ID:** AI-RH-010  
**Student Code:** DAS011046

## 1. Objective
The objective is to build a conversational assistant that helps users locate information in an HR policy knowledge base using Python and basic NLP techniques.

## 2. Implementation
The application is built with Streamlit. HR policy entries are stored in `data/hr_policies.json`, organized by category, title, keywords, and content. Text preprocessing lowercases input, removes punctuation, and normalizes whitespace. A rule-based intent detector recognizes common topics. For other queries, scikit-learn's TF-IDF vectorizer represents policy documents and cosine similarity ranks likely matches. A fallback message is shown when similarity is too low.

## 3. Features
The chatbot covers leave policy, working hours, code of conduct, benefits and compensation, grievance redressal, and performance reviews. It includes sample questions, chat history, a retrieval explanation panel, and fallback handling.

## 4. Testing
Tested query categories should include greetings, leave, working hours, benefits, grievances, performance reviews, and an unrelated query to verify fallback behavior. Record screenshots of the running app and these different responses before submission.

## 5. Tools and Technologies
Python, Streamlit, JSON, scikit-learn, regular expressions, VS Code, and Git/GitHub.

## 6. Limitations and Future Work
This is a demonstration using sample policy content, not an official employer policy source. Intent detection uses predefined patterns; TF-IDF retrieval is not a generative AI model. Future improvements could include document upload, multilingual support, feedback collection, authentication, analytics, and an admin interface.

## 7. Conclusion
The project demonstrates a basic HR policy chatbot with a structured knowledge base, intent recognition, information retrieval, and fallback responses. Users should verify important employment information with the appropriate HR team.
