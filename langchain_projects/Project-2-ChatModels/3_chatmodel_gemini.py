from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',

)
result = chat_model.invoke("what is the capital of India")
print(result.content)