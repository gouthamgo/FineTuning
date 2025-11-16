"""
Fine-Tuning Learning Platform - Public Dashboard
Free, open-source learning platform for transformer fine-tuning
"""

import streamlit as st
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(
    page_title="Fine-Tuning Learning Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .lesson-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #e0e0e0;
        margin-bottom: 1rem;
        background: white;
    }
    .lesson-card:hover {
        border-color: #667eea;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .colab-button {
        background: linear-gradient(90deg, #f9ab00 0%, #f57c00 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
    }
    .progress-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight: bold;
    }
    .badge-completed {
        background: #10b981;
        color: white;
    }
    .badge-available {
        background: #3b82f6;
        color: white;
    }
    .badge-coming-soon {
        background: #9ca3af;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Lesson data
LESSONS = {
    "module1": {
        "title": "🟢 Module 1: Foundations",
        "subtitle": "Get comfortable with transformers and pre-trained models",
        "duration": "Week 1",
        "lessons": [
            {
                "id": "m1l1",
                "title": "What is Fine-Tuning?",
                "duration": "30 min",
                "difficulty": "Beginner",
                "description": "Learn the fundamentals of fine-tuning, when to use it, and real-world examples.",
                "colab_url": "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module1_foundations/01_what_is_finetuning.ipynb",
                "status": "available"
            },
            {
                "id": "m1l2",
                "title": "Your First Model",
                "duration": "1 hour",
                "difficulty": "Beginner",
                "description": "Load pre-trained models, understand tokenizers, and run your first inference.",
                "colab_url": "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module1_foundations/02_your_first_model.ipynb",
                "status": "available"
            },
            {
                "id": "m1l3",
                "title": "Understanding Data",
                "duration": "1 hour",
                "difficulty": "Beginner",
                "description": "Learn about dataset formats, data preparation, and quality checks.",
                "colab_url": "",
                "status": "coming_soon"
            }
        ]
    },
    "module2": {
        "title": "🟡 Module 2: Your First Fine-Tuning",
        "subtitle": "Actually train your first model!",
        "duration": "Week 2",
        "lessons": [
            {
                "id": "m2l1",
                "title": "First Fine-Tuning (Sentiment Analysis)",
                "duration": "2 hours",
                "difficulty": "Beginner",
                "description": "Fine-tune a sentiment classifier from scratch on IMDB reviews. Watch your model learn!",
                "colab_url": "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module2_first_training/01_first_finetuning.ipynb",
                "status": "available",
                "featured": True
            },
            {
                "id": "m2l2",
                "title": "Evaluating Your Model",
                "duration": "1 hour",
                "difficulty": "Beginner",
                "description": "Deep dive into metrics, confusion matrices, and error analysis.",
                "colab_url": "",
                "status": "coming_soon"
            },
            {
                "id": "m2l3",
                "title": "Saving & Sharing Models",
                "duration": "1 hour",
                "difficulty": "Beginner",
                "description": "Save your model and share it on HuggingFace Hub.",
                "colab_url": "",
                "status": "coming_soon"
            }
        ]
    },
    "module3": {
        "title": "🟠 Module 3: Going Deeper",
        "subtitle": "Master hyperparameters and optimization",
        "duration": "Week 3",
        "lessons": [
            {
                "id": "m3l1",
                "title": "Hyperparameters Demystified",
                "duration": "1.5 hours",
                "difficulty": "Intermediate",
                "description": "Understand learning rate, batch size, epochs, and more.",
                "colab_url": "",
                "status": "coming_soon"
            }
        ]
    }
}

# Sidebar
with st.sidebar:
    st.markdown("### 🎓 Navigation")

    selected = option_menu(
        menu_title=None,
        options=["Home", "Lessons", "About", "Deploy"],
        icons=["house", "book", "info-circle", "cloud-upload"],
        default_index=0,
    )

    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    total_lessons = sum(len(m["lessons"]) for m in LESSONS.values())
    available_lessons = sum(1 for m in LESSONS.values() for l in m["lessons"] if l["status"] == "available")

    st.metric("Available Lessons", f"{available_lessons}/{total_lessons}")
    st.metric("Modules", len(LESSONS))

    st.markdown("---")
    st.markdown("### 🔗 Quick Links")
    st.markdown("- [GitHub Repo](https://github.com/gouthamgo/FineTuning)")
    st.markdown("- [HuggingFace Docs](https://huggingface.co/docs)")
    st.markdown("- [Google Colab](https://colab.research.google.com/)")

# Main content based on selection
if selected == "Home":
    st.markdown('<div class="main-header">🚀 Fine-Tuning Learning Platform</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Learn to Fine-Tune Transformer Models from Scratch</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Interactive • Free • Open Source • No Setup Required</p>", unsafe_allow_html=True)

    st.markdown("---")

    # Hero section
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📓 Interactive")
        st.write("Learn by doing with hands-on Jupyter notebooks in Google Colab")

    with col2:
        st.markdown("### 💰 100% Free")
        st.write("Free GPU from Google Colab. No credit card required.")

    with col3:
        st.markdown("### 🎯 Beginner-Friendly")
        st.write("From zero to fine-tuning in 6 weeks. No PhD needed!")

    st.markdown("---")

    # Quick Start
    st.markdown("## 🚀 Quick Start")

    st.markdown("""
    ### How It Works:

    1. **Choose a lesson** from the Lessons tab
    2. **Click "Open in Colab"** - Opens in Google Colab (free GPU!)
    3. **Run the notebook** - Learn by actually coding
    4. **Build real projects** - Create portfolio-worthy applications

    **That's it!** No installation, no setup, no cost.
    """)

    # Featured lesson
    st.markdown("---")
    st.markdown("## ⭐ Featured Lesson")

    featured = None
    for module in LESSONS.values():
        for lesson in module["lessons"]:
            if lesson.get("featured"):
                featured = lesson
                break

    if featured:
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(f"### {featured['title']}")
            st.write(featured['description'])
            st.markdown(f"**Duration:** {featured['duration']} | **Difficulty:** {featured['difficulty']}")

        with col2:
            st.markdown("### ")
            st.markdown("### ")
            st.markdown(f"[<img src='https://colab.research.google.com/assets/colab-badge.svg'>]({featured['colab_url']})", unsafe_allow_html=True)

    # Learning path overview
    st.markdown("---")
    st.markdown("## 📚 Learning Path")

    for module_key, module in LESSONS.items():
        with st.expander(f"{module['title']} ({module['duration']})", expanded=(module_key == "module1")):
            st.markdown(f"*{module['subtitle']}*")
            st.write(f"**{len(module['lessons'])} lessons**")

elif selected == "Lessons":
    st.markdown('<div class="main-header">📚 All Lessons</div>', unsafe_allow_html=True)

    # Filter
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("Browse all lessons organized by module")
    with col2:
        filter_status = st.selectbox("Filter", ["All", "Available", "Coming Soon"])

    st.markdown("---")

    # Display lessons by module
    for module_key, module in LESSONS.items():
        st.markdown(f"## {module['title']}")
        st.markdown(f"**{module['subtitle']}** • {module['duration']}")
        st.markdown("")

        for lesson in module["lessons"]:
            # Apply filter
            if filter_status == "Available" and lesson["status"] != "available":
                continue
            if filter_status == "Coming Soon" and lesson["status"] != "coming_soon":
                continue

            # Lesson card
            col1, col2 = st.columns([3, 1])

            with col1:
                # Status badge
                if lesson["status"] == "available":
                    badge_class = "badge-available"
                    badge_text = "✅ Available"
                else:
                    badge_class = "badge-coming-soon"
                    badge_text = "🔜 Coming Soon"

                st.markdown(f'<span class="progress-badge {badge_class}">{badge_text}</span>', unsafe_allow_html=True)

                st.markdown(f"### {lesson['title']}")
                st.write(lesson['description'])
                st.markdown(f"⏱️ {lesson['duration']} | 📊 {lesson['difficulty']}")

            with col2:
                st.markdown("###")
                if lesson["status"] == "available" and lesson["colab_url"]:
                    st.markdown(f"""
                    <a href="{lesson['colab_url']}" target="_blank">
                        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
                    </a>
                    """, unsafe_allow_html=True)
                else:
                    st.info("Coming Soon!")

            st.markdown("---")

elif selected == "About":
    st.markdown('<div class="main-header">ℹ️ About This Platform</div>', unsafe_allow_html=True)

    st.markdown("""
    ## What is This?

    This is a **completely free, open-source learning platform** for anyone who wants to learn fine-tuning of transformer models.

    ### Why We Built This

    Most fine-tuning tutorials are either:
    - ❌ Too theoretical (no actual code)
    - ❌ Too advanced (assumes you're an expert)
    - ❌ Incomplete (leaves you hanging)
    - ❌ Expensive (requires paid services)

    We wanted something different:
    - ✅ **Hands-on** - Write real code, train real models
    - ✅ **Complete** - From zero to production
    - ✅ **Free** - No hidden costs
    - ✅ **Beginner-friendly** - Clear explanations

    ### The Technology Stack

    Everything we use is free:

    - **Google Colab** - Free GPU for training (worth $100s/month!)
    - **HuggingFace** - Pre-trained models and datasets
    - **GitHub** - Host all notebooks and code
    - **Streamlit Cloud** - This dashboard (deployed for free)

    **Total cost: $0** 💰

    ### Learning Philosophy

    1. **Learn by Doing** - Every lesson has runnable code
    2. **Progressive Complexity** - Start simple, build up
    3. **Real Projects** - Build portfolio-worthy work
    4. **Community-Driven** - Open source, community contributions welcome

    ### Curriculum Overview

    **Module 1:** Foundations (Week 1)
    - Understand what fine-tuning is
    - Load and use pre-trained models
    - Prepare data for training

    **Module 2:** Your First Fine-Tuning (Week 2)
    - Actually fine-tune a sentiment classifier
    - Evaluate model performance
    - Save and share your model

    **Module 3:** Going Deeper (Week 3)
    - Master hyperparameters
    - Advanced optimization (LoRA, quantization)
    - Troubleshoot common issues

    **Module 4:** Real-World Projects (Week 4-5)
    - Customer support classifier
    - Named entity recognition
    - Custom chatbot
    - Document analyzer

    **Module 5:** Production (Week 6)
    - Model optimization
    - Deployment options
    - Monitoring and iteration

    ### Contributing

    This is an open-source project! We welcome:
    - 🐛 Bug reports
    - 💡 Feature suggestions
    - 📝 New lessons or improvements
    - 🌟 Stars on GitHub

    [Visit our GitHub repo](https://github.com/gouthamgo/FineTuning) to contribute!

    ### Credits

    Built with ❤️ using:
    - [HuggingFace Transformers](https://huggingface.co/docs/transformers/)
    - [Google Colab](https://colab.research.google.com/)
    - [Streamlit](https://streamlit.io/)
    - [PyTorch](https://pytorch.org/)

    ---

    **Made for learners, by learners. Always free. Always open source.**
    """)

elif selected == "Deploy":
    st.markdown('<div class="main-header">☁️ Deploy Your Own</div>', unsafe_allow_html=True)

    st.markdown("""
    ## Want to run this dashboard yourself?

    You can deploy your own version of this platform for **FREE** on Streamlit Cloud!

    ### Step-by-Step Deployment

    #### 1. Fork the Repository

    ```bash
    # Go to: https://github.com/gouthamgo/FineTuning
    # Click "Fork" in the top right
    ```

    #### 2. Sign Up for Streamlit Cloud

    - Go to [share.streamlit.io](https://share.streamlit.io)
    - Sign in with your GitHub account (free)

    #### 3. Deploy the App

    1. Click "New app"
    2. Select your forked repository
    3. Set:
       - **Branch:** `main`
       - **Main file path:** `webapp/app.py`
    4. Click "Deploy"!

    **That's it!** Your dashboard will be live in ~2 minutes.

    #### 4. Share Your Link

    You'll get a URL like: `https://yourname-finetuning.streamlit.app`

    Share it with:
    - Your students
    - Your team
    - The world!

    ### Free Tier Limits

    Streamlit Cloud free tier includes:
    - ✅ Unlimited public apps
    - ✅ 1 GB RAM per app
    - ✅ Custom domain support
    - ✅ Community support

    **Perfect for this dashboard!**

    ### Custom Domain (Optional)

    Want to use your own domain? Streamlit Cloud supports custom domains on the free tier!

    Just add a CNAME record pointing to your Streamlit app.

    ### Need Help?

    - [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
    - [GitHub Issues](https://github.com/gouthamgo/FineTuning/issues)

    ---

    ## Local Development

    Want to run this locally?

    ```bash
    # Clone the repo
    git clone https://github.com/gouthamgo/FineTuning.git
    cd FineTuning

    # Install dependencies
    pip install streamlit streamlit-option-menu

    # Run the dashboard
    streamlit run webapp/app.py
    ```

    Opens at `http://localhost:8501`
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem;'>
    <p>Built with ❤️ for the ML community</p>
    <p>
        <a href='https://github.com/gouthamgo/FineTuning' target='_blank'>GitHub</a> •
        <a href='https://huggingface.co/docs/transformers' target='_blank'>HuggingFace</a> •
        <a href='https://colab.research.google.com' target='_blank'>Google Colab</a>
    </p>
    <p style='color: #666; font-size: 0.9rem;'>100% Free • Open Source • No Setup Required</p>
</div>
""", unsafe_allow_html=True)
