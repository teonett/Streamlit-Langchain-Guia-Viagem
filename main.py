from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
API_KEY = 'digita_aqui_sua_api_key'

llm = OpenAI(openai_api_key=API_KEY, temperature=0.1)

prompt_template = PromptTemplate(
    input_variables=["reteiros"],
    template="Quero que você atue como um guia de viagem. Eu vou escrever minha localização para você e você irá sugerir um lugar para visitar perto da minha localização: {reteiros}",
)

meal_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    output_key="Destinos",  # the output from this chain will be called 'meals'
    verbose=True
)

st.title("Planejando uma Viagem")
user_prompt = st.text_input(
    "De o nome do lacal de onde mora e qual tipo de lugares queira visitar, por exemplo 'Ex.: Estou em São Paulo e quero visitar apenas museus'")

if st.button("Generate") and user_prompt:
    with st.spinner("Generating..."):
        output = meal_chain({'reteiros': user_prompt})
        st.write(output)
