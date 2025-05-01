# Backend service


## Описание


## Технологии

## Требования

## Установка и Запуск

### CMD
`pyenv install 3.12.4` \
`pyenv local 3.12.4` \
`poetry env use python` \
`poetry shell` \
`python main.py`

### Docker

``` commandline
docker build --progress=plain  -t example_project . && \
docker run -it  -p 8000:8000 example_project
```
