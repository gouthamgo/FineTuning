# 🚀 Fine-Tuning Learning Platform

**Learn to Fine-Tune Transformer Models from Scratch - Interactive Jupyter Notebooks + Web Dashboard**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace-yellow)](https://huggingface.co/)

---

## 🎯 What is This?

This is a **complete, hands-on learning platform** designed for beginners who want to actually learn fine-tuning—not just read about it.

**No more tutorials that you never complete!** This platform combines:
- 📓 **Interactive Jupyter notebooks** (learn by doing)
- 📊 **Progress tracking dashboard** (see your growth)
- 🎓 **Structured curriculum** (from zero to hero)
- 💪 **Real projects** (build your portfolio)

**Perfect for:** Beginners who know Python basics but have never fine-tuned a model before.

---

## ✨ Features

- ✅ **15 Progressive Lessons** - From "What is fine-tuning?" to production deployment
- ✅ **100% Hands-On** - Write real code, train real models, see real results
- ✅ **Works Locally or Colab** - No paid API keys required
- ✅ **Beginner-Friendly** - Clear explanations, no PhD required
- ✅ **Progress Tracking** - Web dashboard shows your learning journey
- ✅ **Real Projects** - Build portfolio-worthy applications

---

## 🚀 Quick Start

### Option 1: Local Setup (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/gouthamgo/FineTuning.git
cd FineTuning

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Jupyter
jupyter lab

# 4. Open first lesson
# Navigate to: lessons/module1_foundations/01_what_is_finetuning.ipynb
```

### Option 2: Google Colab (Free GPU!)

1. Open [Google Colab](https://colab.research.google.com/)
2. Upload notebook from `lessons/` folder
3. Change runtime to GPU (Runtime → Change runtime type → GPU)
4. Start learning!

### Option 3: Launch Progress Dashboard

```bash
# Run the Streamlit dashboard
streamlit run webapp/app.py

# Opens at http://localhost:8501
```

---

## 📚 Learning Path

### 🟢 Module 1: Foundations (Week 1)
**Get comfortable with transformers and pre-trained models**

| Lesson | Topic | Duration | Status |
|--------|-------|----------|--------|
| 1.1 | What is Fine-Tuning? | 30 min | ✅ Available |
| 1.2 | Your First Model | 1 hour | ✅ Available |
| 1.3 | Understanding Data | 1 hour | 🔜 Coming Soon |

**By the end:** You'll understand fine-tuning and run inference with pre-trained models.

---

### 🟡 Module 2: Your First Fine-Tuning (Week 2)
**Actually train your first model!**

| Lesson | Topic | Duration | Status |
|--------|-------|----------|--------|
| 2.1 | First Fine-Tuning | 2 hours | ✅ Available |
| 2.2 | Evaluating Your Model | 1 hour | 🔜 Coming Soon |
| 2.3 | Saving & Sharing Models | 1 hour | 🔜 Coming Soon |

**By the end:** You'll have fine-tuned a sentiment classifier from scratch!

---

### 🟠 Module 3: Going Deeper (Week 3)
**Master hyperparameters and optimization**

- Hyperparameters Demystified
- Common Problems & Solutions
- LoRA and Efficient Fine-Tuning
- Unsloth for Speed Optimization

**By the end:** You'll know how to troubleshoot and optimize models.

---

### 🔴 Module 4: Real-World Projects (Week 4-5)
**Build portfolio projects**

Choose your path:

**Project A:** Customer Support Classifier (Multi-class)
**Project B:** Named Entity Recognition (Healthcare/Legal)
**Project C:** Custom Chatbot (Instruction Fine-Tuning)
**Project D:** Document Analyzer (Real Business Use)

**By the end:** You'll have deployable projects for your portfolio.

---

### 🟣 Module 5: Production (Week 6)
**Deploy and scale your models**

- Model Optimization (Quantization, Pruning)
- Deployment Options (API, Gradio, Docker)
- Monitoring & Iteration

**By the end:** You'll know how to put models in production.

---

## 📖 Example: What You'll Learn

**Lesson 2.1 - Your First Fine-Tuning** includes:

```python
# You'll write code like this:
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer

# Load pre-trained model
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2
)

# Prepare your data
tokenized_data = dataset.map(tokenize_function, batched=True)

# Fine-tune!
trainer = Trainer(
    model=model,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_test,
    compute_metrics=compute_metrics,
)

