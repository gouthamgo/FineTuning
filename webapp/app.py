"""
Fine-Tuning Learning Platform - Ultra Modern Design
Trendy, beautiful, and beginner-friendly!
"""

import streamlit as st
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(
    page_title="Fine-Tuning Academy",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern CSS with glassmorphism and animations
st.markdown("""
<style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Glassmorphism effect for main container */
    .main .block-container {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }

    /* Modern header with text gradient */
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: fadeInDown 1s ease-out;
    }

    .hero-subtitle {
        font-size: 1.5rem;
        text-align: center;
        color: #4a5568;
        font-weight: 500;
        margin-bottom: 0.5rem;
        animation: fadeInUp 1s ease-out;
    }

    .hero-tags {
        text-align: center;
        font-size: 1.1rem;
        color: #718096;
        margin-bottom: 2rem;
        animation: fadeIn 1.5s ease-out;
    }

    /* Fade in animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    /* Modern cards with hover effect */
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        height: 100%;
    }

    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);
    }

    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .feature-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .feature-desc {
        font-size: 1rem;
        opacity: 0.9;
        line-height: 1.6;
    }

    /* Lesson cards - ultra modern */
    .lesson-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        border: 2px solid transparent;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .lesson-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        background-size: 200% 100%;
        animation: shimmer 3s infinite;
    }

    @keyframes shimmer {
        0% {background-position: 200% 0;}
        100% {background-position: -200% 0;}
    }

    .lesson-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 50px rgba(102, 126, 234, 0.3);
        border-color: #667eea;
    }

    /* Status badges - modern pills */
    .badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .badge-available {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }

    .badge-coming {
        background: linear-gradient(135deg, #a8b8d8 0%, #8b9dc3 100%);
        color: white;
    }

    /* Colab button - super eye-catching */
    .colab-btn {
        display: inline-block;
        background: linear-gradient(135deg, #f9ab00 0%, #ff6b6b 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(249, 171, 0, 0.3);
        border: none;
    }

    .colab-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(249, 171, 0, 0.5);
        text-decoration: none;
        color: white;
    }

    /* Stats boxes */
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
    }

    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Section headers */
    .section-header {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* Module sections */
    .module-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        font-size: 1.8rem;
        font-weight: 700;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }

    /* Smooth scrolling */
    html {
        scroll-behavior: smooth;
    }

    /* Better spacing */
    .spacer-small {
        height: 2rem;
    }

    .spacer-large {
        height: 4rem;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        color: white;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Link styling */
    a {
        color: #667eea;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    a:hover {
        color: #764ba2;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Lesson data
LESSONS = {
    "module1": {
        "title": "🌱 Foundations",
        "emoji": "🟢",
        "subtitle": "Start your journey - understand the basics",
        "duration": "Week 1",
        "color": "#10b981",
        "lessons": [
            {
                "id": "m1l1",
                "title": "What Even is Fine-Tuning? (Let's Talk Like Friends)",
                "duration": "30 min",
                "difficulty": "Super Beginner",
                "description": "Seriously, what is this fine-tuning thing everyone talks about? I'll explain it like we're chatting over coffee. Zero jargon, promise!",
                "colab_url": "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module1_foundations/01_what_is_finetuning.ipynb",
                "status": "available",
                "icon": "💡"
            },
            {
                "id": "m1l2",
                "title": "Your First AI Model (Yes, YOU Can Do This!)",
                "duration": "1 hour",
                "difficulty": "Beginner",
                "description": "Let's actually load a real AI model and make it work! We'll take it step-by-step. You'll be amazed at how easy this is.",
                "colab_url": "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module1_foundations/02_your_first_model.ipynb",
                "status": "available",
                "icon": "🤖"
            },
            {
                "id": "m1l3",
                "title": "Understanding Your Data (The Secret Sauce)",
                "duration": "1 hour",
                "difficulty": "Beginner",
                "description": "Data is like ingredients for cooking. Bad ingredients = bad food. I'll show you how to prep your data like a chef!",
                "colab_url": "",
                "status": "coming_soon",
                "icon": "📊"
            }
        ]
    },
    "module2": {
        "title": "🚀 Your First Fine-Tuning",
        "emoji": "🟡",
        "subtitle": "This is where the magic happens!",
        "duration": "Week 2",
        "color": "#f59e0b",
        "lessons": [
            {
                "id": "m2l1",
                "title": "ACTUALLY Fine-Tune Your First Model! 🎉",
                "duration": "2 hours",
                "difficulty": "Beginner",
                "description": "This is THE lesson! You'll train your own AI model from scratch. Watch it learn in real-time. It's like magic, but it's REAL!",
                "colab_url": "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module2_first_training/01_first_finetuning.ipynb",
                "status": "available",
                "featured": True,
                "icon": "⚡"
            },
            {
                "id": "m2l2",
                "title": "Is Your Model Actually Good? (Let's Find Out)",
                "duration": "1 hour",
                "difficulty": "Beginner",
                "description": "Your model is trained! But... is it good? I'll show you how to test it properly (and what all those numbers mean).",
                "colab_url": "",
                "status": "coming_soon",
                "icon": "📈"
            },
            {
                "id": "m2l3",
                "title": "Save & Share Your Model (Show Off Time!)",
                "duration": "1 hour",
                "difficulty": "Beginner",
                "description": "Let's save your model and put it online so others can use it. Add this to your portfolio!",
                "colab_url": "",
                "status": "coming_soon",
                "icon": "💾"
            }
        ]
    },
    "module3": {
        "title": "🧠 Level Up",
        "emoji": "🟠",
        "subtitle": "Go from good to GREAT",
        "duration": "Week 3",
        "color": "#f97316",
        "lessons": [
            {
                "id": "m3l1",
                "title": "Hyperparameters Decoded (Not as Scary as It Sounds)",
                "duration": "1.5 hours",
                "difficulty": "Intermediate",
                "description": "Those confusing settings? I'll explain them in plain English. You'll become a tuning wizard!",
                "colab_url": "",
                "status": "coming_soon",
                "icon": "🎛️"
            }
        ]
    }
}

# Sidebar
with st.sidebar:
    st.markdown("<div style='text-align: center; padding: 1rem;'>", unsafe_allow_html=True)
    st.markdown("# 🚀 Academy")
    st.markdown("</div>", unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=["🏠 Home", "📚 Lessons", "ℹ️ About", "☁️ Deploy"],
        icons=["house-fill", "book-fill", "info-circle-fill", "cloud-upload-fill"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "white", "font-size": "1.2rem"},
            "nav-link": {
                "font-size": "1.1rem",
                "text-align": "left",
                "margin": "0.5rem 0",
                "padding": "1rem",
                "border-radius": "10px",
                "color": "white",
                "background-color": "rgba(255, 255, 255, 0.1)",
            },
            "nav-link-selected": {
                "background": "rgba(255, 255, 255, 0.3)",
                "font-weight": "600",
            },
        }
    )

    st.markdown("<div class='spacer-small'></div>", unsafe_allow_html=True)

    # Stats
    total_lessons = sum(len(m["lessons"]) for m in LESSONS.values())
    available_lessons = sum(1 for m in LESSONS.values() for l in m["lessons"] if l["status"] == "available")

    st.markdown(f"""
    <div class='stat-box'>
        <div class='stat-number'>{available_lessons}/{total_lessons}</div>
        <div class='stat-label'>Ready to Learn</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='stat-box'>
        <div class='stat-number'>{len(LESSONS)}</div>
        <div class='stat-label'>Learning Modules</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='spacer-small'></div>", unsafe_allow_html=True)

    st.markdown("### 🔗 Quick Links")
    st.markdown("- [GitHub](https://github.com/gouthamgo/FineTuning)")
    st.markdown("- [HuggingFace](https://huggingface.co/docs)")
    st.markdown("- [Google Colab](https://colab.research.google.com/)")

# Main content
if selected == "🏠 Home":
    st.markdown('<div class="hero-title">Fine-Tuning Academy</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Learn AI Like a Friend is Teaching You</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-tags">Free • Interactive • Actually Fun • Zero BS</div>', unsafe_allow_html=True)

    st.markdown("<div class='spacer-large'></div>", unsafe_allow_html=True)

    # Feature cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🎓</div>
            <div class='feature-title'>Learn by Doing</div>
            <div class='feature-desc'>Hands-on lessons in Google Colab. Click, code, learn. No boring theory!</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-card' style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);'>
            <div class='feature-icon'>💰</div>
            <div class='feature-title'>100% Free</div>
            <div class='feature-desc'>Free GPU from Google. Free courses. Free everything. Seriously.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='feature-card' style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);'>
            <div class='feature-icon'>🤝</div>
            <div class='feature-title'>Friend Mode</div>
            <div class='feature-desc'>No jargon. No PhD needed. Just me explaining like we're friends.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='spacer-large'></div>", unsafe_allow_html=True)

    # Quick start
    st.markdown("<div class='section-header'>🚀 Start in 30 Seconds</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background: white; padding: 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);'>
        <h3 style='color: #667eea; margin-bottom: 1.5rem;'>Here's how this works:</h3>
        <ol style='font-size: 1.2rem; line-height: 2; color: #4a5568;'>
            <li><strong>Pick a lesson</strong> from below (start with the first one!)</li>
            <li><strong>Click the orange button</strong> - opens in Google Colab</li>
            <li><strong>Run the code cells</strong> - just click play ▶️</li>
            <li><strong>Learn by doing</strong> - you'll train real AI models!</li>
        </ol>
        <p style='font-size: 1.1rem; color: #718096; margin-top: 1.5rem;'>
            <strong>No installation. No setup. No credit card.</strong> Just click and learn!
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='spacer-large'></div>", unsafe_allow_html=True)

    # Featured lesson
    st.markdown("<div class='section-header'>⭐ Start Here!</div>", unsafe_allow_html=True)

    for module in LESSONS.values():
        for lesson in module["lessons"]:
            if lesson.get("featured"):
                st.markdown(f"""
                <div class='lesson-card' style='border: 3px solid #667eea;'>
                    <div style='display: flex; justify-content: space-between; align-items: start;'>
                        <div style='flex: 1;'>
                            <span class='badge badge-available'>⭐ MOST POPULAR</span>
                            <h2 style='color: #667eea; margin: 1rem 0;'>{lesson['icon']} {lesson['title']}</h2>
                            <p style='font-size: 1.2rem; color: #4a5568; line-height: 1.8; margin-bottom: 1.5rem;'>
                                {lesson['description']}
                            </p>
                            <div style='color: #718096; margin-bottom: 1.5rem;'>
                                ⏱️ {lesson['duration']} • 📊 {lesson['difficulty']}
                            </div>
                            <a href='{lesson['colab_url']}' target='_blank' class='colab-btn'>
                                🔥 Open in Colab (Free GPU!)
                            </a>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

elif selected == "📚 Lessons":
    st.markdown('<div class="hero-title" style="font-size: 3rem;">📚 All Lessons</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle" style="font-size: 1.2rem;">Your learning path from zero to hero</div>', unsafe_allow_html=True)

    st.markdown("<div class='spacer-large'></div>", unsafe_allow_html=True)

    for module_key, module in LESSONS.items():
        st.markdown(f"""
        <div class='module-header'>
            {module['emoji']} {module['title']}
            <div style='font-size: 1rem; opacity: 0.9; margin-top: 0.5rem;'>{module['subtitle']} • {module['duration']}</div>
        </div>
        """, unsafe_allow_html=True)

        for lesson in module["lessons"]:
            status_badge = "badge-available" if lesson["status"] == "available" else "badge-coming"
            status_text = "✅ Ready to Learn" if lesson["status"] == "available" else "🔜 Coming Soon"

            st.markdown(f"""
            <div class='lesson-card'>
                <div style='display: flex; justify-content: space-between; align-items: start; flex-wrap: wrap;'>
                    <div style='flex: 1; min-width: 300px;'>
                        <span class='badge {status_badge}'>{status_text}</span>
                        <h3 style='color: #2d3748; margin: 1rem 0; font-size: 1.5rem;'>
                            {lesson['icon']} {lesson['title']}
                        </h3>
                        <p style='font-size: 1.1rem; color: #4a5568; line-height: 1.8; margin-bottom: 1rem;'>
                            {lesson['description']}
                        </p>
                        <div style='color: #718096;'>
                            ⏱️ {lesson['duration']} • 📊 {lesson['difficulty']}
                        </div>
                    </div>
                    <div style='margin-top: 1rem;'>
            """, unsafe_allow_html=True)

            if lesson["status"] == "available" and lesson["colab_url"]:
                st.markdown(f"""
                        <a href='{lesson['colab_url']}' target='_blank' class='colab-btn'>
                            🚀 Start Learning
                        </a>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                        <div style='padding: 1rem 2rem; background: #e2e8f0; border-radius: 50px; color: #718096; font-weight: 600;'>
                            Coming Soon!
                        </div>
                """, unsafe_allow_html=True)

            st.markdown("""
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div class='spacer-small'></div>", unsafe_allow_html=True)

elif selected == "ℹ️ About":
    st.markdown('<div class="hero-title" style="font-size: 3rem;">ℹ️ About</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Why this exists & how it works</div>', unsafe_allow_html=True)

    st.markdown("<div class='spacer-large'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background: white; padding: 2.5rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);'>
        <h2 style='color: #667eea; margin-bottom: 1.5rem;'>The Real Talk</h2>
        <p style='font-size: 1.2rem; line-height: 2; color: #4a5568;'>
            Look, most AI tutorials suck. They're either:<br><br>
            ❌ Too technical ("assume you have a PhD")<br>
            ❌ Too expensive ("$999 for our course!")<br>
            ❌ Too boring ("here's 40 hours of lectures")<br>
            ❌ Never finish ("part 2 coming never")<br>
            <br>
            So I built this. It's:<br><br>
            ✅ Explained like I'm talking to a friend<br>
            ✅ 100% free (seriously, $0)<br>
            ✅ Actually fun to learn<br>
            ✅ Complete curriculum<br>
            ✅ You write REAL code<br>
            <br>
            <strong>This is the course I wish I had when I started.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='spacer-large'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 20px; color: white; height: 100%;'>
            <h3 style='margin-bottom: 1rem;'>🎯 What You'll Learn</h3>
            <ul style='font-size: 1.1rem; line-height: 2;'>
                <li>How AI models actually work</li>
                <li>Train your own models</li>
                <li>Build real projects</li>
                <li>Deploy to production</li>
                <li>Add to your portfolio</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 2rem; border-radius: 20px; color: white; height: 100%;'>
            <h3 style='margin-bottom: 1rem;'>💰 The Tech Stack (All Free!)</h3>
            <ul style='font-size: 1.1rem; line-height: 2;'>
                <li>Google Colab (free GPU!)</li>
                <li>HuggingFace (models & data)</li>
                <li>GitHub (hosting)</li>
                <li>Streamlit (this dashboard)</li>
            </ul>
            <p style='margin-top: 1rem; font-weight: 600;'>Total cost: $0</p>
        </div>
        """, unsafe_allow_html=True)

elif selected == "☁️ Deploy":
    st.markdown('<div class="hero-title" style="font-size: 3rem;">☁️ Deploy</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Run your own version for free</div>', unsafe_allow_html=True)

    st.markdown("<div class='spacer-large'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='background: white; padding: 2.5rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);'>
        <h2 style='color: #667eea; margin-bottom: 1.5rem;'>Deploy in 5 Minutes (Free!)</h2>

        <div style='background: #f7fafc; padding: 2rem; border-radius: 16px; margin: 1.5rem 0;'>
            <h3 style='color: #2d3748; margin-bottom: 1rem;'>Step 1: Fork the Repo</h3>
            <p style='font-size: 1.1rem; color: #4a5568; line-height: 1.8;'>
                Go to <a href='https://github.com/gouthamgo/FineTuning' target='_blank'>github.com/gouthamgo/FineTuning</a><br>
                Click "Fork" button → You now have your own copy!
            </p>
        </div>

        <div style='background: #f7fafc; padding: 2rem; border-radius: 16px; margin: 1.5rem 0;'>
            <h3 style='color: #2d3748; margin-bottom: 1rem;'>Step 2: Deploy to Streamlit</h3>
            <p style='font-size: 1.1rem; color: #4a5568; line-height: 1.8;'>
                Go to <a href='https://share.streamlit.io' target='_blank'>share.streamlit.io</a><br>
                Sign in with GitHub<br>
                Click "New app"<br>
                Select your forked repo<br>
                File: <code>webapp/app.py</code><br>
                Click "Deploy"!
            </p>
        </div>

        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 16px; margin: 1.5rem 0; color: white;'>
            <h3 style='margin-bottom: 1rem;'>🎉 That's It!</h3>
            <p style='font-size: 1.2rem; line-height: 1.8;'>
                You'll get a URL like: yourname-finetuning.streamlit.app<br><br>
                Share it with friends, students, or the world!
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<div class='spacer-large'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 2rem; background: rgba(255, 255, 255, 0.5); border-radius: 20px; margin-top: 3rem;'>
    <p style='font-size: 1.1rem; color: #4a5568; margin-bottom: 1rem;'>
        Built with ❤️ for people who want to actually learn AI
    </p>
    <p style='color: #718096;'>
        <a href='https://github.com/gouthamgo/FineTuning' target='_blank'>GitHub</a> •
        <a href='https://huggingface.co' target='_blank'>HuggingFace</a> •
        <a href='https://colab.research.google.com' target='_blank'>Google Colab</a>
    </p>
    <p style='color: #a0aec0; margin-top: 1rem; font-size: 0.9rem;'>
        100% Free • Forever • No BS
    </p>
</div>
""", unsafe_allow_html=True)
