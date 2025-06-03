from fastapi import APIRouter
from fastapi.responses import Response

from reminder_ai.scheduler import Scheduler

ROUTE_STATUS = "status"
router_status = APIRouter(tags=[ROUTE_STATUS])


@router_status.get("/scheduler")
async def _() -> Response:
    return Response(content=str(Scheduler.schedule), status_code=200)
