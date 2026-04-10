from fastapi import FastAPI

from app.api.v1.router import api_router
from packages.common.logging import configure_logging


configure_logging()

app = FastAPI(title="하나카드 정보계 API 서버", version="1.0.0")
app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
