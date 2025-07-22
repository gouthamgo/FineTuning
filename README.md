# 🚀 Fine-Tuning Transformer Models: Complete Beginner's Guide

A practical, no-nonsense guide to fine-tuning transformer models locally with HuggingFace. Perfect for getting started with custom text classification, NER, and more.

## 📋 Table of Contents
- [What is Fine-Tuning?](#what-is-fine-tuning)
- [When Do You Need It?](#when-do-you-need-it)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Basic Example](#basic-example)
- [Advanced Tips](#advanced-tips)
- [Common Issues](#common-issues)
- [Resources](#resources)

## What is Fine-Tuning?

Fine-tuning takes a pre-trained model (like BERT) that already understands language and teaches it your specific task with your data.

**Pre-trained model** → **Your specific data** → **Specialized model**

Think of it like hiring someone who already speaks English fluently and training them to be a lawyer, doctor, or engineer.

## When Do You Need It?

### ❌ Skip fine-tuning if:
- Zero-shot classification works well enough
- You have < 100 examples
- Your task is generic (sentiment analysis, basic NER)
- You're just starting out

### ✅ Fine-tune when:
- You have domain-specific language (legal, medical, technical)
- You need custom categories not covered by existing models
- You have 1000+ labeled examples
- Accuracy really matters for your use case

## Quick Start

```bash
git clone https://github.com/yourusername/finetuning-guide
cd finetuning-guide
pip install -r requirements.txt
python examples/basic_classification.py
```

## Installation

## Installation

### Basic Setup
```bash
pip install transformers datasets torch accelerate evaluate
```

### GPU Support (Recommended)
```bash
# For CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### Optional Extras
```bash
pip install wandb tensorboard  # For tracking experiments
```

### Hardware Requirements

| Setup | What You Can Train | Speed |
|-------|-------------------|-------|
| CPU Only | DistilBERT, small models | Slow but works |
| GPU 8GB+ | BERT-base, most classification | Good |
| GPU 16GB+ | BERT-large, small generative | Great |
| Multiple GPUs | Large models, faster training | Excellent |

## Basic Example

### 1. Prepare Your Data

Create a CSV file with your training data:

```python
import pandas as pd

# Your data should look like this
df = pd.DataFrame({
    'text': [
        'This software license agreement covers usage rights',
        'Patient shows normal vital signs and recovery',
        'Quarterly revenue increased by 15% this period'
    ],
    'label': ['legal', 'medical', 'financial']
})

df.to_csv('training_data.csv', index=False)
```

### 2. Basic Training Script

```python
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    TrainingArguments, Trainer, DataCollatorWithPadding
)
from datasets import Dataset, load_dataset
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv('training_data.csv')
labels = df['label'].unique()
label2id = {label: i for i, label in enumerate(labels)}
id2label = {i: label for label, i in label2id.items()}

# Add numeric labels
df['labels'] = df['label'].map(label2id)

# Load model and tokenizer
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, 
    num_labels=len(labels),
    id2label=id2label,
    label2id=label2id
)

# Tokenize function
def tokenize_function(examples):
    return tokenizer(examples['text'], truncation=True, padding=True, max_length=512)

# Create dataset
dataset = Dataset.from_pandas(df)
tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Split data
train_size = int(0.8 * len(tokenized_dataset))
train_dataset = tokenized_dataset.select(range(train_size))
eval_dataset = tokenized_dataset.select(range(train_size, len(tokenized_dataset)))

# Metrics function
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return {'accuracy': accuracy_score(labels, predictions)}

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    greater_is_better=True,
)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    tokenizer=tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
    compute_metrics=compute_metrics,
)

# Train
trainer.train()

# Save model
trainer.save_model('./fine_tuned_model')
tokenizer.save_pretrained('./fine_tuned_model')
```

### 3. Using Your Fine-Tuned Model

```python
from transformers import pipeline

# Load your trained model
classifier = pipeline(
    "text-classification",
    model="./fine_tuned_model",
    tokenizer="./fine_tuned_model"
)

# Test it
result = classifier("This contract needs legal review before signing")
print(f"Label: {result[0]['label']}, Confidence: {result[0]['score']:.3f}")
```

## Advanced Tips

### Model Selection Guide

**For Text Classification:**
- `distilbert-base-uncased` - Fast, good for most cases
- `bert-base-uncased` - More accurate, standard choice
- `roberta-base` - Often outperforms BERT
- `electra-base-discriminator` - Very efficient

**For Named Entity Recognition:**
- `bert-base-cased` - Capitalization matters for NER
- `distilbert-base-cased` - Faster alternative
- `roberta-base` - Strong performance

**For Text Generation:**
- `gpt2` - Good starting point
- `microsoft/DialoGPT-small` - For conversational tasks
- `google/flan-t5-base` - Instruction following

### Hyperparameter Tuning

```python
# Conservative settings (good starting point)
training_args = TrainingArguments(
    learning_rate=2e-5,
    num_train_epochs=3,
    per_device_train_batch_size=16,
    warmup_steps=500,
    weight_decay=0.01,
)

# Aggressive settings (when you have lots of data)
training_args = TrainingArguments(
    learning_rate=5e-5,
    num_train_epochs=5,
    per_device_train_batch_size=32,
    warmup_steps=1000,
    weight_decay=0.1,
)
```

### Data Quality Tips

1. **Balance your classes** - Don't have 1000 examples of one label and 10 of another
2. **Clean your text** - Remove weird characters, normalize spacing
3. **Validate your labels** - Double-check a sample of your annotations
4. **Test on unseen data** - Always hold out data the model hasn't seen

## Common Issues

### Out of Memory Errors
```python
# Reduce batch size
per_device_train_batch_size=8  # Instead of 16

# Use gradient accumulation
gradient_accumulation_steps=2

# Use a smaller model
model_name = "distilbert-base-uncased"  # Instead of bert-large
```

### Poor Performance
- Check your data quality first
- Make sure you have enough examples per class (minimum 100, prefer 1000+)
- Try different learning rates (1e-5, 2e-5, 5e-5)
- Increase training epochs if training loss is still decreasing

### Model Not Learning
- Verify your labels are correct
- Check if the task is actually learnable
- Try a different base model
- Increase learning rate slightly

## Example Projects

Check the `examples/` folder for complete implementations:

- `text_classification.py` - Basic document classification
- `named_entity_recognition.py` - Custom NER training
- `sentiment_analysis.py` - Domain-specific sentiment
- `pdf_tagger.py` - Smart PDF content tagging

## Resources

### Official Documentation
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/)
- [HuggingFace Datasets](https://huggingface.co/docs/datasets/)

### Model Hubs
- [HuggingFace Model Hub](https://huggingface.co/models)
- [Pre-trained Models by Task](https://huggingface.co/models?pipeline_tag=text-classification)

### Learning Materials
- [HuggingFace Course](https://huggingface.co/course/)
- [Fine-tuning Tutorial](https://huggingface.co/docs/transformers/training)

## Contributing

Found an issue? Have a suggestion? Please open an issue or submit a pull request!

## License

MIT License - feel free to use this code for your projects.

---

