"""
Helper utilities for fine-tuning lessons
"""

import torch
import numpy as np
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report


def print_model_info(model):
    """Print detailed information about a model."""
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

    print("=" * 60)
    print("MODEL INFORMATION")
    print("=" * 60)
    print(f"Model type: {model.__class__.__name__}")
    print(f"Total parameters: {total_params:,}")
    print(f"Trainable parameters: {trainable_params:,}")
    print(f"Non-trainable parameters: {total_params - trainable_params:,}")
    print(f"Model size (MB): {total_params * 4 / 1024 / 1024:.2f}")
    print("=" * 60)


def print_dataset_info(dataset):
    """Print information about a dataset."""
    print("=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)
    print(f"Number of examples: {len(dataset)}")
    print(f"Features: {list(dataset.features.keys())}")

    # Check for label distribution if labels exist
    if 'label' in dataset.features:
        labels = [example['label'] for example in dataset]
        unique_labels = set(labels)
        print(f"\nLabel distribution:")
        for label in sorted(unique_labels):
            count = labels.count(label)
            pct = (count / len(labels)) * 100
            print(f"  Label {label}: {count} ({pct:.1f}%)")

    print("=" * 60)


def plot_training_history(training_logs: List[Dict]):
    """Plot training and validation metrics over time."""
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Extract metrics
    train_loss = [log['loss'] for log in training_logs if 'loss' in log]
    eval_loss = [log['eval_loss'] for log in training_logs if 'eval_loss' in log]

    # Plot loss
    axes[0].plot(train_loss, label='Training Loss', marker='o')
    if eval_loss:
        axes[0].plot(eval_loss, label='Validation Loss', marker='s')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].set_title('Training and Validation Loss')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Plot accuracy if available
    if any('eval_accuracy' in log for log in training_logs):
        eval_accuracy = [log['eval_accuracy'] for log in training_logs if 'eval_accuracy' in log]
        axes[1].plot(eval_accuracy, label='Validation Accuracy', marker='s', color='green')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Accuracy')
        axes[1].set_title('Validation Accuracy')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def plot_confusion_matrix(y_true: List[int], y_pred: List[int], labels: List[str] = None):
    """Plot a confusion matrix."""
    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=labels or range(len(cm)),
                yticklabels=labels or range(len(cm)))
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

    return cm


def analyze_predictions(y_true: List[int], y_pred: List[int],
                       texts: List[str] = None, labels: List[str] = None):
    """Analyze model predictions and show classification report."""
    print("=" * 60)
    print("CLASSIFICATION REPORT")
    print("=" * 60)
    print(classification_report(y_true, y_pred, target_names=labels))
    print("=" * 60)

    # Show some misclassified examples if texts provided
    if texts:
        misclassified = [(i, texts[i], y_true[i], y_pred[i])
                        for i in range(len(texts))
                        if y_true[i] != y_pred[i]]

        if misclassified:
            print(f"\nSample Misclassified Examples (showing up to 5):\n")
            for idx, text, true_label, pred_label in misclassified[:5]:
                label_names = labels or ["Label"]
                true_name = label_names[true_label] if labels else true_label
                pred_name = label_names[pred_label] if labels else pred_label
                print(f"Example {idx}:")
                print(f"  Text: {text[:100]}...")
                print(f"  True: {true_name} | Predicted: {pred_name}\n")


def calculate_model_metrics(predictions: np.ndarray, labels: np.ndarray) -> Dict:
    """Calculate various metrics for model evaluation."""
    from sklearn.metrics import accuracy_score, precision_recall_fscore_support

    preds = np.argmax(predictions, axis=1)

    accuracy = accuracy_score(labels, preds)
    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, preds, average='weighted'
    )

    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }


def predict_with_model(text: str, model, tokenizer, device='cpu'):
    """Make a prediction on a single text."""
    # Tokenize
    inputs = tokenizer(text, return_tensors="pt", truncation=True,
                      padding=True, max_length=512)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Predict
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)

    # Get probabilities
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    prediction = torch.argmax(probabilities, dim=-1).item()
    confidence = probabilities[0][prediction].item()

    return prediction, confidence, probabilities[0].cpu().numpy()


def batch_predict(texts: List[str], model, tokenizer, batch_size=16, device='cpu'):
    """Make predictions on a batch of texts."""
    all_predictions = []
    all_confidences = []

    model.eval()

    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]

        # Tokenize
        inputs = tokenizer(batch_texts, return_tensors="pt", truncation=True,
                         padding=True, max_length=512)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        # Predict
        with torch.no_grad():
            outputs = model(**inputs)

        # Get probabilities
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predictions = torch.argmax(probabilities, dim=-1)
        confidences = probabilities.gather(1, predictions.unsqueeze(1)).squeeze()

        all_predictions.extend(predictions.cpu().numpy())
        all_confidences.extend(confidences.cpu().numpy())

    return all_predictions, all_confidences


def check_gpu_availability():
    """Check and print GPU availability information."""
    print("=" * 60)
    print("HARDWARE INFORMATION")
    print("=" * 60)

    if torch.cuda.is_available():
        print(f"✅ CUDA is available!")
        print(f"GPU Device: {torch.cuda.get_device_name(0)}")
        print(f"Number of GPUs: {torch.cuda.device_count()}")
        print(f"CUDA Version: {torch.version.cuda}")

        # Memory info
        total_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
        print(f"GPU Memory: {total_memory:.2f} GB")
    else:
        print("⚠️  CUDA is not available. Using CPU.")
        print("Training will be slower. Consider using Google Colab for free GPU access.")

    print("=" * 60)


def estimate_training_time(num_samples: int, batch_size: int, num_epochs: int,
                          samples_per_second: float = 10):
    """Estimate training time."""
    steps_per_epoch = num_samples // batch_size
    total_steps = steps_per_epoch * num_epochs
    estimated_seconds = total_steps * (batch_size / samples_per_second)

    minutes = estimated_seconds // 60
    seconds = estimated_seconds % 60

    print(f"Estimated training time: {int(minutes)} minutes, {int(seconds)} seconds")
    print(f"(This is a rough estimate. Actual time may vary)")


def save_model_card(model_name: str, task: str, metrics: Dict, save_path: str):
    """Generate a model card README."""
    card = f"""# {model_name}

## Model Description

Fine-tuned model for {task}.

## Training Details

- Base Model: {model_name}
- Task: {task}
- Framework: HuggingFace Transformers

## Performance

| Metric | Score |
|--------|-------|
| Accuracy | {metrics.get('accuracy', 'N/A'):.4f} |
| Precision | {metrics.get('precision', 'N/A'):.4f} |
| Recall | {metrics.get('recall', 'N/A'):.4f} |
| F1 Score | {metrics.get('f1', 'N/A'):.4f} |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("{save_path}")
model = AutoModelForSequenceClassification.from_pretrained("{save_path}")

# Make predictions
text = "Your text here"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
```

## Training Data

[Describe your training data here]

## Limitations

[Describe any limitations or biases]
"""

    with open(f"{save_path}/README.md", 'w') as f:
        f.write(card)

    print(f"✅ Model card saved to {save_path}/README.md")
