import os
import json
from textwrap import dedent

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "curriculum.json")
PAGES_DIR = os.path.join(BASE_DIR, "pages")


def load_curriculum():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def make_week_filename(week_number: int) -> str:
    return os.path.join(PAGES_DIR, f"Week_{week_number:02d}.py")


def build_week_page_code(week_label: str) -> str:
    code = f"""
    import streamlit as st
    import json
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "data", "curriculum.json")

    st.set_page_config(page_title="{week_label} – Topics Overview", layout="wide")

    st.title("{week_label} – Topics Overview")

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        curriculum = json.load(f)

    week = curriculum.get("{week_label}", {{}})

    if not week:
        st.warning("No topics defined for {week_label}.")
    else:
        for day, topic in week.items():
            st.markdown(f"### {{day}}: {{topic}}")
    """
    return dedent(code).lstrip()


def generate_week_pages():
    os.makedirs(PAGES_DIR, exist_ok=True)

    curriculum = load_curriculum()
    weeks = sorted(curriculum.keys(), key=lambda w: int(w.split()[1]))

    for week_label in weeks:
        week_number = int(week_label.split()[1])
        filename = make_week_filename(week_number)

        code = build_week_page_code(week_label)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"Generated: {filename}")


if __name__ == "__main__":
    generate_week_pages()

# # generate_week_pages.py
# import os
# import json
# from textwrap import dedent

# PAGES_DIR = "pages"
# CURRICULUM_PATH = "data/curriculum.json"

# def ensure_pages_dir():
#     os.makedirs(PAGES_DIR, exist_ok=True)

# def load_curriculum():
#     with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
#         return json.load(f)

# def make_week_file_content(week_number: int) -> str:
#     week_key = f"Week {week_number}"
#     filename_title = f"Week {week_number:02d}"

#     return dedent(f"""
#     import streamlit as st
#     import json

#     st.set_page_config(page_title="{filename_title} – Calculus Curriculum", layout="wide")

#     st.title("{filename_title} – Topics Overview")

#     with open("data/curriculum.json", "r", encoding="utf-8") as f:
#         curriculum = json.load(f)

#     week_key = "Week {week_number}"
#     week_data = curriculum.get(week_key, {{}})

#     if not week_data:
#         st.warning(f"No curriculum data found for {{week_key}}.")
#     else:
#         st.subheader(f"Curriculum for {{week_key}}")
#         for day, topic in sorted(week_data.items()):
#             st.markdown(f"### {{day}}")
#             st.write(topic)
#     """)

# def generate_week_pages():
#     ensure_pages_dir()
#     curriculum = load_curriculum()

#     for week_number in range(1, 16 + 1):
#         week_key = f"Week {week_number}"
#         if week_key not in curriculum:
#             print(f"Skipping {week_key}: not in curriculum.json")
#             continue

#         filename = os.path.join(PAGES_DIR, f"Week_{week_number:02d}.py")
#         content = make_week_file_content(week_number)

#         with open(filename, "w", encoding="utf-8") as f:
#             f.write(content.strip() + "\n")

#         print(f"Created: {filename}")

# if __name__ == "__main__":
#     generate_week_pages()
