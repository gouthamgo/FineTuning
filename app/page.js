'use client'

export default function Home() {
  const lessons = {
    module1: {
      title: "🌱 Foundations",
      emoji: "🟢",
      subtitle: "Start your journey - understand the basics",
      duration: "Week 1",
      lessons: [
        {
          id: "m1l1",
          title: "What Even is Fine-Tuning? (Let's Talk Like Friends)",
          duration: "30 min",
          difficulty: "Super Beginner",
          description: "Seriously, what is this fine-tuning thing everyone talks about? I'll explain it like we're chatting over coffee. Zero jargon, promise!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module1_foundations/01_what_is_finetuning.ipynb",
          status: "available",
          icon: "💡"
        },
        {
          id: "m1l2",
          title: "Your First AI Model (Yes, YOU Can Do This!)",
          duration: "1 hour",
          difficulty: "Beginner",
          description: "Let's actually load a real AI model and make it work! We'll take it step-by-step. You'll be amazed at how easy this is.",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module1_foundations/02_your_first_model.ipynb",
          status: "available",
          icon: "🤖"
        },
        {
          id: "m1l3",
          title: "Understanding Your Data (The Secret Sauce)",
          duration: "1 hour",
          difficulty: "Beginner",
          description: "Data is like ingredients for cooking. Bad ingredients = bad food. I'll show you how to prep your data like a chef!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module1_foundations/03_understanding_data.ipynb",
          status: "available",
          icon: "📊"
        }
      ]
    },
    module2: {
      title: "🚀 Your First Fine-Tuning",
      emoji: "🟡",
      subtitle: "This is where the magic happens!",
      duration: "Week 2",
      lessons: [
        {
          id: "m2l1",
          title: "ACTUALLY Fine-Tune Your First Model! 🎉",
          duration: "2 hours",
          difficulty: "Beginner",
          description: "This is THE lesson! You'll train your own AI model from scratch. Watch it learn in real-time. It's like magic, but it's REAL!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module2_first_training/01_first_finetuning.ipynb",
          status: "available",
          featured: true,
          icon: "⚡"
        },
        {
          id: "m2l2",
          title: "Making Your Model Better (Hyperparameter Tuning)",
          duration: "1.5 hours",
          difficulty: "Intermediate",
          description: "Learn the secret dials and knobs that make your model go from good to GREAT! We'll experiment with learning rates, batch sizes, and more.",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module2_first_training/02_hyperparameter_tuning.ipynb",
          status: "available",
          icon: "🎛️"
        },
        {
          id: "m2l3",
          title: "Debugging Like a Pro (When Things Go Wrong)",
          duration: "1 hour",
          difficulty: "Intermediate",
          description: "Your model will fail. A lot. Learn how to fix the most common errors fast and become a debugging ninja!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module2_first_training/03_debugging_training.ipynb",
          status: "available",
          icon: "🔧"
        }
      ]
    },
    module3: {
      title: "🎯 Advanced Techniques",
      emoji: "🔵",
      subtitle: "Level up your skills!",
      duration: "Week 3",
      lessons: [
        {
          id: "m3l1",
          title: "LoRA & QLoRA (Train HUGE Models on Free GPUs!)",
          duration: "1.5 hours",
          difficulty: "Advanced",
          description: "Train models with BILLIONS of parameters using these clever tricks. Same results, way less memory!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module3_advanced/01_lora_qlora.ipynb",
          status: "available",
          icon: "🚀"
        },
        {
          id: "m3l2",
          title: "Multi-Task Learning (One Model, Many Jobs)",
          duration: "1.5 hours",
          difficulty: "Advanced",
          description: "Train your model to do multiple tasks at once. Sentiment analysis AND summarization? Easy!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module3_advanced/02_multitask_learning.ipynb",
          status: "available",
          icon: "🎨"
        },
        {
          id: "m3l3",
          title: "Custom Loss Functions (Get Creative!)",
          duration: "1 hour",
          difficulty: "Advanced",
          description: "Master 5 custom loss functions for imbalanced data, cost-sensitive errors, and more. Write your own production-grade loss functions!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module3_advanced/03_custom_loss_functions.ipynb",
          status: "available",
          icon: "🎲"
        },
        {
          id: "m3l4",
          title: "Performance Optimization (Make Models 10x Faster!)",
          duration: "2 hours",
          difficulty: "Advanced",
          description: "Master quantization, distillation, pruning, ONNX Runtime, and batching to make models 10x faster and 95% cheaper. Essential production skills!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module3_advanced/04_performance_optimization.ipynb",
          status: "available",
          icon: "⚡"
        }
      ]
    },
    module4: {
      title: "💼 Real-World Projects",
      emoji: "🟠",
      subtitle: "Build portfolio-worthy projects!",
      duration: "Week 4",
      lessons: [
        {
          id: "m4l1",
          title: "Project: Production Customer Support Bot",
          duration: "3 hours",
          difficulty: "Intermediate",
          description: "End-to-end portfolio project with production code, monitoring, and deployment. Put this on your resume!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module4_projects/01_customer_support_bot.ipynb",
          status: "available",
          featured: true,
          icon: "💬"
        },
        {
          id: "m4l2",
          title: "Project: Code Review Assistant",
          duration: "3 hours",
          difficulty: "Advanced",
          description: "Fine-tune CodeT5 to review code, detect bugs, assess quality, and suggest improvements. Integrates with GitHub Actions for automated PR reviews!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module4_projects/02_code_review_assistant.ipynb",
          status: "available",
          icon: "💻"
        }
      ]
    },
    module5: {
      title: "🌐 Deployment & Production",
      emoji: "🟣",
      subtitle: "Ship it to the world!",
      duration: "Week 5",
      lessons: [
        {
          id: "m5l1",
          title: "Deploy to Production (3 Different Ways!)",
          duration: "2 hours",
          difficulty: "Intermediate",
          description: "Deploy with HuggingFace Spaces, FastAPI + Docker, and AWS Lambda. Get a live URL for your resume!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module5_deployment/01_deploy_production.ipynb",
          status: "available",
          icon: "🚀"
        },
        {
          id: "m5l2",
          title: "MLOps & Monitoring (Production Excellence)",
          duration: "1.5 hours",
          difficulty: "Advanced",
          description: "Build a complete monitoring system with Prometheus, structured logging, alerting, and continuous training. This separates good from great ML engineers!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module5_deployment/02_mlops_monitoring.ipynb",
          status: "available",
          icon: "📊"
        },
        {
          id: "m5l3",
          title: "Cost Optimization & Scaling",
          duration: "2 hours",
          difficulty: "Advanced",
          description: "Reduce ML costs by 90% through serverless deployment, auto-scaling, spot instances, and A/B testing. Save $10K+/year on infrastructure!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module5_deployment/03_cost_optimization_scaling.ipynb",
          status: "available",
          featured: true,
          icon: "💰"
        }
      ]
    },
    module6: {
      title: "💼 Get Hired!",
      emoji: "⭐",
      subtitle: "Turn projects into job offers",
      duration: "Week 6",
      lessons: [
        {
          id: "m6l1",
          title: "Portfolio, Resume & Interview Prep",
          duration: "2 hours",
          difficulty: "All levels",
          description: "GitHub portfolio setup, resume bullets that get interviews, and answers to top 20 ML interview questions. This is how you actually get hired!",
          colabUrl: "https://colab.research.google.com/github/gouthamgo/FineTuning/blob/main/lessons/module6_job_readiness/01_portfolio_interview_prep.ipynb",
          status: "available",
          featured: true,
          icon: "🎯"
        }
      ]
    }
  }

  return (
    <main className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="border-b border-gray-200 bg-white">
        <div className="max-w-5xl mx-auto px-6 py-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Fine-Tuning Academy
          </h1>
          <p className="text-xl text-gray-600">
            Learn AI like a friend is teaching you
          </p>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-5xl mx-auto px-6 py-12">
        {/* Quick Intro */}
        <div className="mb-16">
          <div className="bg-white rounded-lg border border-gray-200 p-8">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4">
              How it works
            </h2>
            <div className="space-y-3 text-gray-600">
              <p>1. Pick a lesson below (start with the first one)</p>
              <p>2. Click to open in Google Colab (free GPU included)</p>
              <p>3. Run the code cells and learn by doing</p>
              <p>4. Build real projects for your portfolio</p>
            </div>
            <div className="mt-6 pt-6 border-t border-gray-100">
              <p className="text-sm text-gray-500">
                No installation. No setup. No credit card. Just learning.
              </p>
            </div>
          </div>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-6 mb-16">
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="text-3xl font-bold text-gray-900 mb-1">16</div>
            <div className="text-sm text-gray-600">Lessons</div>
          </div>
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="text-3xl font-bold text-gray-900 mb-1">6</div>
            <div className="text-sm text-gray-600">Modules</div>
          </div>
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="text-3xl font-bold text-gray-900 mb-1">100%</div>
            <div className="text-sm text-gray-600">Free</div>
          </div>
        </div>

        {/* Lessons by Module */}
        <div className="space-y-12">
          {Object.values(lessons).map((module, idx) => (
            <div key={idx}>
              {/* Module Header */}
              <div className="mb-6">
                <div className="flex items-center gap-3 mb-2">
                  <span className="text-2xl">{module.emoji}</span>
                  <h2 className="text-2xl font-semibold text-gray-900">
                    {module.title.replace(/^[^\s]+\s/, '')}
                  </h2>
                </div>
                <p className="text-gray-600 ml-11">{module.subtitle}</p>
              </div>

              {/* Lessons */}
              <div className="space-y-4">
                {module.lessons.map(lesson => (
                  <div key={lesson.id} className="lesson-card">
                    <div className="flex items-start justify-between gap-6">
                      <div className="flex-1">
                        {/* Badges */}
                        <div className="flex items-center gap-2 mb-3">
                          <span className={`badge ${lesson.status === 'available' ? 'badge-available' : 'badge-coming'}`}>
                            {lesson.status === 'available' ? 'Available' : 'Coming Soon'}
                          </span>
                          {lesson.featured && (
                            <span className="badge badge-featured">
                              Featured
                            </span>
                          )}
                        </div>

                        {/* Title */}
                        <h3 className="text-lg font-semibold text-gray-900 mb-2">
                          {lesson.icon} {lesson.title}
                        </h3>

                        {/* Description */}
                        <p className="text-gray-600 text-sm mb-4 leading-relaxed">
                          {lesson.description}
                        </p>

                        {/* Meta */}
                        <div className="flex items-center gap-4 text-xs text-gray-500">
                          <span>⏱ {lesson.duration}</span>
                          <span>•</span>
                          <span>{lesson.difficulty}</span>
                        </div>
                      </div>

                      {/* CTA */}
                      <div className="flex-shrink-0">
                        {lesson.status === 'available' && lesson.colabUrl ? (
                          <a
                            href={lesson.colabUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="btn-primary"
                          >
                            Open in Colab →
                          </a>
                        ) : (
                          <div className="px-4 py-2 rounded-lg bg-gray-100 text-gray-400 text-sm font-medium">
                            Coming Soon
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* Footer */}
        <div className="mt-20 pt-12 border-t border-gray-200">
          <div className="text-center">
            <p className="text-gray-600 mb-4">
              Built for people who want to actually learn AI
            </p>
            <div className="flex items-center justify-center gap-6 text-sm">
              <a
                href="https://github.com/gouthamgo/FineTuning"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-600 hover:text-gray-900 transition-colors"
              >
                GitHub
              </a>
              <span className="text-gray-300">•</span>
              <a
                href="https://huggingface.co"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-600 hover:text-gray-900 transition-colors"
              >
                HuggingFace
              </a>
              <span className="text-gray-300">•</span>
              <a
                href="https://colab.research.google.com"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-600 hover:text-gray-900 transition-colors"
              >
                Google Colab
              </a>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}
