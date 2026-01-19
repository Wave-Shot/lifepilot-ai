import streamlit as st
import requests

API_URL = "https://lifepilot-ai.onrender.com/agent"

st.set_page_config(
    page_title="LifePilot AI",
    page_icon="🧭",
    layout="centered"
)

st.title("🧭 LifePilot AI")
st.subheader("Turn goals into clear, actionable plans")

user_input = st.text_area(
    "What do you want help planning?",
    placeholder="e.g. Build a consistent routine for gym, work, and learning AI",
    height=120
)

if st.button("Generate Plan"):
    if not user_input.strip():
        st.warning("Please enter a goal or problem.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(
                API_URL,
                json={"message": user_input},
                timeout=60
            )

        if response.status_code != 200:
            st.error(f"Error {response.status_code}: {response.text}")
        else:
            data = response.json()

            st.success("Plan generated")

            st.markdown("### Summary")
            st.write(data["summary"])

            st.markdown("### Key Assumptions")
            for item in data["key_assumptions"]:
                st.write("•", item)

            st.markdown("### Steps")
            for step in data["steps"]:
                st.write("•", step)

            st.markdown("### Risks")
            for risk in data["risks"]:
                st.write("•", risk)

            st.markdown("### Next Actions (24h)")
            for action in data["next_actions_24h"]:
                st.write("•", action)
