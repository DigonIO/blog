import asyncio
import datetime as dt
from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from scheduler.trigger import weekday as weekday_factory
from pydantic import BaseModel

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


class V1RemindersUsers_Post_Body(BaseModel):
    prompt: str
    schedule_time: dt.datetime | None = None  # None means now


@router_reminders.post("/users/{user_id}")
async def _(*, user_id: UUID, body: V1RemindersUsers_Post_Body) -> PlainTextResponse:
    Scheduler.schedule.once(
        body.schedule_time or dt.timedelta(),
        fake_remind,
        kwargs={"user_id": user_id, "prompt": body.prompt},
    )
    return PlainTextResponse(content="OK")


class V1RemindersGroups_Post_Body(BaseModel):
    prompt: str
    weekday: int  # 0: Monday, ..., 6: Sunday
    n_weeks: int


@router_reminders.post("/groups/{group_id}")
async def _(
    *,
    group_id: UUID,
    body: V1RemindersGroups_Post_Body,
) -> PlainTextResponse:
    day_and_time = weekday_factory(body.weekday, dt.time(hour=9, minute=0, tzinfo=UTC))
    Scheduler.schedule.weekly(
        day_and_time,
        fake_remind,
        kwargs={"group_id": group_id, "prompt": body.prompt},
        max_attempts=body.n_weeks,
    )
    return PlainTextResponse(content="OK")
