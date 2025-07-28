from fastapi import APIRouter

from reminder_ai.api.v1.reminders import ROUTE_REMINDERS, router_reminders
from reminder_ai.api.v1.status import ROUTE_STATUS, router_status
from reminder_ai.api.v1.for_the_lazy import ROUTE_FOR_THE_LAZY, router_for_the_lazy

router_v1 = APIRouter()
router_v1.include_router(router_reminders, prefix=f"/{ROUTE_REMINDERS}")
router_v1.include_router(router_status, prefix=f"/{ROUTE_STATUS}")
router_v1.include_router(router_for_the_lazy, prefix=f"/{ROUTE_FOR_THE_LAZY}")
