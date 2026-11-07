import uvicorn
from fastapi import FastAPI

from api.routes.chat import router as chat_router

app = FastAPI(title='Delta View API')
app.include_router(chat_router, prefix='/api')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
