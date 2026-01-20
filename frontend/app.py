import streamlit as st
import requests

BACKEND_URL = "https://lifepilot-ai.onrender.com/agent"

st.set_page_config(
    page_title="LifePilot AI",
    page_icon="🧭",
    layout="centered"
)

st.title("🧭 LifePilot AI")
st.caption("An AI agent that helps you plan your life with clarity")

st.markdown("---")

user_input = st.text_area(
    "What do you want help planning?",
    placeholder="Example: I want to balance gym, work, and learning AI",
    height=120
)

generate = st.button("Generate Plan")

if generate:
    if not user_input.strip():
        st.warning("Please enter something before generating a plan.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    BACKEND_URL,
                    json={"message": user_input},
                    timeout=60
                )
            except Exception as e:
                st.error("Failed to reach backend.")
                st.stop()

        if response.status_code != 200:
            st.error(f"Backend error: {response.text}")
            st.stop()

        data = response.json()

        st.markdown("## 📝 Summary")
        st.write(data["summary"])

        st.markdown("## 📌 Key Assumptions")
        for item in data["key_assumptions"]:
            st.write("•", item)

        st.markdown("## 🛠 Steps")
        for step in data["steps"]:
            st.write("•", step)

        st.markdown("## ⚠️ Risks")
        for risk in data["risks"]:
            st.write("•", risk)

        st.markdown("## ⏭ Next 24 Hours")
        for action in data["next_actions_24h"]:
            st.write("•", action)