trainer.train()  # Watch your model learn!
```

Then you'll:
- ✅ See loss decrease in real-time
- ✅ Evaluate on test data
- ✅ Make predictions on new text
- ✅ Save your trained model
- ✅ Understand every parameter

---

## 🛠️ Requirements

### Software
- Python 3.10+
- Jupyter Lab or Google Colab
- (Optional) Streamlit for dashboard

### Hardware Options

| Option | What You Can Do | Cost |
|--------|----------------|------|
| **CPU Only** | All lessons (slow training) | Free |
| **Google Colab Free** | All lessons with GPU | Free |
| **Local GPU (8GB+)** | Fast training, all projects | Hardware cost |

**Recommendation:** Start with Google Colab (free GPU), then move to local if needed.

---

## 📁 Repository Structure

```
FineTuning/
├── lessons/                    # Interactive Jupyter notebooks
│   ├── module1_foundations/    # Week 1: Basics
│   ├── module2_first_training/ # Week 2: First model
│   ├── module3_going_deeper/   # Week 3: Advanced
│   ├── module4_projects/       # Week 4-5: Real projects
│   └── module5_production/     # Week 6: Deployment
├── webapp/                     # Progress tracking dashboard
│   └── app.py                 # Streamlit app
├── datasets/                   # Sample datasets
├── utils/                      # Helper functions
│   └── helpers.py             # Visualization, metrics, etc.
├── projects/                   # Project templates
│   ├── sentiment_analyzer/
│   ├── ner_extractor/
│   └── chatbot/
├── requirements.txt            # All dependencies
├── README.md                   # This file
├── unsloth.md                 # Optimization guide
└── usecases.md                # Project ideas
```

---

## 🎓 Learning Philosophy

This platform is built on these principles:

1. **Learn by Doing** - Every concept has runnable code
2. **Progressive Complexity** - Start simple, build up gradually
3. **Real Projects** - Build things you can show employers
4. **No Black Boxes** - Understand what's happening under the hood
5. **Practical Focus** - Skills you'll actually use

---

## 🌟 Why This Platform?

### ❌ What This Is NOT:
- Another theory-heavy tutorial you never finish
- A list of code snippets without context
- Outdated examples that don't work anymore
- Assumes you have a PhD in ML

### ✅ What This IS:
- A complete curriculum from zero to deployment
- Hands-on notebooks you can run immediately
- Up-to-date with latest HuggingFace best practices
- Designed for beginners who want to actually DO it

---

## 🎯 Learning Outcomes

After completing this platform, you will:

- ✅ Understand transformer architecture fundamentals
- ✅ Fine-tune models for any classification task
- ✅ Build custom NER systems
- ✅ Optimize models for production (LoRA, quantization)
- ✅ Deploy models as APIs or web apps
- ✅ Troubleshoot common issues confidently
- ✅ Have 2-4 portfolio projects to show employers

---

## 📊 Progress Tracking

Launch the dashboard to track your journey:

```bash
streamlit run webapp/app.py
```

Features:
- See which lessons you've completed
- Track overall progress percentage
- Quick links to each notebook
- Motivational milestones

---

## 🤝 Contributing

This is an educational project, and contributions are welcome!

**Ways to contribute:**
- Report issues or bugs in lessons
- Suggest new projects or use cases
- Improve explanations or code examples
- Add new lessons or modules
- Share your success stories!

Open an issue or submit a PR on GitHub.

---

## 💬 Getting Help

Stuck on a lesson? Have questions?

1. **Check the FAQ** in each notebook
2. **Review the troubleshooting section** in Module 3
3. **Open an issue** on GitHub with your question
4. **Join the discussion** in GitHub Discussions

---

## 📜 License

MIT License - Free to use for learning and commercial projects.

---

## 🙏 Acknowledgments

Built with:
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/)
- [HuggingFace Datasets](https://huggingface.co/docs/datasets/)
- [PyTorch](https://pytorch.org/)
- [Streamlit](https://streamlit.io/)

Inspired by the amazing ML community and all the learners who want to go from reading about AI to actually building it.

---

## 🚀 Ready to Start?

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Open your first lesson
jupyter lab lessons/module1_foundations/01_what_is_finetuning.ipynb

# 3. Start learning!
```

**Let's turn you from a beginner into a confident fine-tuner! 💪**

---

---

# 📖 Reference: Quick Fine-Tuning Guide

*The content below is a quick reference guide for experienced users. If you're a beginner, start with the interactive lessons above!*

---

## What is Fine-Tuning?

Fine-tuning takes a pre-trained model (like BERT) that already understands language and teaches it your specific task with your data.

**Pre-trained model** → **Your specific data** → **Specialized model**

## When Do You Need It?

### ✅ Fine-tune when:
- You have domain-specific language (legal, medical, technical)
- You need custom categories not covered by existing models
- You have 500+ labeled examples
- Accuracy really matters for your use case

### ❌ Skip fine-tuning if:
- Zero-shot classification works well enough
- You have < 100 examples
- Your task is generic (sentiment analysis, basic NER)
- You're just experimenting

## Quick Start Code

### Installation
```bash
pip install transformers datasets torch accelerate evaluate
```

### Basic Training Script

```python
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    TrainingArguments, Trainer
)
from datasets import Dataset
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

# Load your data
df = pd.read_csv('training_data.csv')  # Columns: 'text', 'label'
labels = df['label'].unique()
label2id = {label: i for i, label in enumerate(labels)}
df['labels'] = df['label'].map(label2id)

# Load model and tokenizer
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=len(labels)
)

# Tokenize
def tokenize_function(examples):
    return tokenizer(examples['text'], truncation=True, padding=True, max_length=512)

dataset = Dataset.from_pandas(df)
tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Split data
train_size = int(0.8 * len(tokenized_dataset))
train_dataset = tokenized_dataset.select(range(train_size))
eval_dataset = tokenized_dataset.select(range(train_size, len(tokenized_dataset)))

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

trainer.train()
trainer.save_model('./my_model')
```

### Using Your Model

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="./my_model")
result = classifier("Your text here")
print(result)
```

## Model Selection Guide

**For Text Classification:**
- `distilbert-base-uncased` - Fast, good for most cases
- `bert-base-uncased` - More accurate, standard choice
- `roberta-base` - Often outperforms BERT

**For Named Entity Recognition:**
- `bert-base-cased` - Capitalization matters
- `distilbert-base-cased` - Faster alternative

## Common Issues

### Out of Memory
```python
per_device_train_batch_size=8  # Reduce batch size
gradient_accumulation_steps=2   # Accumulate gradients
```

### Poor Performance
- Check data quality and balance
- Try different learning rates (1e-5, 2e-5, 5e-5)
- Increase training epochs
- Use more training data

## Resources

- [HuggingFace Documentation](https://huggingface.co/docs/transformers/)
- [HuggingFace Course](https://huggingface.co/course/)
- [Model Hub](https://huggingface.co/models)

---

**Happy Fine-Tuning! 🚀**
