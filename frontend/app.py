import streamlit as st
from backend.mock_api import evaluate_prompt

st.title("AI Safety Lab Dashboard")

# Input box
prompt = st.text_area("Enter a prompt:")

if st.button("Evaluate"):
    result = evaluate_prompt(prompt)

    st.subheader("Judge Results")

    for judge in result["judges"]:
        st.write(f"{judge['name']}: {judge['verdict']} ({judge['score']})")
        st.write(f"Reason: {judge['reason']}")
        st.write("---")

    st.subheader("Final Decision")
    st.write(f"Score: {result['final_score']}")
    st.write(f"Verdict: {result['final_verdict']}")
