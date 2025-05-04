import asyncio
import json

import redis.asyncio as redis
from fastapi import APIRouter
from loguru import logger
from pydantic import BaseModel

router = APIRouter()


class MakeTextRequest(BaseModel):
    chat_id: int = None
    message_id: int = None
    prompt: str = None


@router.post('/make_text_request')
async def make_text_request(request_body: MakeTextRequest) -> None:
    logger.info(f'Запрос на обработку текста по промпту: {request_body.prompt}')

    r = redis.Redis(host='localhost', port=6379, db=0, password='your_strong_password')

    # TODO move to worker: resp = await generate_with_cleanup(prompt=prompt)
    # TODO put message to to_send_message queue

    # Имя очереди
    queue_name = 'to_send_message'  # TODO define in motherbase, get from env

    # Проверка существования очереди (не обязательно, но если нужно)
    exists = await r.exists(queue_name)
    if not exists:
        logger.warning(f"Очередь '{queue_name}' не существует, создаём новую")

    # Добавление сообщения в очередь
    message = request_body.prompt or "445wyueytirtiolgyho;!"
    key = json.dumps({'chat_id': request_body.chat_id, 'message_id': request_body.message_id})

    await r.hset('to_send_message', key=key, value=message)
    logger.info(f"Сообщение добавлено в очередь '{queue_name}': {message}")

    # Закрытие соединения
    await r.aclose()

    # return resp

# asyncio.run(make_text_request())


# ================== bottom



# OLLAMA_URL = "http://ollama:11434"


# async def generate_with_cleanup(prompt: str):
#     # Создаем сессию с таймаутами
#     async with (aiohttp.ClientSession() as session):  # TODO rewrite with https://github.com/ollama/ollama-python
#
#         # Отправляем запрос
#         async with session.post(
#             f"{OLLAMA_URL}/api/generate",
#             json={"model": "deepseek-r1:1.5b", "prompt": prompt, "stream": False},
#         ) as response:
#             response.raise_for_status()
#             response_json = await response.json()
#             logger.info(response)
#             return response_json.get('response')