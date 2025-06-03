from fastapi import APIRouter

from sales_ai.api.v1.reminders import router_reminders, ROUTE_REMINDERS
from sales_ai.api.v1.status import router_status, ROUTE_STATUS

router_v1 = APIRouter()
router_v1.include_router(router_reminders, prefix=f"/{ROUTE_REMINDERS}")
router_v1.include_router(router_status, prefix=f"/{ROUTE_STATUS}")
