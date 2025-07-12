from fastapi import Header, HTTPException
from app.core.config import settings

def api_key_auth(x_api_key: str = Header(...)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.config import settings

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        api_key = request.headers.get("x-api-key")
        if api_key != settings.API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key")
        return await call_next(request)
