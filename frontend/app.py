import streamlit as st
import requests

BACKEND_URL = "https://lifepilot-ai.onrender.com/agent"

st.set_page_config(
    page_title="LifePilot AI",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 LifePilot AI")
st.subheader("Your personal AI agent for routines & planning")

user_input = st.text_area(
    "What do you want help with?",
    placeholder="Example: Build a consistent routine for gym, work, and learning AI"
)

if st.button("Generate Plan"):
    if not user_input.strip():
        st.warning("Please enter a message")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    BACKEND_URL,
                    json={"message": user_input},
                    timeout=30
                )

                if response.status_code != 200:
                    st.error(f"Backend error: {response.text}")
                else:
                    data = response.json()

                    st.success("Plan generated!")

                    st.markdown("### 📝 Summary")
                    st.write(data.get("summary", ""))

                    st.markdown("### 🔑 Key Assumptions")
                    for item in data.get("key_assumptions", []):
                        st.write("- ", item)

                    st.markdown("### 🧩 Steps")
                    for step in data.get("steps", []):
                        st.write("- ", step)

                    st.markdown("### ⚠️ Risks")
                    for risk in data.get("risks", []):
                        st.write("- ", risk)

                    st.markdown("### 🚀 Next Actions (24h)")
                    for action in data.get("next_actions_24h", []):
                        st.write("- ", action)

            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
