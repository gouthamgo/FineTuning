# 🚀 Deployment Guide

This guide shows you how to deploy the Fine-Tuning Learning Platform for **FREE**.

---

## 🎯 Architecture Overview

Our platform is 100% free and requires no backend infrastructure:

```
┌─────────────────┐
│  GitHub         │  Hosts notebooks (free)
│  (Source Code)  │
└────────┬────────┘
         │
         ├──────────────┐
         │              │
┌────────▼────────┐  ┌──▼──────────────┐
│ Google Colab    │  │ Streamlit Cloud │
│ (Notebooks)     │  │ (Dashboard)     │
│ Free GPU!       │  │ Free hosting!   │
└─────────────────┘  └─────────────────┘
         │                    │
         └──────────┬─────────┘
                    │
              ┌─────▼──────┐
              │   Users    │
              │  (Learners)│
              └────────────┘
```

**Cost: $0** 💰

---

## 📦 What Gets Deployed

### 1. **Jupyter Notebooks** (via GitHub → Colab)
- Hosted on GitHub (free)
- Students open directly in Google Colab
- Free GPU access from Colab

### 2. **Streamlit Dashboard** (via Streamlit Cloud)
- Hosted on Streamlit Cloud (free tier)
- Public URL provided
- No database needed (uses static lesson data)

---

## 🌐 Option 1: Deploy Dashboard to Streamlit Cloud (Recommended)

### Prerequisites
- GitHub account (free)
- Streamlit Cloud account (free - sign in with GitHub)

### Step-by-Step

#### 1. Fork the Repository

```bash
# Go to: https://github.com/gouthamgo/FineTuning
# Click "Fork" button in top right
# This creates your own copy
```

#### 2. Sign Up for Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Continue with GitHub"
3. Authorize Streamlit to access your GitHub

#### 3. Deploy Your App

1. Click "New app" button
2. Fill in deployment settings:
   - **Repository:** `your-username/FineTuning`
   - **Branch:** `main`
   - **Main file path:** `webapp/app.py`
   - **App URL:** Choose a custom URL (e.g., `my-finetuning-platform`)

3. Click "Deploy"!

#### 4. Wait ~2 Minutes

Streamlit will:
- Clone your repo
- Install dependencies
- Launch the app
- Give you a public URL

#### 5. Share Your Platform!

Your URL will be: `https://your-app-name.streamlit.app`

Share it with:
- Students
- Colleagues
- Social media
- The world!

---

## 💻 Option 2: Run Locally

Perfect for development or testing.

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/gouthamgo/FineTuning.git
cd FineTuning

# Install dependencies
pip install streamlit streamlit-option-menu

# Run the dashboard
streamlit run webapp/app.py
```

Opens at: `http://localhost:8501`

---

## 🎨 Customization

### Change Branding

Edit `webapp/app.py`:

```python
# Line 11-14
st.set_page_config(
    page_title="Your Custom Title",  # Change this
    page_icon="🎓",  # Change this emoji
    ...
)
```

### Add More Lessons

Edit the `LESSONS` dictionary in `webapp/app.py`:

```python
{
    "id": "m1l4",
    "title": "Your New Lesson",
    "duration": "1 hour",
    "difficulty": "Beginner",
    "description": "What this lesson teaches",
    "colab_url": "https://colab.research.google.com/github/...",
    "status": "available"  # or "coming_soon"
}
```

### Custom Domain (Streamlit Cloud)

1. Go to your Streamlit app settings
2. Click "Custom domain"
3. Add CNAME record:
   ```
   learn.yourdomain.com  CNAME  your-app.streamlit.app
   ```

---

## 🔧 Troubleshooting

### Dashboard Not Loading

**Issue:** App shows errors on Streamlit Cloud

**Solution:**
1. Check `requirements.txt` includes:
   ```
   streamlit>=1.28.0
   streamlit-option-menu>=0.3.6
   ```
2. Redeploy the app

### Colab Links Not Working

**Issue:** "Open in Colab" buttons give 404

**Solution:**
1. Ensure notebooks are in your `main` branch
2. Check GitHub repo is public
3. Verify file paths in Colab URLs

