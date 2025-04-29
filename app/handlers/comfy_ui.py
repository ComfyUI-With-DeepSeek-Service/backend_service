from fastapi import APIRouter
from loguru import logger

router = APIRouter()


@router.post('/generate_image')
async def create_user(prompt: str) -> str:
    logger.debug(f'Запрос на генерацию картинки по промпту: {prompt}')

    return 'Скоро я буду генерить картинки!'
