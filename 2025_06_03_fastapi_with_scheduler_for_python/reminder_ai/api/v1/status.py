from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from reminder_ai.scheduler import Scheduler

ROUTE_STATUS = "status"
router_status = APIRouter(tags=[ROUTE_STATUS])


@router_status.get("/scheduler")
async def _() -> PlainTextResponse:
    return PlainTextResponse(content=str(Scheduler.schedule), status_code=200)
