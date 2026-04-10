from packages.common.schemas import MarketSubData


class NiceApiClient:
    async def send_status(self, market: str, items: list[MarketSubData]) -> dict:
        # TODO: 실제 하나카드 정보계 연동 시 httpx.AsyncClient 호출로 교체
        return {
            "status": "sent",
            "market": market,
            "count": len(items),
        }
