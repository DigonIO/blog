import signal
from typing import Any, AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from sales_ai.scheduler import Scheduler
from sales_ai.api import router_api


def stop_scheduler(*args: Any) -> None:
    Scheduler.stop_scheduler()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    Scheduler.start_scheduler()
    signal.signal(signal.SIGINT, stop_scheduler)
    yield


app = FastAPI(
    title="Sales AI",
    lifespan=lifespan,
)

app.include_router(router=router_api, prefix="/api")
