from fastapi import APIRouter, BackgroundTasks, Depends

from app.services.market_service import MarketService
from packages.common.config import settings
from packages.common.schemas import MarketRequest, MarketResponse

router = APIRouter(prefix="/market", tags=["market"])


@router.post("/status", response_model=MarketResponse)
async def register_market_status(
    req: MarketRequest,
    background_tasks: BackgroundTasks,
    service: MarketService = Depends(MarketService),
) -> MarketResponse:
    if len(req.sub_data) > settings.chunk_size:
        background_tasks.add_task(service.send_chunked, req)
        return MarketResponse(
            status="queued",
            total=len(req.sub_data),
            detail=f"chunked by {settings.chunk_size}",
        )
    return await service.send(req)
