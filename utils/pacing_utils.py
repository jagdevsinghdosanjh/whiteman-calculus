from datetime import datetime, timezone
from utils.date_utils import get_day_number, get_week_and_day, is_sunday


def get_today_pacing(join_date):
    """
    Return (week, day, is_sunday) for today's lesson.
    Uses timezone-aware datetime to satisfy Ruff DTZ005.
    """
    today = datetime.now(timezone.utc).date()

    if is_sunday(today):
        return None, None, True

    day_number = get_day_number(join_date, today)
    week, day = get_week_and_day(day_number)

    return week, day, False
