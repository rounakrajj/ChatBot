from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
model = ChatMistralAI(model="mistral-small-2506",temperature=0.9)
print("choose your AI mode")
print("1. Funny AI"  )
print("2. Serious AI"  )
print("3. Sad AI"  )
mode=input("Enter the mode number: ")

if mode == "1":
    messages = [
        SystemMessage(content="you are a funny AI agent")
    ]
elif mode == "2":
    messages = [
        SystemMessage(content="you are a serious AI agent")
    ]
elif mode == "3":
    messages = [
        SystemMessage(content="you are a sad AI agent")
    ]
else:
    print("Invalid mode selected.")
    messages = []

1
print("------------------WELCOME TYPE 0 TO EXIT------------------")

while True:
    
    prompt=input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt=="0":
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(prompt)   
    messages.append(AIMessage(content=response.content) )
    print(f"Bot: {response.content}")
print(messages)
