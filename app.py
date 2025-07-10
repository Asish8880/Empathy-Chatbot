import streamlit as st
import joblib
from utils.preprocessing import clean_text
from model.response_logic import generate_response

#load model
model = joblib.load('model/emotion_model.pkl')

#UI
st.set_page_config(page_title="Empathy Chatbot", page_icon="🤖")
st.title("🤖 Empathy Chatbot")
st.write("Talk to a culturally-aware emotional support bot.")

user_input = st.text_area("🗨️ How are you feeling today?", "")

if st.button("Analyze"):
    if user_input.strip():
        clean_input = clean_text(user_input)
        emotion = model.predict([clean_input])[0]
        response = generate_response(emotion, culture="Indian")

        st.subheader("🎯 Detected Emotion:")
        st.success(emotion.capitalize())

        st.subheader("💬 Empathetic Response:")
        st.info(response)
    else:
        st.warning("Please enter a message above.")
