import streamlit as st
from model import predict_disease

st.set_page_config(page_title="AI Symptom Checker", page_icon="🩺")

st.title("🩺 AI Symptom Checker")
st.write("Enter your symptoms below and get a predicted condition with treatment suggestions.")

user_input = st.text_area("📝 Describe your symptoms", height=150)

if st.button("🔍 Check Now"):
    if user_input.strip() == "":
        st.warning("Please enter your symptoms.")
    else:
        with st.spinner("Analyzing symptoms..."):
            disease, action, prescription = predict_disease(user_input)

        st.success(f"**Predicted Disease:** {disease}")
        st.info(f"**Immediate Action:** {action}")
        st.code(prescription, language='markdown')