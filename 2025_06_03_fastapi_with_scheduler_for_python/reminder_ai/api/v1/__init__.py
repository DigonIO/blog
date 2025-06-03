from fastapi import APIRouter

from reminder_ai.api.v1.reminders import ROUTE_REMINDERS, router_reminders
from reminder_ai.api.v1.status import ROUTE_STATUS, router_status

router_v1 = APIRouter()
router_v1.include_router(router_reminders, prefix=f"/{ROUTE_REMINDERS}")
router_v1.include_router(router_status, prefix=f"/{ROUTE_STATUS}")
