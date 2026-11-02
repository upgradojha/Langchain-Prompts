from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

import streamlit as st

load_dotenv()
model = ChatOpenAI(model='gpt-5-nano', reasoning_effort='minimal', max_completion_tokens=700)

template = load_prompt("template.json")

st.header("Research Assistant")

product_name = st.selectbox("Enter product name", ['Laptop', 'Mobile', 'Electronic', 'Keyboard'])
target_audience = st.text_input("Target audience name")
key_features = st.text_input("Key Features")

if st.button('Send'):

    chain = template | model
    result = chain.invoke({
        'product_name': product_name,
        'target_audience': target_audience,
        'key_features': key_features
    })

    st.write(result.content)