### Local Development Issues

**Issue:** `streamlit: command not found`

**Solution:**
```bash
pip install streamlit streamlit-option-menu
```

**Issue:** Port already in use

**Solution:**
```bash
streamlit run webapp/app.py --server.port 8502
```

---

## 📊 Monitoring & Analytics (Optional)

Want to see how many people use your platform?

### Add Google Analytics

1. Get tracking ID from Google Analytics
2. Edit `webapp/app.py`:

```python
# Add after st.set_page_config()
st.markdown(f"""
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
""", unsafe_allow_html=True)
```

### Streamlit Analytics (Built-in)

Streamlit Cloud provides basic analytics:
- Page views
- Unique visitors
- Session duration

Access at: `https://share.streamlit.io/your-app/analytics`

---

## 🔐 Security & Privacy

### No User Data Collected

This platform:
- ✅ No login required
- ✅ No database
- ✅ No cookies
- ✅ No tracking (unless you add it)
- ✅ No personal data

### Notebooks Run in User's Colab

- Students run code in their own Colab environment
- You don't see their code or data
- Completely isolated

### Making Repo Private

If you want a private platform:

1. Make GitHub repo private
2. Share Colab links directly (they still work for authorized users)
3. Deploy dashboard to Streamlit Cloud (still works)

**Note:** Free Streamlit Cloud requires public repos. For private repos, consider local hosting.

---

## 🚀 Performance

### Streamlit Cloud Limits (Free Tier)

- **RAM:** 1 GB per app
- **CPU:** Shared
- **Uptime:** App sleeps after inactivity
- **Wake time:** ~10 seconds

**This is fine for our dashboard!** (Static content, no heavy compute)

### Optimizations

If your dashboard is slow:

1. **Reduce images/media** in the app
2. **Use caching:**
   ```python
   @st.cache_data
   def load_lesson_data():
       return LESSONS
   ```
3. **Lazy load** heavy content

---

## 🔄 Updates & Maintenance

### Updating Lessons

1. Add new notebook to `lessons/` folder
2. Commit and push to GitHub
3. Update `LESSONS` dict in `webapp/app.py`
4. Streamlit Cloud auto-redeploys (takes ~1 min)

### Auto-Deployment

Streamlit Cloud watches your GitHub repo:
- Every push to `main` triggers redeploy
- Takes 1-2 minutes
- Zero downtime

### Manual Redeploy

If needed:
1. Go to share.streamlit.io
2. Click on your app
3. Click "Reboot app"

---

## 📈 Scaling

### Current Architecture
- **Supports:** Unlimited concurrent users
- **Cost:** $0
- **Limitations:** Streamlit Cloud free tier limits

### If You Outgrow Free Tier

**More users?**
- Upgrade to Streamlit Cloud paid tier ($20/month)
- OR self-host on AWS/GCP/Heroku

**More compute?**
- Dashboard is lightweight (just displays lessons)
- Actual compute happens in student's Colab
- You don't need more resources!

---

## ✅ Deployment Checklist

Before going public:

- [ ] Notebooks have Colab badges
- [ ] All Colab links tested and working
- [ ] README updated with your info
- [ ] GitHub repo is public (if using free Streamlit)
- [ ] Dashboard deployed to Streamlit Cloud
- [ ] Custom domain configured (optional)
- [ ] Tested on mobile devices
- [ ] Added to social media/portfolio

---

## 🆘 Need Help?

**Streamlit Issues:**
- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Community](https://discuss.streamlit.io)

**GitHub Issues:**
- [FineTuning Issues](https://github.com/gouthamgo/FineTuning/issues)

**General Questions:**
- Open a GitHub Discussion
- DM on Twitter/LinkedIn

---

## 🎉 You're Live!

Congratulations! You now have a free, public learning platform.

**Share your platform:**
- Twitter/X
- LinkedIn
- Reddit (r/MachineLearning)
- HackerNews
- Dev.to

**Next steps:**
- Add more lessons
- Get feedback from learners
- Build a community
- Help others learn!

---

**Built with ❤️ • Always Free • Open Source**
