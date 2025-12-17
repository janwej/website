import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="CV Website", layout="wide")

page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>CV Website</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <!-- Tailwind via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    html, body {
      margin: 0;
      padding: 0;
    }

    /* Active nav button styling */
    .nav-btn-base {
      border-radius: 9999px;
      padding: 0.75rem 1.5rem;
      font-size: 0.9rem;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.3s ease;
      background-color: rgba(15, 23, 42, 0.7);
      color: #e5e7eb;
      border: 1px solid rgba(51, 65, 85, 0.7);
    }

    .nav-btn-base:hover {
      background-color: rgba(30, 64, 175, 0.8);
      transform: scale(1.05);
    }

    .nav-btn-active {
      background-image: linear-gradient(to right, #a855f7, #ec4899);
      color: white;
      box-shadow: 0 10px 25px rgba(168, 85, 247, 0.5);
      transform: scale(1.1);
      border-color: transparent;
    }

    .nav-btn-label {
      font-weight: 500;
    }
  </style>
</head>

<body class="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">

  <!-- Bubble Navigation Bar -->
  <nav id="navbar" class="fixed top-0 left-0 right-0 z-50 transition-all duration-300 bg-transparent">
    <div class="max-w-6xl mx-auto px-4 py-4">
      <div class="flex items-center justify-center gap-2 flex-wrap">
        <button class="nav-btn-base nav-btn nav-btn-active" data-section="about" type="button">
          <div class="flex items-center gap-2">
            <!-- User icon -->
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
                 xmlns="http://www.w3.org/2000/svg" class="text-purple-200">
              <path d="M12 12C14.0711 12 15.75 10.3211 15.75 8.25C15.75 6.17893 14.0711 4.5 12 4.5C9.92893 4.5 8.25 6.17893 8.25 8.25C8.25 10.3211 9.92893 12 12 12Z"
                    stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M5.25 19.5C5.25 16.8766 7.37665 14.75 10 14.75H14C16.6234 14.75 18.75 16.8766 18.75 19.5"
                    stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="nav-btn-label">About Me</span>
          </div>
        </button>

        <button class="nav-btn-base nav-btn" data-section="skills" type="button">
          <div class="flex items-center gap-2">
            <!-- Code icon -->
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
                 xmlns="http://www.w3.org/2000/svg" class="text-purple-200">
              <path d="M9 18L3 12L9 6" stroke="currentColor" stroke-width="1.5"
                    stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M15 6L21 12L15 18" stroke="currentColor" stroke-width="1.5"
                    stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="nav-btn-label">Skills</span>
          </div>
        </button>

        <button class="nav-btn-base nav-btn" data-section="projects" type="button">
          <div class="flex items-center gap-2">
            <!-- Briefcase icon -->
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
                 xmlns="http://www.w3.org/2000/svg" class="text-purple-200">
              <path d="M9 6.75C9 5.92157 9.67157 5.25 10.5 5.25H13.5C14.3284 5.25 15 5.92157 15 6.75V8.25H9V6.75Z"
                    stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M4.5 9.75C4.5 8.92157 5.17157 8.25 6 8.25H18C18.8284 8.25 19.5 8.92157 19.5 9.75V17.25C19.5 18.0784 18.8284 18.75 18 18.75H6C5.17157 18.75 4.5 18.0784 4.5 17.25V9.75Z"
                    stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="nav-btn-label">Projects</span>
          </div>
        </button>

        <button class="nav-btn-base nav-btn" data-section="education" type="button">
          <div class="flex items-center gap-2">
            <!-- Graduation cap icon -->
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
                 xmlns="http://www.w3.org/2000/svg" class="text-purple-200">
              <path d="M12 4.5L3 9L12 13.5L21 9L12 4.5Z" stroke="currentColor" stroke-width="1.5"
                    stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M6 11.25V16.5C8.48528 18.25 10.9375 19.125 12 19.5C13.0625 19.125 15.5147 18.25 18 16.5V11.25"
                    stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="nav-btn-label">Education</span>
          </div>
        </button>

      </div>
    </div>
  </nav>

  <!-- Main Content -->
  <div class="pt-24 pb-16 px-4">
    <div class="max-w-6xl mx-auto space-y-32">

      <!-- About Me Section -->
      <section id="about" class="min-h-screen flex items-center">
        <div class="w-full">
          <div class="text-center mb-12">
            <div class="w-32 h-32 mx-auto mb-6 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 p-1 shadow-2xl shadow-purple-500/50">
              <div class="w-full h-full rounded-full bg-slate-800 flex items-center justify-center">
                <!-- Big user icon -->
                <svg width="64" height="64" viewBox="0 0 24 24" fill="none"
                     xmlns="http://www.w3.org/2000/svg" class="text-purple-400">
                  <path d="M12 13.5C14.4853 13.5 16.5 11.4853 16.5 9C16.5 6.51472 14.4853 4.5 12 4.5C9.51472 4.5 7.5 6.51472 7.5 9C7.5 11.4853 9.51472 13.5 12 13.5Z"
                        stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M5.25 19.5C5.25 16.8766 7.37665 14.75 10 14.75H14C16.6234 14.75 18.75 16.8766 18.75 19.5"
                        stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
            </div>
            <h1 class="text-5xl md:text-6xl font-bold text-white mb-4 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-400">
              Your Name
            </h1>
            <p class="text-2xl text-purple-300 mb-2">Full Stack Developer</p>
            <p class="text-lg text-gray-400">Madrid, Spain</p>
          </div>

          <div class="bg-slate-800/50 backdrop-blur-lg rounded-3xl p-8 shadow-2xl border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300">
            <h2 class="text-3xl font-bold text-white mb-6">About Me</h2>
            <p class="text-gray-300 text-lg leading-relaxed mb-6">
              Passionate developer with expertise in building modern web applications.
              I love creating intuitive user experiences and solving complex problems through code.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

              <div class="flex items-center gap-3 text-gray-300">
                <!-- Mail icon -->
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                     xmlns="http://www.w3.org/2000/svg" class="text-purple-400">
                  <path d="M4.5 6.75H19.5C20.3284 6.75 21 7.42157 21 8.25V15.75C21 16.5784 20.3284 17.25 19.5 17.25H4.5C3.67157 17.25 3 16.5784 3 15.75V8.25C3 7.42157 3.67157 6.75 4.5 6.75Z"
                        stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M4.5 9L12 12.75L19.5 9"
                        stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span>your.email@example.com</span>
              </div>

              <div class="flex items-center gap-3 text-gray-300">
                <!-- GitHub icon (simple) -->
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                     xmlns="http://www.w3.org/2000/svg" class="text-purple-400">
                  <path d="M12 2.25C7.44365 2.25 3.75 5.94365 3.75 10.5C3.75 14.1449 6.13721 17.1916 9.46875 18.2109C9.49219 18.1641 9.5 18.1094 9.5 18.0547V16.5C8.03125 16.8281 7.6875 15.8203 7.6875 15.8203C7.54688 15.4219 7.29688 15.1641 7.29688 15.1641C6.92188 14.8828 7.3125 14.8828 7.3125 14.8828C7.71875 14.9141 7.9375 15.3047 7.9375 15.3047C8.29688 15.9609 8.9375 15.7734 9.1875 15.6641C9.22656 15.4141 9.33594 15.2266 9.45312 15.1172C8.1875 14.9922 6.85938 14.5078 6.85938 12.3984C6.85938 11.8203 7.0625 11.3438 7.39844 10.9844C7.34375 10.8594 7.17188 10.3281 7.44531 9.63281C7.44531 9.63281 7.89062 9.49219 9.5 10.4141C9.92188 10.2969 10.375 10.2422 10.8281 10.2422C11.2812 10.2422 11.7344 10.2969 12.1562 10.4141C13.7656 9.48438 14.2109 9.63281 14.2109 9.63281C14.4844 10.3281 14.3125 10.8594 14.2578 10.9844C14.5938 11.3438 14.7969 11.8203 14.7969 12.3984C14.7969 14.5234 13.4609 14.9844 12.1875 15.1094C12.3438 15.2422 12.4844 15.5078 12.4844 15.9375V18.0547C12.4844 18.1094 12.5 18.1641 12.5156 18.2109C15.8472 17.1916 18.2344 14.1449 18.2344 10.5C18.25 5.94365 14.5563 2.25 12 2.25Z"
                        fill="currentColor"/>
                </svg>
                <span>github.com/yourusername</span>
              </div>

              <div class="flex items-center gap-3 text-gray-300">
                <!-- LinkedIn icon -->
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                     xmlns="http://www.w3.org/2000/svg" class="text-purple-400">
                  <path d="M6.75 6.75C7.57843 6.75 8.25 6.07843 8.25 5.25C8.25 4.42157 7.57843 3.75 6.75 3.75C5.92157 3.75 5.25 4.42157 5.25 5.25C5.25 6.07843 5.92157 6.75 6.75 6.75Z"
                        fill="currentColor"/>
                  <path d="M5.25 9H8.25V18.75H5.25V9Z"
                        fill="currentColor"/>
                  <path d="M10.5 9H13.3125V10.3125H13.3438C13.75 9.5625 14.7812 8.78125 16.2188 8.78125C18.9844 8.78125 19.5 10.5469 19.5 12.8281V18.75H16.5V13.5469C16.5 12.4219 16.4688 10.9688 15.0312 10.9688C13.5625 10.9688 13.3125 12.2031 13.3125 13.4688V18.75H10.5V9Z"
                        fill="currentColor"/>
                </svg>
                <span>linkedin.com/in/yourprofile</span>
              </div>

            </div>
          </div>
        </div>
      </section>

      <!-- Skills Section -->
      <section id="skills" class="min-h-screen flex items-center">
        <div class="w-full">
          <h2 class="text-4xl md:text-5xl font-bold text-white mb-12 text-center">Technical Skills</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Each card -->
            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-6 border border-slate-700/50 hover:border-purple-500/50 hover:scale-105 transition-all duration-300 shadow-xl">
              <h3 class="text-xl font-bold text-purple-400 mb-4">Frontend</h3>
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">React</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">TypeScript</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Tailwind CSS</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Next.js</span>
              </div>
            </div>

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-6 border border-slate-700/50 hover:border-purple-500/50 hover:scale-105 transition-all duration-300 shadow-xl">
              <h3 class="text-xl font-bold text-purple-400 mb-4">Backend</h3>
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Node.js</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Python</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Express</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Django</span>
              </div>
            </div>

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-6 border border-slate-700/50 hover:border-purple-500/50 hover:scale-105 transition-all duration-300 shadow-xl">
              <h3 class="text-xl font-bold text-purple-400 mb-4">Database</h3>
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">PostgreSQL</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">MongoDB</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Redis</span>
              </div>
            </div>

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-6 border border-slate-700/50 hover:border-purple-500/50 hover:scale-105 transition-all duration-300 shadow-xl">
              <h3 class="text-xl font-bold text-purple-400 mb-4">DevOps</h3>
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Docker</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">AWS</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">CI/CD</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Git</span>
              </div>
            </div>

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-6 border border-slate-700/50 hover:border-purple-500/50 hover:scale-105 transition-all duration-300 shadow-xl">
              <h3 class="text-xl font-bold text-purple-400 mb-4">Tools</h3>
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">VS Code</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Figma</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Postman</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Linux</span>
              </div>
            </div>

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-6 border border-slate-700/50 hover:border-purple-500/50 hover:scale-105 transition-all duration-300 shadow-xl">
              <h3 class="text-xl font-bold text-purple-400 mb-4">Soft Skills</h3>
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Team Leadership</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Problem Solving</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Agile</span>
                <span class="px-3 py-1 bg-purple-500/20 text-purple-300 rounded-full text-sm border border-purple-500/30">Communication</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Projects Section -->
      <section id="projects" class="min-h-screen flex items-center">
        <div class="w-full">
          <h2 class="text-4xl md:text-5xl font-bold text-white mb-12 text-center">Featured Projects</h2>
          <div class="space-y-8">

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-8 border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 shadow-xl hover:shadow-2xl hover:scale-[1.02]">
              <div class="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-blue-500 to-cyan-500 text-white font-bold mb-4">
                Project 1
              </div>
              <h3 class="text-2xl font-bold text-white mb-3">E-Commerce Platform</h3>
              <p class="text-gray-300 mb-4 leading-relaxed">
                Full-stack e-commerce solution with real-time inventory management, payment processing, and admin dashboard.
              </p>
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">React</span>
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">Node.js</span>
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">PostgreSQL</span>
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">Stripe</span>
              </div>
            </div>

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-8 border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 shadow-xl hover:shadow-2xl hover:scale-[1.02]">
              <div class="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-purple-500 to-pink-500 text-white font-bold mb-4">
                Project 2
              </div>
              <h3 class="text-2xl font-bold text-white mb-3">AI-Powered Analytics Dashboard</h3>
              <p class="text-gray-300 mb-4 leading-relaxed">
                Data visualization platform with machine learning insights for business intelligence and predictive analytics.
              </p>
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">Python</span>
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">TensorFlow</span>
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">React</span>
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">D3.js</span>
              </div>
            </div>

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-8 border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 shadow-xl hover:shadow-2xl hover:scale-[1.02]">
              <div class="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-green-500 to-emerald-500 text-white font-bold mb-4">
                Project 3
              </div>
              <h3 class="text-2xl font-bold text-white mb-3">Social Media App</h3>
              <p class="text-gray-300 mb-4 leading-relaxed">
                Mobile-first social platform with real-time messaging, media sharing, and personalized content feeds.
              </p>
              <div class="flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">React Native</span>
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">Firebase</span>
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">Redux</span>
                <span class="px-3 py-1 bg-slate-700/50 text-gray-300 rounded-lg text-sm border border-slate-600">WebSocket</span>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- Education Section -->
      <section id="education" class="min-h-screen flex items-center">
        <div class="w-full">
          <h2 class="text-4xl md:text-5xl font-bold text-white mb-12 text-center">Education &amp; Certifications</h2>
          <div class="space-y-6">

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-6 border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 shadow-xl">
              <div class="flex items-start justify-between flex-wrap gap-4">
                <div class="flex-1">
                  <h3 class="text-xl font-bold text-white mb-2">Master of Science in Computer Science</h3>
                  <p class="text-purple-400 font-medium mb-2">University Name</p>
                  <p class="text-gray-300">Specialized in Machine Learning and Software Engineering</p>
                </div>
                <div class="px-4 py-2 bg-purple-500/20 text-purple-300 rounded-lg border border-purple-500/30">
                  2020 - 2022
                </div>
              </div>
            </div>

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-6 border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 shadow-xl">
              <div class="flex items-start justify-between flex-wrap gap-4">
                <div class="flex-1">
                  <h3 class="text-xl font-bold text-white mb-2">Bachelor of Science in Computer Engineering</h3>
                  <p class="text-purple-400 font-medium mb-2">University Name</p>
                  <p class="text-gray-300">Graduated with Honors, GPA: 3.8/4.0</p>
                </div>
                <div class="px-4 py-2 bg-purple-500/20 text-purple-300 rounded-lg border border-purple-500/30">
                  2016 - 2020
                </div>
              </div>
            </div>

            <div class="bg-slate-800/50 backdrop-blur-lg rounded-2xl p-6 border border-slate-700/50 hover:border-purple-500/50 transition-all duration-300 shadow-xl">
              <div class="flex items-start justify-between flex-wrap gap-4">
                <div class="flex-1">
                  <h3 class="text-xl font-bold text-white mb-2">AWS Certified Solutions Architect</h3>
                  <p class="text-purple-400 font-medium mb-2">Amazon Web Services</p>
                  <p class="text-gray-300">Professional level cloud architecture certification</p>
                </div>
                <div class="px-4 py-2 bg-purple-500/20 text-purple-300 rounded-lg border border-purple-500/30">
                  2023
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>

    </div>
  </div>

  <!-- Footer -->
  <footer class="bg-slate-900/90 backdrop-blur-lg py-8 border-t border-slate-700/50">
    <div class="max-w-6xl mx-auto px-4 text-center">
      <p class="text-gray-400">© 2024 Your Name. All rights reserved.</p>
    </div>
  </footer>

  <!-- JS: nav behavior + smooth scroll + active section -->
  <script>
    const nav = document.getElementById('navbar');
    const buttons = document.querySelectorAll('.nav-btn');
    const sections = ['about', 'skills', 'projects', 'education'];

    function setActiveButton(id) {
      buttons.forEach(btn => {
        if (btn.dataset.section === id) {
          btn.classList.add('nav-btn-active');
        } else {
          btn.classList.remove('nav-btn-active');
        }
      });
    }

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.dataset.section;
        const el = document.getElementById(id);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth' });
          setActiveButton(id);
        }
      });
    });

    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        nav.classList.add('bg-slate-900/95', 'backdrop-blur-lg', 'shadow-lg', 'border-b', 'border-slate-800/80');
      } else {
        nav.classList.remove('bg-slate-900/95', 'backdrop-blur-lg', 'shadow-lg', 'border-b', 'border-slate-800/80');
      }

      // Set active section based on scroll position
      let current = 'about';
      const offset = window.innerHeight / 3;

      sections.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
          const rect = el.getBoundingClientRect();
          if (rect.top <= offset && rect.bottom >= offset) {
            current = id;
          }
        }
      });

      setActiveButton(current);
    });
  </script>

</body>
</html>
"""

# Render the page inside Streamlit
html(page, height=2200, scrolling=True)
