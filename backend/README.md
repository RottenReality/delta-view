# Delta View: Backend

FastAPI service that runs a LangChain stock-analysis agent and streams its responses to the frontend.

See the [root README](../README.md) for the full project overview and setup.

## Development

From this folder, install dependencies and start the API:

```bash
uv sync
uv run python -m uvicorn main:app --reload
```

The API runs on <http://localhost:8000> and exposes `POST /api/chat`. It reads `OPENAI_API_KEY` from the `.env` file in the project root (see `.env.example`).

Running uvicorn as a module skips the `uvicorn.exe` wrapper, which can fail on Windows with `uv trampoline failed to canonicalize script path`.
