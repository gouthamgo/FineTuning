# Sample Datasets

This directory contains sample datasets for practicing fine-tuning.

## Available Datasets

### 1. sample_sentiment.csv
- **Task:** Sentiment classification (positive/negative)
- **Size:** 1,000 examples
- **Format:** CSV with columns: `text`, `label`
- **Use in:** Module 2 - First Fine-tuning

### 2. customer_support.csv (Coming Soon)
- **Task:** Multi-class classification
- **Categories:** urgent, billing, technical, general
- **Size:** 2,000 examples

### 3. ner_dataset.json (Coming Soon)
- **Task:** Named Entity Recognition
- **Entities:** PERSON, ORG, LOC, DATE
- **Size:** 1,500 examples

## Data Format

### Sentiment Analysis
```csv
text,label
"This is great!",1
"This is terrible.",0
```

### Multi-class Classification
```csv
text,category
"My account is locked",technical
"I was charged twice",billing
```

### NER (JSON)
```json
{
  "text": "John works at Apple in California",
  "entities": [
    {"text": "John", "label": "PERSON", "start": 0, "end": 4},
    {"text": "Apple", "label": "ORG", "start": 14, "end": 19}
  ]
}
```

## Using HuggingFace Datasets

Instead of local files, you can also use datasets from HuggingFace Hub:

```python
from datasets import load_dataset

# Load popular datasets
dataset = load_dataset("imdb")  # Movie reviews
dataset = load_dataset("ag_news")  # News classification
dataset = load_dataset("conll2003")  # NER
dataset = load_dataset("squad")  # Question answering
```

## Creating Your Own Dataset

For best results:

1. **Collect 500-10,000 labeled examples**
2. **Ensure balanced classes** (roughly equal examples per category)
3. **Clean your data** (remove duplicates, fix typos)
4. **Split properly** (70% train, 15% validation, 15% test)
5. **Document your data** (where it came from, any biases)

## Data Quality Checklist

- [ ] No duplicate examples
- [ ] Balanced class distribution (within 20%)
- [ ] Consistent labeling (no conflicting labels)
- [ ] Appropriate length (not too short or long)
- [ ] Representative of real-world data
- [ ] Privacy compliant (no PII if public)

## Licensing

Sample datasets in this repository are for educational purposes only.
Always check the license before using external datasets.
