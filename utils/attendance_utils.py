from datetime import datetime, timezone
from supabase_client import supabase


def mark_attendance(student_id: str, status: str = "Present") -> None:
    """
    Insert attendance record for the student if not already marked today.
    Uses timezone-aware datetime to satisfy Ruff DTZ005.
    """

    today = datetime.now(timezone.utc).date()

    # Check if attendance already exists for today
    existing = (
        supabase.table("attendance")
        .select("id")
        .eq("student_id", student_id)
        .eq("attendance_date", str(today))
        .execute()
    )

    if existing.data:
        return  # Already marked

    # Insert new attendance record
    supabase.table("attendance").insert({
        "student_id": student_id,
        "attendance_date": str(today),
        "status": status
    }).execute()
