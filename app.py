import streamlit as st
from agent import ask_agentic_ai
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Agentic AI", page_icon="🤖")
st.title("🤖 Tia's Agentic AI Assistant")

mode = st.selectbox("🎯 Select Mode", ["Full Stack", "DSA", "Data Science"])

mode_prompts = {
    "DSA": "You're a pro DSA coach helping Tia master patterns and problem solving.",
    "Full Stack": "You're a mentor guiding Tia in React, Next.js, MongoDB, Express, Tailwind, etc.",
    "Data Science": "You're a data science coach helping with ML, Python, Streamlit, and model deployment."
}
new_system_prompt = mode_prompts[mode]

import json

CHAT_FILE = "chat_memory.json"

def load_chat():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [{"role": "system", "content": new_system_prompt}]

def save_chat(messages):
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2)

if "messages" not in st.session_state:
    st.session_state.messages = load_chat()

st.session_state.messages[0]["content"] = new_system_prompt

components.html("""
<script>
  const streamlitInput = window.parent.document.querySelector('input[type=text]');
  const button = document.createElement("button");
  button.innerHTML = "🎤";
  button.style.marginLeft = "10px";
  button.onclick = () => {
    const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      streamlitInput.value = transcript;
      streamlitInput.dispatchEvent(new Event("input", { bubbles: true }));
    };
    recognition.start();
  };
  streamlitInput.parentNode.appendChild(button);
</script>
""", height=0)

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

user_prompt = st.chat_input("Ask your agent anything...")

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    st.chat_message("user").write(user_prompt)

    with st.spinner("Thinking..."):
        reply = ask_agentic_ai(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)
        save_chat(st.session_state.messages)


        with open("agentic_chat_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[MODE: {mode}]\n")
            f.write(f"User: {user_prompt}\n")
            f.write(f"Assistant: {reply}\n\n")
