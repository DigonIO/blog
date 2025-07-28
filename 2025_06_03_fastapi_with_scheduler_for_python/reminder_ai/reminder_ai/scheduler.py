import asyncio
import datetime as dt

from scheduler.asyncio import Scheduler as AioScheduler

UTC = dt.timezone.utc


class Scheduler:
    is_running_event = asyncio.Event()
    schedule: AioScheduler

    @classmethod
    def start_scheduler(cls) -> None:
        cls.schedule = AioScheduler(tzinfo=UTC)
        cls.is_running_event.set()

    @classmethod
    def stop_scheduler(cls) -> None:
        cls.is_running_event.clear()

    @classmethod
    def is_running(cls) -> bool:
        return cls.is_running_event.is_set()
