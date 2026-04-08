from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
from starlette.responses import JSONResponse

from api.graph import app_graph

api = FastAPI(
    title="AI Assistant API",
    summary="AI Assistant API - service to answer FAQ questions",
    version="1.0.0",
)

api.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


async def generate_chat_responses(message: str):
    initial_input = {"messages": [HumanMessage(content=message)]}

    async for event in app_graph.astream(initial_input, stream_mode="messages"):
        msg, metadata = event

        if msg.content:
            yield msg.content


@api.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    return StreamingResponse(
        generate_chat_responses(chat_request.message),
        media_type="text/event-stream"
    )


@api.get("/health", tags=["Health"], response_class=JSONResponse)
async def health_check():
    return JSONResponse({"status": "OK"})
