import asyncio
import datetime as dt
import random
import signal
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI

from reminder_ai.api import router_api
from reminder_ai.scheduler import UTC, Scheduler


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
        dt.time(hour=0, minute=0, second=0, tzinfo=UTC), fake_reset_daily_token_quota
    )
    yield


app = FastAPI(
    title="Reminder AI",
    lifespan=lifespan,
)

app.include_router(router=router_api, prefix="/api")
