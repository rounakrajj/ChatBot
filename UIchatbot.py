import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load env
load_dotenv()

# Model
model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

st.title("🤖 Multi-Mode Chatbot")

# Mode selection
mode = st.selectbox(
    "Choose your AI mode",
    ["Funny AI", "Serious AI", "Sad AI"]
)

# Initialize session state
if "messages" not in st.session_state:
    if mode == "Funny AI":
        st.session_state.messages = [SystemMessage(content="you are a funny AI agent and you have a good sense of humor and you can make jokes and puns")]
    elif mode == "Serious AI":
        st.session_state.messages = [SystemMessage(content="you are a serious AI agent and you provide thoughtful and detailed responses")]
    elif mode == "Sad AI":
        st.session_state.messages = [SystemMessage(content="you are a sad AI agent and you express feelings of sadness and empathy  and you can provide emotional support to users who are feeling down")]

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# Input
prompt = st.chat_input("Type your message (0 to exit)")

if prompt:
    if prompt == "0":
        st.write("Exiting the chatbot. Goodbye!")
    else:
        # Add user message
        st.session_state.messages.append(HumanMessage(content=prompt))
        st.chat_message("user").write(prompt)

        # Get response (same as your logic)
        response = model.invoke(prompt)

        # Store response
        st.session_state.messages.append(AIMessage(content=response.content))
        st.chat_message("assistant").write(response.content) 