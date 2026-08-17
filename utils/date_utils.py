from datetime import date


def get_day_number(join_date: date, today: date) -> int:
    """Return number of days since joining (starting at 1)."""
    delta = (today - join_date).days + 1
    return max(delta, 1)

def get_week_and_day(day_number: int) -> tuple[int, int]:
    """Convert day number → (week, day). Week has 6 days (Mon–Sat)."""
    week = (day_number - 1) // 6 + 1
    day = (day_number - 1) % 6 + 1
    return week, day


def is_sunday(date_obj: date) -> bool:
    """Return True if the given date is Sunday."""
    return date_obj.weekday() == 6