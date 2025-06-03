import asyncio
import datetime as dt
from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import Response
from scheduler.trigger import weekday as weekday_factory

from reminder_ai.scheduler import UTC, Scheduler

ROUTE_REMINDERS = "reminders"

router_reminders = APIRouter(tags=[ROUTE_REMINDERS])


async def fake_remind(
    *,
    user_id: UUID | None = None,
    group_id: UUID | None = None,
    prompt: str,
) -> None:
    t_generate = "[{entity}] Generate reminder message with prompt: {prompt}..."
    t_remind = "[{entity}] Sending reminder message via WhatsApp API"

    match user_id, group_id:
        case UUID() as uuid, None:
            print(t_generate.format(entity=f"User {uuid}", prompt=prompt[:20]))
            await asyncio.sleep(4)  # simulate request to llm api
            print(t_remind.format(entity=f"User {uuid}"))
        case None, UUID() as uuid:
            print(t_generate.format(entity=f"Group {uuid}", prompt=prompt[:20]))
            await asyncio.sleep(4)  # simulate request to llm api
            print(t_remind.format(entity=f"Group {uuid}"))
        case _:
            raise ValueError("Exactly one of user_id or group_id is required.")


@router_reminders.post("/users/{user_id}")
async def _(
    *,
    user_id: UUID,
    prompt: str,
) -> Response:
    schedule_time = dt.datetime.now(tz=UTC) + dt.timedelta(seconds=10)
    Scheduler.schedule.once(
        schedule_time, fake_remind, kwargs={"user_id": user_id, "prompt": prompt}
    )
    return Response(content="OK")


@router_reminders.post("/groups/{group_id}")
async def _(
    *,
    group_id: UUID,
    prompt: str,
    weekday: int,  # 0: Monday, ..., 6: Sunday
    n_weeks: int,
) -> Response:
    schedule_time = weekday_factory(weekday, dt.time(hour=9, minute=0, tzinfo=UTC))
    Scheduler.schedule.weekly(
        schedule_time,
        fake_remind,
        kwargs={"group_id": group_id, "prompt": prompt},
        max_attempts=n_weeks,
    )
    return Response(content="OK")
