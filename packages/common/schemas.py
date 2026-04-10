from pydantic import BaseModel, Field


class MarketSubData(BaseModel):
    tx_id: str = Field(..., description="중복 전송 방지용 트랜잭션 ID")
    payload: dict = Field(default_factory=dict)


class MarketRequest(BaseModel):
    market: str = Field(..., examples=["KRX"])
    sub_data: list[MarketSubData] = Field(default_factory=list)


class MarketResponse(BaseModel):
    status: str
    total: int
    detail: str | None = None
