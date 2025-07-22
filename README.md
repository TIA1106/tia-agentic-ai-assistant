# 🤖 Tia's Agentic AI Assistant

A personalized AI chatbot built with **Streamlit**, designed to guide Tia in mastering **DSA**, **Full Stack Development**, and **Data Science**. The assistant adapts based on selected learning mode and gives actionable, focused replies. It also supports chat history persistence.

---

## 🔥 Features

- 🎯 Mode selection: DSA / Full Stack / Data Science
- 💬 Chat interface (Streamlit UI)
- 🧠 Custom system prompt updates based on selected mode
- ✅ Supports OpenAI-compatible free API 
- 🧱 Easily extendable and hackathon-ready

---

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/TIA1106/tia-agentic-ai-assistant.git
cd tia-agentic-ai-assistant
```
2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # OR
   source venv/bin/activate  # Mac/Linux
   ```
3. Install the required packages
  ```bash
pip install -r requirements.txt
```
4. Add your .env file
Create a .env file in the root folder:
```bash
TOGETHER_API_KEY=your_api_key_here
```
🚀 Run the App

```bash
streamlit run app.py
```
📌 Modes Explained:
| Mode             | Role                                                            |
| ---------------- | --------------------------------------------------------------- |
| **DSA**          | Expert in algorithms, problem-solving strategies, and patterns. |
| **Full Stack**   | Mentor for React, Next.js, MongoDB, Express, Tailwind, etc.     |
| **Data Science** | Guide for Python, ML models, Streamlit, and deployment.         |



