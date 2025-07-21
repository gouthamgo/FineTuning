<br/>
<p align="center">
  <img src="https://i.imgur.com/OAbOU37.png" alt="FineTuning Logo" width="150"/>
</p>

<h1 align="center">The Self-Study Guide to Efficient LLM Fine-Tuning</h1>

<p align="center">
  This document is both a guide and a library. It will teach you the core concepts of modern, parameter-efficient fine-tuning (PEFT) and provide you with the tools to apply them, powered by the <strong>FineTuning Toolkit</strong>.
  <br/>
  <br/>
  <a href="#"><strong>Explore Advanced Docs »</strong></a>
  <br/>
  <br/>
  <a href="#">Report a Bug</a>
  ·
  <a href="#">Ask a Question</a>
</p>

<p align="center">
    <img src="https://img.shields.io/pypi/v/finetuning-toolkit.svg?color=blue" alt="PyPI Version">
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version">
    <img src="https://img.shields.io/badge/license-Apache_2.0-blue.svg" alt="License">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

---

Welcome! If you're here, you're curious about how to adapt powerful Large Language Models (LLMs) like Llama or Mistral for your specific tasks without needing a server farm. You're in the right place.

This guide is structured in three parts:
1.  **The "Why":** We'll learn the core theory behind fine-tuning and LoRA, using simple analogies.
2.  **The "How":** A hands-on walkthrough where you'll fine-tune your first model using this toolkit.
3.  **The "What's Next":** We'll explore advanced techniques and how to choose the right tool for the job.

## Part 1: The Core Concepts (The "Why")

### First, Why Fine-Tune?

Imagine you have a brilliant, general-purpose AI assistant (a base LLM). It knows about history, science, and can write poetry. But it knows nothing about your company's internal documents or your specific product's support policies.

**Fine-tuning** is the process of taking this generalist model and training it a little more on your specific data. The goal is to make it an expert in *your* domain.

### The Problem with "Full" Fine-Tuning

The traditional way to do this was **full fine-tuning**. This means updating *every single one* of the model's billions of parameters.

*   🧠 **Analogy:** It's like re-educating the entire expert, modifying their entire brain.
*   💰 **The Cost:** This requires immense computational power (many high-end GPUs), a lot of VRAM, and each time you create a specialized model, you have to save a full multi-billion parameter copy. It's slow, expensive, and inefficient.

### The Solution: Parameter-Efficient Fine-Tuning (PEFT)

PEFT techniques take a much smarter approach. Instead of modifying the original model, they **freeze it** and insert a few, tiny, new layers to train.

*   🧠 **Analogy:** Instead of re-educating the expert, you give them a small, magical "notebook" and a pen. The expert's original knowledge remains untouched. You only train the contents of the notebook. This notebook contains all the task-specific information.

This is revolutionary because we now only need to train and save the "notebook," which is a tiny fraction (~0.01%) of the full model's size!

### Meet LoRA: The Most Popular "Notebook"

**LoRA (Low-Rank Adaptation)** is the most popular PEFT method. It works on a simple but powerful principle from linear algebra.

Any large change to the model's weights (a big matrix, `ΔW`) can be efficiently approximated by two much, much smaller matrices (`A` and `B`). So, instead of training the giant `ΔW`, LoRA creates these two small "adapter" matrices and only trains them.

This is the "notebook." It's incredibly efficient.

## Part 2: Your First Fine-Tuning Journey (The "How")

Let's get our hands dirty. We'll use the `FineTuning` toolkit to apply LoRA to a real model.

### Step 1: Installation

First, let's get the necessary tools. You'll need `PyTorch`, `transformers` for the models, and our toolkit.

