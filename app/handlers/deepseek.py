from fastapi import APIRouter
from loguru import logger
import aiohttp
import asyncio

router = APIRouter()

OLLAMA_URL = "http://ollama:11434"


async def generate_with_cleanup(prompt: str):
    # Создаем сессию с таймаутами
    async with (aiohttp.ClientSession() as session):  # TODO rewrite with https://github.com/ollama/ollama-python

        # Отправляем запрос
        async with session.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": "deepseek-r1:1.5b", "prompt": prompt, "stream": False},
        ) as response:
            response.raise_for_status()
            response_json = await response.json()
            logger.info(response)
            return response_json.get('response')


@router.post('/make_text_request')
async def create_user(prompt: str) -> str:
    logger.info(f'Запрос на обработку текста по промпту: {prompt}')

    resp = await generate_with_cleanup(prompt=prompt)

    return resp
