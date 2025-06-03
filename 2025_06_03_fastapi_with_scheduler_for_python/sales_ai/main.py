import signal
from typing import Any, AsyncGenerator
from contextlib import asynccontextmanager
import random
import datetime as dt
import asyncio
from fastapi import FastAPI

from sales_ai.scheduler import Scheduler
from sales_ai.api import router_api


def stop_scheduler(*args: Any) -> None:
    Scheduler.stop_scheduler()


async def fake_health_check() -> None:
    """Simulate a health check with random success/failure."""
    await asyncio.sleep(0.1)  # simulate some work
    status = "ok" if random.random() < 0.8 else "bad"
    print(f"[{dt.datetime.now()}] Platform health check: {status}")


async def fake_reset_daily_token_quota() -> None:
    """Simulate a daily token quota reset."""
    print(f"[{dt.datetime.now()}] Starting to reset daily token quotas for all users")
    await asyncio.sleep(0.5)  # simulate some work
    print(f"[{dt.datetime.now()}] Successfully reset daily token quotas for all users")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    Scheduler.start_scheduler()
    signal.signal(signal.SIGINT, stop_scheduler)

    Scheduler.schedule.cyclic(dt.timedelta(seconds=30), fake_health_check)
    Scheduler.schedule.daily(
        dt.time(hour=0, minute=0, second=0), fake_reset_daily_token_quota
    )
    yield


app = FastAPI(
    title="Sales AI",
    lifespan=lifespan,
)

app.include_router(router=router_api, prefix="/api")
