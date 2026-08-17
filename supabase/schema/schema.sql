-- Assignments (per week/day or standalone)
create table calculus_portal.assignments (
  id bigserial primary key,
  title text not null,
  description text,
  week_number int,
  day_number int,
  created_at timestamptz not null default now()
);

-- Questions
create table calculus_portal.questions (
  id bigserial primary key,
  assignment_id bigint not null,
  question_text text not null,
  question_type text not null, -- 'MCQ', 'NUMERIC', 'SYMBOLIC'
  options jsonb,               -- for MCQ: ["A","B","C","D"]
  correct_answer text not null,
  max_marks int not null default 1,

  constraint questions_assignment_fkey
    foreign key (assignment_id)
    references calculus_portal.assignments (id) on delete cascade,

  constraint questions_type_check
    check (question_type in ('MCQ', 'NUMERIC', 'SYMBOLIC'))
);

-- Submissions
create table calculus_portal.submissions (
  id bigserial primary key,
  student_id uuid not null,
  assignment_id bigint not null,
  submitted_at timestamptz not null default now(),
  total_marks_obtained int not null,
  max_marks int not null,

  constraint submissions_student_fkey
    foreign key (student_id)
    references calculus_portal.students (id) on delete cascade,

  constraint submissions_assignment_fkey
    foreign key (assignment_id)
    references calculus_portal.assignments (id) on delete cascade
);

-- Per-question responses
create table calculus_portal.submission_items (
  id bigserial primary key,
  submission_id bigint not null,
  question_id bigint not null,
  student_answer text not null,
  is_correct boolean not null,
  marks_obtained int not null,

  constraint submission_items_submission_fkey
    foreign key (submission_id)
    references calculus_portal.submissions (id) on delete cascade,

  constraint submission_items_question_fkey
    foreign key (question_id)
    references calculus_portal.questions (id) on delete cascade
);
