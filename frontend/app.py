import streamlit as st
import requests

st.set_page_config(
    page_title="LifePilot AI",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 LifePilot AI")
st.caption("A personal planning & decision-making AI agent")

st.divider()

user_input = st.text_area(
    "Describe your goal or problem",
    placeholder="e.g. I want to balance gym, work, and learning AI without burning out",
    height=120
)

if st.button("Generate Plan", use_container_width=True):
    if not user_input.strip():
        st.warning("Please describe your goal first.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/agent",
                    json={"message": user_input},
                    timeout=60
                )

                if response.status_code != 200:
                    st.error("Agent failed. Please try again.")
                else:
                    data = response.json()

                    st.subheader("Summary")
                    st.write(data["summary"])

                    st.subheader("Steps")
                    for step in data["steps"]:
                        st.write(f"- {step}")

                    st.subheader("Risks")
                    for risk in data["risks"]:
                        st.write(f"- {risk}")

                    st.subheader("Next 24 Hours")
                    for action in data["next_actions_24h"]:
                        st.write(f"- {action}")

            except Exception as e:
                st.error(str(e))
