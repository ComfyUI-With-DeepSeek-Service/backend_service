from fastapi import APIRouter
from loguru import logger

router = APIRouter()


@router.post('/make_text_request')
async def create_user(prompt: str) -> str:
    logger.debug(f'Запрос на обработку текста по промпту: {prompt}')

    return 'Скоро я буду отвечать на вопросы!'
