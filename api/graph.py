import operator
from typing import List, Annotated

import httpx
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph, END
from pydantic import BaseModel, Field


class AgentState(BaseModel):
    messages: Annotated[List[BaseMessage], operator.add]
    context: str = Field(default="")
    needs_human: bool = Field(default=False)


llm = ChatAnthropic(model="claude-sonnet-4-6", temperature=0.7)


async def researcher_node(state: AgentState):
    user_query = state.messages[-1].content

    mcp_url = "http://faq-assist-mcp:8000/call/search_neo4j"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                mcp_url,
                json={"arguments": {"query": user_query}},
                timeout=20.0
            )
            response.raise_for_status()
            search_result = response.json().get("content", "Nothing found.")
        except Exception as e:
            print(f"MCP Error: {e}")
            search_result = "Could not reach the knowledge base."

    return {"context": str(search_result)}


async def generator_node(state: AgentState):
    prompt = f"Use this context: {state.context}"
    messages = [("system", prompt)] + state.messages

    response = await llm.ainvoke(messages)
    return {"messages": [response]}


workflow = StateGraph(state_schema=AgentState)

workflow.add_node("researcher", researcher_node)
workflow.add_node("generator", generator_node)

workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "generator")
workflow.add_edge("generator", END)

app_graph = workflow.compile()
