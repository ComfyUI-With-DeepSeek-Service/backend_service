import sys

import uvicorn
from fastapi import FastAPI
from loguru import logger

from app.handlers.comfy_ui import router as comfy_ui
from app.handlers.deepseek import router as deepseek
from settings.config import settings

logger.remove()
logger.add(sys.stderr, level='DEBUG' if settings.DEV else 'INFO')

app = FastAPI(title='Backend service')


app.include_router(comfy_ui)
app.include_router(deepseek)


@app.get("/")
def home():
    return "Hello, World!"


if __name__ == '__main__':
    uvicorn.run(app='main:app', port=8001, host='0.0.0.0', reload=True)
