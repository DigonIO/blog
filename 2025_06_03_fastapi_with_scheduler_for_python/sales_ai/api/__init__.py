from fastapi import APIRouter

from sales_ai.api.v1 import router_v1

router_api = APIRouter()
router_api.include_router(router_v1, prefix="/v1")
