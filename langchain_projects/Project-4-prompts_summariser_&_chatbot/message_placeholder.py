from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

# chat_template
chat_template = ChatPromptTemplate([
    ('system', "you are helpful customer support agent."),  
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', "{query}"),  #I want to request a refund for my order
    
])

chat_history = []

# load chat history
with open("chatbot_history.txt", "r") as file:
    chat_history.extend(file.readlines())
print("Chat history loaded:", chat_history)

# create a prompt
prompt = chat_template.invoke({ 'chat_history': chat_history ,
                                      'query': 'where is my refund ?'})

print("Prompt:", prompt)