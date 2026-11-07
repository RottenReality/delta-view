from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

from tools.market_data import market_data_tools

load_dotenv()

model = ChatOpenAI(
    model='c1/openai/gpt-5/v-20250930',
    base_url='https://api.thesys.dev/v1/embed/',
)

checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    checkpointer=checkpointer,
    tools=market_data_tools,
)