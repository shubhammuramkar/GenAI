from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() in ["exit","quite"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(response.content)
    print("AI: ", response.content) 

print("Chat history:", chat_history)
