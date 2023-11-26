# Реализовать FastAPI приложение в докере со всеми видами запросов:
# get, retrieve (это вытянуть не все объекты, а 1 по id), update (put, patch), post, delete.


from fastapi import FastAPI

from src.rest.api.router import router as api_router

app = FastAPI(
    title="My first app",
)

app.include_router(api_router)

# Base.metadata.create_all(engine)