```bash
pip install torch transformers finetuning-toolkit

Step 2: A Step-by-Step LoRA Fine-Tune

Let's walk through the code. The comments explain each part of the process.

Generated python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from finetuning_toolkit import FineTuningConfig, FineTuningModel

# --- 1. Load the "Generalist Expert" ---
# We load a pre-trained model from the Hugging Face Hub.
# This model is our frozen, base knowledge.
# `device_map="auto"` intelligently places the model across your available GPUs.
model_name = "meta-llama/Llama-2-7b-chat-hf"
base_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# --- 2. Create the LoRA "Notebook" Configuration ---
# This is where we define the properties of our LoRA adapter.
config = FineTuningConfig(
    method="lora", # We specify we're using the standard LoRA method.

    # -- Key LoRA Hyperparameters --
    # `r`: The rank, or the "capacity" of our notebook. A higher `r` means more
    # parameters and more expressive power, but at the cost of size.
    # Good starting values are 8, 16, 32.
    lora_r=16,

    # `alpha`: The scaling factor. It controls how much we trust the notebook's
    # knowledge over the expert's. A common rule of thumb is `alpha = 2 * r`.
    lora_alpha=32,

    # `dropout`: A regularization technique to prevent overfitting.
    lora_dropout=0.05,

    # `target_modules`: This is crucial. We tell LoRA which parts of the model's
    # "brain" (layers) to attach the notebooks to. The attention mechanism's
    # query (q) and value (v) projections are almost always the best choice.
    target_modules=["q_proj", "v_proj"]
)

# --- 3. Attach the Notebook to the Expert ---
# We create the final, trainable model by wrapping our base model with the config.
# Our toolkit handles all the complex work of injecting the LoRA layers.
model = FineTuningModel(base_model, config)

# Let's see the magic! This function shows how few parameters we're actually training.
model.print_trainable_parameters()
# Output: trainable params: 4,194,304 || all params: 6,742,609,920 || trainable%: 0.0622
# Notice we're training less than 0.1% of the model!

# --- 4. Start Training ---
# Now, you would run your standard PyTorch training loop.
# You feed your dataset to `model` and use an optimizer.
#
# for batch in your_dataset:
#   outputs = model(**batch)
#   loss = outputs.loss
#   loss.backward()
#   optimizer.step()
#   optimizer.zero_grad()
#
# This part is standard machine learning, so we'll skip the boilerplate.

# --- 5. Save Your "Notebook" ---
# After training, you don't save the whole 7B parameter model.
# You only save the lightweight adapter you trained.
model.save_adapter("./my-first-llama-adapter")

# This saved directory is just a few megabytes, easy to share and deploy!

Congratulations! You've just conceptually completed your first parameter-efficient fine-tune. You now understand the core workflow.

Part 3: Exploring the LoRA Zoo (What's Next?)

LoRA was a breakthrough, but the research didn't stop there. Scientists have developed variants that are even more efficient or solve specific problems. Our toolkit makes it trivial to experiment with them.

Why do these variants exist? To be even faster, use less memory, or generalize better.

Here is a quick guide to the methods included in this toolkit:

Method	Description	Use This When...
LoRA	Standard Low-Rank Adaptation. The industry-standard for efficient fine-tuning.	You want a reliable, well-understood baseline. Always start here.
VERA	Vector-based Random Adapters. A hyper-efficient variant that uses one shared low-rank matrix.	You are severely memory-constrained (VRAM) and need the fastest training possible.
LoRA+	An enhanced version of LoRA that uses different learning rates for its adapter matrices for improved stability.	Your training with standard LoRA is unstable or not converging well.
Delta-LoRA	A delta-based approach that improves efficiency by learning and applying only the changes to weights.	You're doing iterative fine-tuning or need to minimize memory usage at all costs.
LoRA-FA	Feature-safe extension of LoRA adapted for specific transformer layers to prevent catastrophic forgetting.	Your model must not lose its original capabilities after fine-tuning.
Experimenting is Easy!

Want to try VERA for its memory savings? The only thing you need to change is the method in the configuration. The rest of your code stays identical.

Generated python
# Switch from LoRA to VERA by changing one line
config = FineTuningConfig(
    method="vera", # <-- That's it!
    lora_r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"]
)

# The rest of your code remains the same
model = FineTuningModel(base_model, config)
# ... continue with your training loop ...

This flexibility is the core strength of the FineTuning toolkit. It turns your code into a laboratory for cutting-edge LLM research.

🗺️ Your Journey Forward

You now have the foundational knowledge and the tools to start your own fine-tuning projects.

What to explore next:

Quantization (QLoRA): A technique to run this process with even less memory by loading the base model in 4-bit precision. (Coming soon to this toolkit!).

Merging Adapters: After training, you can "merge" your LoRA adapter back into the base model to create a new, standalone model that doesn't require extra code for inference.

Contributing: The best way to learn is to build. Check out our roadmap and open issues to see how you can help.

🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. Please see our CONTRIBUTING.md guide.

📜 License

Distributed under the Apache 2.0 License. See LICENSE for more information.

📚 Further Reading & Citations

If you use these methods in your research, please cite the original authors.

LoRA: Hu, et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. arXiv:2106.09685

VERA: Kopiczko, et al. (2023). VERA: Vector-based Random Matrix Adaptation. arXiv:2310.11454

(Add citations for other methods as needed)
