# Delta View

A chat assistant for stock research. You ask about a company in plain language, and an LLM agent calls market-data tools to answer, with replies shown as generated UI such as tables and cards, not plain text.

## What it does

The agent can:

- get the latest price for a ticker
- get historical prices for a date range
- pull a company's balance sheet
- fetch recent news for a ticker

Example questions:

- "How has NVDA moved over the last three months?"
- "Compare the balance sheets of AAPL and MSFT."
- "Any recent news on TSLA?"

Each chat runs in its own thread, so the agent remembers earlier messages in the same chat.

## How it works

```
React (C1Chat)  ──POST /api/chat──▶  FastAPI  ──▶  LangChain agent  ──▶  yfinance tools
       ▲                                                   │
       └────────────── streamed response ◀─────────────────┘
```

- **Backend:** FastAPI runs a LangChain agent (`create_agent`) with four tools built on `yfinance`. Chat memory per thread comes from LangGraph's `InMemorySaver`. The response streams back token by token.
- **Model:** called through the Thesys C1 API, which is OpenAI-compatible. C1 returns UI components as well as text.
- **Frontend:** React and Vite, using the Thesys GenUI SDK's `C1Chat` to render those components. In development, Vite forwards `/api` requests to the backend.

## Tech stack

| Layer    | Tools                                         |
| -------- | --------------------------------------------- |
| Backend  | Python 3.12, FastAPI, LangChain, LangGraph, Pydantic, uv |
| Data     | yfinance                                      |
| LLM      | Thesys C1 (OpenAI-compatible API)             |
| Frontend | React 19, TypeScript, Vite, Thesys GenUI SDK  |

## Project structure

```
backend/
  main.py               FastAPI app
  api/routes/chat.py    /api/chat streaming endpoint
  agents/stock_agent.py agent, model and memory setup
  tools/market_data.py  yfinance tools exposed to the agent
  schemas/chat.py       request models
frontend/
  src/App.tsx           chat UI
  vite.config.ts        dev server and API proxy
```

## Running locally

**Requirements:** Python 3.12+, [uv](https://docs.astral.sh/uv/), Node.js 20+, and a [Thesys](https://console.thesys.dev) API key.

1. Copy `.env.example` to `.env` in the project root and add your key:

   ```bash
   cp .env.example .env
   ```

2. Start the backend (runs on port 8000):

   ```bash
   cd backend
   uv sync
   uv run python -m uvicorn main:app --reload
   ```

3. Start the frontend (runs on port 3000):

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. Open <http://localhost:3000>.

## Notes

- Chat history is kept in memory, so it is lost when the backend restarts.
- Market data comes from Yahoo Finance via `yfinance`. It is meant for personal use and may be delayed.
- This is a demo project, not financial advice.
