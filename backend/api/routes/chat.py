from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from langchain.messages import HumanMessage, SystemMessage

from agents.stock_agent import agent
from schemas.chat import RequestObject

router = APIRouter()

SYSTEM_PROMPT = (
    'You are a stock analysis assistant. You have the ability to get real-time '
    'stock prices, historical stock prices (given a date range), news, and '
    'balance sheet data for a given ticker symbol.'
)


@router.post('/chat')
async def chat(request: RequestObject):
    config = {'configurable': {'thread_id': request.threadId}}

    def generate():
        for token, _ in agent.stream(
            {
                'messages': [
                    SystemMessage(SYSTEM_PROMPT),
                    HumanMessage(request.prompt.content),
                ]
            },
            stream_mode='messages',
            config=config,
        ):
            yield token.content

    return StreamingResponse(
        generate(),
        media_type='text/event-stream',
        headers={
            'Cache-Control': 'no-cache, no-transform',
            'Connection': 'keep-alive',
        },
    )
