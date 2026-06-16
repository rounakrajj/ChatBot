from dotenv import load_dotenv
load_dotenv()

#from langchain.chat_models import init_chat_model
# model=init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")
#response=model.invoke("What is machine?")
#print(response.content) 

from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model="mistral-small-2506",temperature=1.0)
response = model.invoke("who are you?")     
print(response.content)

