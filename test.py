from langchain.llms import OpenAI
from dotenv import dotenv_values
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

open_api_key = dotenv_values(".env")["OPENAI_API_KEY"]

llm = OpenAI(temperature=0.9, openai_api_key=open_api_key)

llm.predict("What would be a good company name for a company that makes colorful socks?")

chat = ChatOpenAI(temperature=0)
chat.predict_messages([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
# >> AIMessage(content="J'aime programmer.", additional_kwargs={})
