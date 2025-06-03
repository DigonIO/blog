from fastapi import APIRouter

ROUTE_MESSAGES = "messages"

router_messages = APIRouter(tags=[ROUTE_MESSAGES])


@router_messages.post("/private")
async def _(*, prompt: str) -> str:

    return "Success"


@router_messages.post("/group")
async def _(*, prompt: str, delay: int, count: int) -> str:

    return "Success"
