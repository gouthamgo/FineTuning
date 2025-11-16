"""
Fine-Tuning Learning Dashboard
A simple Streamlit app to track your learning progress
"""

import streamlit as st
import os
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Fine-Tuning Learning Platform",
    page_icon="🚀",
    layout="wide"
)

# Progress tracking file
PROGRESS_FILE = "webapp/progress.json"

def load_progress():
    """Load user progress from file."""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_progress(progress):
    """Save user progress to file."""
    os.makedirs(os.path.dirname(PROGRESS_FILE), exist_ok=True)
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)

def get_lesson_status(lesson_id, progress):
    """Get the status of a lesson."""
    return progress.get(lesson_id, "not_started")

# Load progress
progress = load_progress()

# Header
st.title("🚀 Fine-Tuning Learning Platform")
st.markdown("### Learn to Fine-Tune Transformer Models from Scratch")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("📊 Your Progress")

    total_lessons = 15
    completed = sum(1 for status in progress.values() if status == "completed")
    progress_pct = (completed / total_lessons) * 100

    st.metric("Lessons Completed", f"{completed}/{total_lessons}")
    st.progress(progress_pct / 100)

    st.markdown("---")
    st.markdown("### 🎯 Quick Links")
    st.markdown("- [HuggingFace Docs](https://huggingface.co/docs)")
    st.markdown("- [Transformers Tutorials](https://huggingface.co/course)")
    st.markdown("- [GitHub Repository](https://github.com/gouthamgo/FineTuning)")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📚 Learning Path")

    # Module 1
    with st.expander("🟢 Module 1: Foundations", expanded=True):
        st.markdown("**Duration:** 1 week | **Difficulty:** Beginner")
        st.markdown("Learn the basics of fine-tuning and transformers.")

        lessons = [
            {
                "id": "m1l1",
                "title": "What is Fine-Tuning?",
                "duration": "30 min",
                "path": "lessons/module1_foundations/01_what_is_finetuning.ipynb"
            },
            {
                "id": "m1l2",
                "title": "Your First Model",
                "duration": "1 hour",
                "path": "lessons/module1_foundations/02_your_first_model.ipynb"
            },
            {
                "id": "m1l3",
                "title": "Understanding Data",
                "duration": "1 hour",
                "path": "lessons/module1_foundations/03_understanding_data.ipynb"
            }
        ]

        for lesson in lessons:
            status = get_lesson_status(lesson["id"], progress)

            col_a, col_b, col_c = st.columns([3, 1, 1])

            with col_a:
                if status == "completed":
                    st.markdown(f"✅ **{lesson['title']}** ({lesson['duration']})")
                elif status == "in_progress":
                    st.markdown(f"🔵 **{lesson['title']}** ({lesson['duration']})")
                else:
                    st.markdown(f"⚪ {lesson['title']} ({lesson['duration']})")

            with col_b:
                if os.path.exists(lesson["path"]):
                    st.markdown(f"[Open Notebook]({lesson['path']})")
                else:
                    st.markdown("*Coming soon*")

            with col_c:
                if status != "completed":
                    if st.button("✓ Mark Done", key=lesson["id"]):
                        progress[lesson["id"]] = "completed"
                        save_progress(progress)
                        st.rerun()

    # Module 2
    with st.expander("🟡 Module 2: Your First Fine-Tuning", expanded=False):
        st.markdown("**Duration:** 1 week | **Difficulty:** Beginner")
        st.markdown("Actually fine-tune your first model!")

        lessons = [
            {
                "id": "m2l1",
                "title": "First Fine-Tuning (Sentiment Analysis)",
                "duration": "2 hours",
                "path": "lessons/module2_first_training/01_first_finetuning.ipynb"
            },
            {
                "id": "m2l2",
                "title": "Evaluating Your Model",
                "duration": "1 hour",
                "path": "lessons/module2_first_training/02_evaluation.ipynb"
            },
            {
                "id": "m2l3",
                "title": "Saving and Sharing Models",
                "duration": "1 hour",
                "path": "lessons/module2_first_training/03_saving_models.ipynb"
            }
        ]

        for lesson in lessons:
            status = get_lesson_status(lesson["id"], progress)

            col_a, col_b, col_c = st.columns([3, 1, 1])

            with col_a:
                if status == "completed":
                    st.markdown(f"✅ **{lesson['title']}** ({lesson['duration']})")
                elif status == "in_progress":
                    st.markdown(f"🔵 **{lesson['title']}** ({lesson['duration']})")
                else:
                    st.markdown(f"⚪ {lesson['title']} ({lesson['duration']})")

            with col_b:
                if os.path.exists(lesson["path"]):
                    st.markdown(f"[Open Notebook]({lesson['path']})")
                else:
                    st.markdown("*Coming soon*")

            with col_c:
                if status != "completed":
                    if st.button("✓ Mark Done", key=lesson["id"]):
                        progress[lesson["id"]] = "completed"
                        save_progress(progress)
                        st.rerun()

    # Module 3
    with st.expander("🟠 Module 3: Going Deeper", expanded=False):
        st.markdown("**Duration:** 1 week | **Difficulty:** Intermediate")
        st.markdown("Understand hyperparameters and advanced techniques.")

        st.markdown("⚪ Hyperparameters Demystified (1.5 hours)")
        st.markdown("⚪ Common Problems & Solutions (1.5 hours)")
        st.markdown("⚪ LoRA and Optimization (1 hour)")

    # Module 4
    with st.expander("🔴 Module 4: Real-World Projects", expanded=False):
        st.markdown("**Duration:** 2 weeks | **Difficulty:** Intermediate")
        st.markdown("Build portfolio-worthy projects.")

        st.markdown("⚪ Project A: Customer Support Classifier")
        st.markdown("⚪ Project B: Named Entity Recognition")
        st.markdown("⚪ Project C: Custom Chatbot")
        st.markdown("⚪ Project D: Document Analyzer")

    # Module 5
    with st.expander("🟣 Module 5: Production & Optimization", expanded=False):
        st.markdown("**Duration:** 1 week | **Difficulty:** Advanced")
        st.markdown("Deploy and optimize your models.")

        st.markdown("⚪ Model Optimization (2 hours)")
        st.markdown("⚪ Deployment Options (2 hours)")
        st.markdown("⚪ Monitoring & Iteration (1 hour)")

with col2:
    st.header("🎯 Quick Start")

    st.markdown("""
    ### Getting Started

    1. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

    2. **Launch Jupyter**
    ```bash
    jupyter lab
    ```

    3. **Start with Module 1**
    - Open Lesson 1.1 notebook
    - Follow along step-by-step
    - Complete exercises

    4. **Track Your Progress**
    - Mark lessons as complete
    - See your progress grow!
    """)

    st.markdown("---")

    st.header("📈 Learning Tips")

    st.info("""
    💡 **Tip 1:** Code along!
    Don't just read - type the code yourself.
    """)

    st.info("""
    💡 **Tip 2:** Use Google Colab
    Free GPU access for faster training!
    """)

    st.info("""
    💡 **Tip 3:** Start small
    Use small datasets first, then scale up.
    """)

    st.info("""
    💡 **Tip 4:** Experiment
    Change parameters and see what happens!
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ for aspiring ML engineers | Happy Learning! 🚀</p>
</div>
""", unsafe_allow_html=True)
