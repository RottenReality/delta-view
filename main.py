from dotenv import load_dotenv

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse


from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

import yfinance as yf

from schemas.chat import PromptObject, RequestObject

load_dotenv()

app = FastAPI()

model = ChatOpenAI(
    model='c1/openai/gpt-5/v-20250930',
    base_url = 'https://api-thesys.dev/v1/embed/'
)

checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    checkpointer=checkpointer,
    tools = []
)

@app.post('/api/chat')
async def chat(request: RequestObject):
    pass