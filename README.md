# 하나카드 정보계 API 서버

주신 아키텍처 초안 기준의 FastAPI 최소 실행 골격입니다.

## 실행

```bash
cd nice_api_server
python -m venv .venv
# Git Bash
source .venv/Scripts/activate
# PowerShell
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.dev.example .env.dev
uvicorn app.main:app --reload --port 8000
```

## 확인

- Health: `http://localhost:8000/health`
- Swagger: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 샘플 요청

`POST /api/v1/market/status`

```json
{
  "market": "KRX",
  "sub_data": [
    {"tx_id": "t1", "payload": {"code": "005930"}},
    {"tx_id": "t2", "payload": {"code": "000660"}}
  ]
}
```
