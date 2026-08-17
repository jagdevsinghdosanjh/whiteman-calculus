-- ============================================================
-- SCHEMA: calculus_portal
-- FULL PRODUCTION-SAFE LMS SCHEMA
-- ============================================================

-- Create schema if not exists
CREATE SCHEMA IF NOT EXISTS calculus_portal;

-- ============================================================
-- TABLE: students
-- ============================================================

CREATE TABLE IF NOT EXISTS calculus_portal.students (
  id uuid NOT NULL,
  full_name text NOT NULL,
  email text NOT NULL,
  join_date date NOT NULL DEFAULT CURRENT_DATE,
  created_at timestamptz DEFAULT now(),
  CONSTRAINT students_pkey PRIMARY KEY (id),
  CONSTRAINT students_email_key UNIQUE (email),
  CONSTRAINT students_id_fkey FOREIGN KEY (id)
      REFERENCES auth.users(id) ON DELETE CASCADE
);

-- RLS
ALTER TABLE calculus_portal.students ENABLE ROW LEVEL SECURITY;

CREATE POLICY students_view_own_profile
ON calculus_portal.students
FOR SELECT
USING (auth.uid() = id);

-- ============================================================
-- TABLE: attendance
-- ============================================================

CREATE TABLE IF NOT EXISTS calculus_portal.attendance (
  id bigserial NOT NULL,
  student_id uuid NOT NULL,
  attendance_date date NOT NULL,
  status text NOT NULL,
  marked_at timestamptz DEFAULT now(),
  CONSTRAINT attendance_pkey PRIMARY KEY (id),
  CONSTRAINT attendance_unique_per_day UNIQUE (student_id, attendance_date),
  CONSTRAINT attendance_student_id_fkey FOREIGN KEY (student_id)
      REFERENCES calculus_portal.students(id) ON DELETE CASCADE,
  CONSTRAINT attendance_status_check CHECK (
      status IN ('Present', 'Absent')
  )
);

-- RLS
ALTER TABLE calculus_portal.attendance ENABLE ROW LEVEL SECURITY;

CREATE POLICY attendance_view_own
ON calculus_portal.attendance
FOR SELECT
USING (auth.uid() = student_id);

CREATE POLICY attendance_insert_own
ON calculus_portal.attendance
FOR INSERT
WITH CHECK (auth.uid() = student_id);

-- ============================================================
-- TABLE: student_progress
-- ============================================================

CREATE TABLE IF NOT EXISTS calculus_portal.student_progress (
  id bigserial NOT NULL,
  student_id uuid NOT NULL,
  progress_date date NOT NULL,
  day_number int NOT NULL,
  week_number int NOT NULL,
  day_in_week int NOT NULL,
  created_at timestamptz DEFAULT now(),
  CONSTRAINT student_progress_pkey PRIMARY KEY (id),
  CONSTRAINT progress_unique_per_day UNIQUE (student_id, progress_date),
  CONSTRAINT student_progress_student_id_fkey FOREIGN KEY (student_id)
      REFERENCES calculus_portal.students(id) ON DELETE CASCADE
);

-- RLS
ALTER TABLE calculus_portal.student_progress ENABLE ROW LEVEL SECURITY;

CREATE POLICY progress_view_own
ON calculus_portal.student_progress
FOR SELECT
USING (auth.uid() = student_id);

-- ============================================================
-- END OF SCHEMA
-- ============================================================
