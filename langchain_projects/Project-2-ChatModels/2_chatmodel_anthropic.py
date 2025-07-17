from langchain import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatAnthropic(
    model='claude-sonnet-4-20250514',
    temperature=0.2,
    max_completion_tokens=10
)

result = chat_model.invoke("what is the capital of India")
print(result.content)