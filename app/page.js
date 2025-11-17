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
          colabUrl: "",
          status: "coming_soon",
          icon: "🚀"
        },
        {
          id: "m3l2",
          title: "Multi-Task Learning (One Model, Many Jobs)",
          duration: "1.5 hours",
          difficulty: "Advanced",
          description: "Train your model to do multiple tasks at once. Sentiment analysis AND summarization? Easy!",
          colabUrl: "",
          status: "coming_soon",
          icon: "🎨"
        },
        {
          id: "m3l3",
          title: "Custom Loss Functions (Get Creative!)",
          duration: "1 hour",
          difficulty: "Advanced",
          description: "Sometimes the default loss function isn't enough. Let's write our own!",
          colabUrl: "",
          status: "coming_soon",
          icon: "🎲"
        }
      ]
    },
    module4: {
      title: "💼 Real-World Projects",
      emoji: "🟠",
      subtitle: "Build something awesome!",
      duration: "Week 4",
      lessons: [
        {
          id: "m4l1",
          title: "Project: Build a Smart Customer Support Bot",
          duration: "3 hours",
          difficulty: "Intermediate",
          description: "End-to-end project: Fine-tune a model to answer customer questions based on your company docs.",
          colabUrl: "",
          status: "coming_soon",
          icon: "💬"
        },
        {
          id: "m4l2",
          title: "Project: Create a Code Review Assistant",
          duration: "3 hours",
          difficulty: "Advanced",
          description: "Train a model to review code, catch bugs, and suggest improvements. Like having a senior dev on your team!",
          colabUrl: "",
          status: "coming_soon",
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
          title: "Deploy Your Model (Make it Public!)",
          duration: "2 hours",
          difficulty: "Intermediate",
          description: "From Colab to the cloud! Deploy your model using HuggingFace Spaces, Gradio, or FastAPI.",
          colabUrl: "",
          status: "coming_soon",
          icon: "🚀"
        },
        {
          id: "m5l2",
          title: "Monitoring & Improving (Keep it Running!)",
          duration: "1.5 hours",
          difficulty: "Advanced",
          description: "Track performance, handle errors, and continuously improve your deployed model.",
          colabUrl: "",
          status: "coming_soon",
          icon: "📊"
        }
      ]
    }
  }

  return (
    <main className="min-h-screen p-4 md:p-8">
      <div className="max-w-7xl mx-auto glass-card p-8 md:p-12">
        {/* Hero Section */}
        <div className="text-center mb-16 animate-fade-in">
          <h1 className="text-5xl md:text-7xl font-extrabold gradient-text mb-4 animate-fade-in-down">
            Fine-Tuning Academy
          </h1>
          <p className="text-2xl md:text-3xl text-gray-700 font-medium mb-3 animate-fade-in-up">
            Learn AI Like a Friend is Teaching You
          </p>
          <p className="text-lg text-gray-600 animate-fade-in">
            Free • Interactive • Actually Fun • Zero BS
          </p>
        </div>

        {/* Feature Cards */}
        <div className="grid md:grid-cols-3 gap-6 mb-16">
          <div className="feature-card">
            <div className="text-5xl mb-4">🎓</div>
            <h3 className="text-xl font-bold mb-2">Learn by Doing</h3>
            <p className="opacity-90">Hands-on lessons in Google Colab. Click, code, learn. No boring theory!</p>
          </div>

          <div className="feature-card bg-gradient-to-br from-pink-500 to-red-500">
            <div className="text-5xl mb-4">💰</div>
            <h3 className="text-xl font-bold mb-2">100% Free</h3>
            <p className="opacity-90">Free GPU from Google. Free courses. Free everything. Seriously.</p>
          </div>

          <div className="feature-card bg-gradient-to-br from-blue-500 to-cyan-400">
            <div className="text-5xl mb-4">🤝</div>
            <h3 className="text-xl font-bold mb-2">Friend Mode</h3>
            <p className="opacity-90">No jargon. No PhD needed. Just me explaining like we're friends.</p>
          </div>
        </div>

        {/* Quick Start */}
        <div className="mb-16">
          <h2 className="text-4xl font-bold gradient-text mb-6">🚀 Start in 30 Seconds</h2>
          <div className="bg-white rounded-2xl p-8 shadow-lg">
            <h3 className="text-2xl font-bold text-purple-600 mb-4">Here's how this works:</h3>
            <ol className="text-lg text-gray-700 space-y-3 leading-relaxed">
              <li className="flex items-start">
                <span className="font-bold mr-2">1.</span>
                <span><strong>Pick a lesson</strong> from below (start with the first one!)</span>
              </li>
              <li className="flex items-start">
                <span className="font-bold mr-2">2.</span>
                <span><strong>Click the orange button</strong> - opens in Google Colab</span>
              </li>
              <li className="flex items-start">
                <span className="font-bold mr-2">3.</span>
                <span><strong>Run the code cells</strong> - just click play ▶️</span>
              </li>
              <li className="flex items-start">
                <span className="font-bold mr-2">4.</span>
                <span><strong>Learn by doing</strong> - you'll train real AI models!</span>
              </li>
            </ol>
            <p className="text-lg text-gray-600 mt-6">
              <strong>No installation. No setup. No credit card.</strong> Just click and learn!
            </p>
          </div>
        </div>

        {/* Featured Lesson */}
        <div className="mb-16">
          <h2 className="text-4xl font-bold gradient-text mb-6">⭐ Start Here!</h2>
          {Object.values(lessons).map(module =>
            module.lessons.filter(lesson => lesson.featured).map(lesson => (
              <div key={lesson.id} className="lesson-card border-4 border-purple-600">
                <span className="badge badge-available mb-4">⭐ MOST POPULAR</span>
                <h3 className="text-2xl font-bold text-purple-600 mb-3">
                  {lesson.icon} {lesson.title}
                </h3>
                <p className="text-lg text-gray-700 leading-relaxed mb-4">
                  {lesson.description}
                </p>
                <div className="text-gray-600 mb-6">
                  ⏱️ {lesson.duration} • 📊 {lesson.difficulty}
                </div>
                <a
                  href={lesson.colabUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="cta-button"
                >
                  🔥 Open in Colab (Free GPU!)
                </a>
              </div>
            ))
          )}
        </div>

        {/* All Lessons */}
        <div className="mb-16">
          <h2 className="text-4xl font-bold gradient-text mb-6">📚 All Lessons</h2>

          {Object.values(lessons).map((module, idx) => (
            <div key={idx} className="mb-8">
              <div className="bg-gradient-to-r from-purple-600 to-purple-900 rounded-2xl p-6 mb-4 text-white shadow-xl">
                <h3 className="text-2xl font-bold">
                  {module.emoji} {module.title}
                </h3>
                <p className="opacity-90 mt-1">
                  {module.subtitle} • {module.duration}
                </p>
              </div>

              <div className="space-y-4">
                {module.lessons.map(lesson => (
                  <div key={lesson.id} className="lesson-card">
                    <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4">
                      <div className="flex-1">
                        <span className={`badge ${lesson.status === 'available' ? 'badge-available' : 'badge-coming'}`}>
                          {lesson.status === 'available' ? '✅ Ready to Learn' : '🔜 Coming Soon'}
                        </span>
                        <h4 className="text-xl font-bold text-gray-800 mt-3 mb-2">
                          {lesson.icon} {lesson.title}
                        </h4>
                        <p className="text-gray-700 leading-relaxed mb-3">
                          {lesson.description}
                        </p>
                        <div className="text-gray-600">
                          ⏱️ {lesson.duration} • 📊 {lesson.difficulty}
                        </div>
                      </div>
                      <div className="flex-shrink-0">
                        {lesson.status === 'available' && lesson.colabUrl ? (
                          <a
                            href={lesson.colabUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="cta-button"
                          >
                            🚀 Start Learning
                          </a>
                        ) : (
                          <div className="px-8 py-4 bg-gray-200 rounded-full text-gray-600 font-semibold">
                            Coming Soon!
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
        <div className="text-center py-8 bg-white/50 rounded-2xl">
          <p className="text-lg text-gray-700 mb-2">
            Built with ❤️ for people who want to actually learn AI
          </p>
          <p className="text-gray-600">
            <a href="https://github.com/gouthamgo/FineTuning" target="_blank" rel="noopener noreferrer" className="text-purple-600 hover:underline font-semibold">
              GitHub
            </a>
            {' • '}
            <a href="https://huggingface.co" target="_blank" rel="noopener noreferrer" className="text-purple-600 hover:underline font-semibold">
              HuggingFace
            </a>
            {' • '}
            <a href="https://colab.research.google.com" target="_blank" rel="noopener noreferrer" className="text-purple-600 hover:underline font-semibold">
              Google Colab
            </a>
          </p>
          <p className="text-gray-500 mt-3 text-sm">
            100% Free • Forever • No BS
          </p>
        </div>
      </div>

      <style jsx>{`
        @keyframes fade-in {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes fade-in-down {
          from {
            opacity: 0;
            transform: translateY(-30px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        @keyframes fade-in-up {
          from {
            opacity: 0;
            transform: translateY(30px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-fade-in {
          animation: fade-in 1.5s ease-out;
        }
        .animate-fade-in-down {
          animation: fade-in-down 1s ease-out;
        }
        .animate-fade-in-up {
          animation: fade-in-up 1s ease-out;
        }
      `}</style>
    </main>
  )
}
