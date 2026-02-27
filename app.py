import streamlit as st
import pickle
from chatbot import generate_response

with open('model/sentiment_model.pkl', 'rb') as f:
    model, vectorizer = pickle.load(f)

st.set_page_config(page_title='Mental Health Companion Chatbot')
st.title('Mental Health Companion Chatbot')

user_input = st.text_area('How are you feeling today?')

if st.button('Analyze'):
    if user_input.strip() == '':
        st.warning('Please enter some text')
    else:
        vec = vectorizer.transform([user_input])
        sentiment = model.predict(vec)[0]
        response = generate_response(sentiment)
        st.write(f'Detected mood: {sentiment}')
        st.success(response)
