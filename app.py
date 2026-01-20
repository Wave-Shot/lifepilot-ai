import streamlit as st
import requests

st.set_page_config(page_title="LifePilot AI", page_icon="🧭")

st.title("🧭 LifePilot AI")
st.subheader("Your personal AI agent for routines and life planning")

message = st.text_area(
    "Describe your goal or problem",
    placeholder="I want to build a consistent routine for gym, work, and learning AI"
)

if st.button("Run Agent"):
    if not message.strip():
        st.error("Please enter a message")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(
                "https://lifepilot-ai.onrender.com/agent",
                json={"message": message},
                timeout=60
            )

            if response.status_code == 200:
                data = response.json()
                st.success("Agent Response")

                st.markdown("### Summary")
                st.write(data.get("summary", ""))

                st.markdown("### Assumptions")
                for a in data.get("key_assumptions", []):
                    st.write("- " + a)

                st.markdown("### Steps")
                for s in data.get("steps", []):
                    st.write("- " + s)

                st.markdown("### Risks")
                for r in data.get("risks", []):
                    st.write("- " + r)

                st.markdown("### Next Actions (24h)")
                for n in data.get("next_actions_24h", []):
                    st.write("- " + n)
            else:
                st.error("Backend error")
                st.code(response.text)
