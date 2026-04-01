from fastapi import FastAPI
from starlette.responses import JSONResponse

api = FastAPI(
    title="AI Assistant API",
    summary="AI Assistant API - service to answer FAQ questions",
    version="1.0.0",
)


@api.get("/health", tags=["Health"], response_class=JSONResponse)
async def health_check():
    return JSONResponse({"status": "OK"})
