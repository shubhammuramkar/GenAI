from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

chat_template = ChatPromptTemplate([
            # SystemMessage(content="You are a helpful {domain} expect."),
            # HumanMessage(content="Tell me about {topic} in simple words.")
            ('system', "You are a helpful {domain} expert."),
            ('human', "Tell me about {topic} in simple words.")
])

prompt = chat_template.invoke({
    'domain': "cricket",
    'topic': "batting"
})

print("Prompt:", prompt)