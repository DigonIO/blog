from fastapi import APIRouter

from sales_ai.api.v1.messages import router_messages, ROUTE_MESSAGES

router_v1 = APIRouter()
router_v1.include_router(router_messages, prefix=f"/{ROUTE_MESSAGES}")
