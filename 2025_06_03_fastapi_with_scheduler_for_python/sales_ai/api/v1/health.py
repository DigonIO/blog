from fastapi import APIRouter, HTTPException
from typing import Literal

ROUTE_HEALTH = "health"

router_health = APIRouter(tags=[ROUTE_HEALTH])


@router_health.get("/status")
async def _() -> Literal["OK", "BAD"]:
    raise NotImplementedError
