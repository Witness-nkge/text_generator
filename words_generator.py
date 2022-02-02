from transformers import pipeline
import streamlit as st

st.title('Text Generator')
text = st.text_input('input text')
max = st.number_input('maximum length')

if st.button('generate'):
    text_generator = pipeline("text-generation")
    st.write(text_generator(text, max_length=int(max), do_sample=False))
