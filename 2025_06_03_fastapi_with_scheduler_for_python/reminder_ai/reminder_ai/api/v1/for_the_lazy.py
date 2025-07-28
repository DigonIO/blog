from uuid import UUID, uuid4
from fastapi import APIRouter


ROUTE_FOR_THE_LAZY = "for_the_lazy"

router_for_the_lazy = APIRouter(tags=[ROUTE_FOR_THE_LAZY])


@router_for_the_lazy.get("/random_uuid4")
async def get_random_uuid4() -> UUID:
    return uuid4()
