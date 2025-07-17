from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(
    model='gpt-4',
    temperature=2,
    max_completion_tokens=10     
)
result = chat_model.invoke("what is the capital of India")
print(result.content)