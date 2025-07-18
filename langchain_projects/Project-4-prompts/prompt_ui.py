from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt, PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

st.header("Research Paper Summarizer")

paper_input = st.selectbox("select research papaer ", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis", "word2vec: Efficient Estimation of Word Representations in Vector Space"])

style_input = st.selectbox('select Explanation style', ["Beginner-Friendly", "Technical", "Code_Oriented","Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])


# dynamic template loading
template = load_prompt('template.json')

# prompt = template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input}
# )

if st.button("summarize"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write("Summary:")
    st.write(result.content)

