import asyncio

from loguru import logger

from app.services.nice_client import NiceApiClient
from packages.common.config import settings
from packages.common.schemas import MarketRequest, MarketResponse, MarketSubData


class MarketService:
    def __init__(self) -> None:
        self._nice_client = NiceApiClient()

    async def send(self, req: MarketRequest) -> MarketResponse:
        await self._nice_client.send_status(req.market, req.sub_data)
        return MarketResponse(status="sent", total=len(req.sub_data))

    async def send_chunked(self, req: MarketRequest) -> None:
        chunks: list[list[MarketSubData]] = [
            req.sub_data[i : i + settings.chunk_size]
            for i in range(0, len(req.sub_data), settings.chunk_size)
        ]
        for idx, chunk in enumerate(chunks):
            await self._nice_client.send_status(req.market, chunk)
            logger.info("청크 {}/{} 전송 완료", idx + 1, len(chunks))
            await asyncio.sleep(settings.chunk_delay_seconds)
