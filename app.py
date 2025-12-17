import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="My CV - Interactive Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
)

# Global Streamlit styling
st.markdown(
    """
    <style>
    /* Make the whole Streamlit app use a dark/gradient background */
    [data-testid="stAppViewContainer"] {
        padding: 0 !important;
        background: linear-gradient(to bottom right, #020617, #4c1d95, #020617) !important;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    body {
        margin: 0;
        padding: 0;
        background: #020617;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My CV - Interactive Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in { animation: fadeIn 1s ease-out; }
        html { scroll-behavior: smooth; }

        /* Remove iframe margins + nudge content down a bit
           so the navbar isn't cut by the Streamlit header */
        body {
            margin: 0;
            padding: 16px 0 0 0; /* top padding pushes everything slightly down */
        }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
    
    <!-- Navigation Bar -->
    <nav id="navbar" class="fixed top-4 left-0 right-0 z-50 transition-all duration-300">
        <div class="max-w-6xl mx-auto px-4 py-4">
            <div class="flex items-center justify-center gap-2 flex-wrap">
                <button onclick="scrollToSection('about')" class="nav-btn px-6 py-3 rounded-full transition-all duration-300 bg-gradient-to-r from-purple-500 to-pink-500 text-white scale-110 shadow-lg shadow-purple-500/50">
                    <div class="flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                        </svg>
                        <span class="font-medium">About Me</span>
                    </div>
                </button>
                <button onclick="scrollToSection('skills')" class="nav-btn px-6 py-3 rounded-full transition-all duration-300 bg-slate-800/50 text-gray-300 hover:bg-slate-700/70 hover:scale-105">
                    <div class="flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path>
                        </svg>
                        <span class="font-medium">Skills</span>
                    </div>
                </button>
                <button onclick="scrollToSection('projects')" class="nav-btn px-6 py-3 rounded-full transition-all duration-300 bg-slate-800/50 text-gray-300 hover:bg-slate-700/70 hover:scale-105">
                    <div class="flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                        </svg>
                        <span class="font-medium">Projects</span>
                    </div>
                </button>
                <button onclick="scrollToSection('education')" class="nav-btn px-6 py-3 rounded-full transition-all duration-300 bg-slate-800/50 text-gray-300 hover:bg-slate-700/70 hover:scale-105">
                    <div class="flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"></path>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path>
                        </svg>
                        <span class="font-medium">Education</span>
                    </div>
                </button>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="pt-32 pb-16 px-4">
        <div class="max-w-6xl mx-auto space-y-32">
            
            <!-- About Me Section -->
            <section id="about" class="py-24">
                <div class="w-full">
                    <div class="text-center mb-12 animate-fade-in">
                        <div class="w-32 h-32 mx-auto mb-6 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 p-1 shadow-2xl shadow-purple-500/50">
                            <div class="w-full h-full rounded-full bg-slate-800 flex items-center justify-center">
                                <svg class="w-16 h-16 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                                </svg>
                            </div>
                        </div>
                        <h1 class="text-6xl font-bold text-white mb-4 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-400">
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
                                <svg class="w-5 h-5 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                                </svg>
                                <span>your.email@example.com</span>
                            </div>
                            <div class="flex items-center gap-3 text-gray-300">
                                <svg class="w-5 h-5 text-purple-400" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                                </svg>
                                <span>github.com/yourusername</span>
                            </div>
                            <div class="flex items-center gap-3 text-gray-300">
                                <svg class="w-5 h-5 text-purple-400" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                                </svg>
                                <span>linkedin.com/in/yourprofile</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Skills, Projects, Education sections stay the same as before -->
            <!-- (keep your existing content here unchanged) -->

        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-slate-900/90 backdrop-blur-lg py-8 border-t border-slate-700/50">
        <div class="max-w-6xl mx-auto px-4 text-center">
            <p class="text-gray-400">© 2024 Your Name. All rights reserved.</p>
        </div>
    </footer>

    <script>
        let activeSection = 'about';
        
        function scrollToSection(sectionId) {
            activeSection = sectionId;
            document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
            updateNavButtons();
        }
        
        function updateNavButtons() {
            const buttons = document.querySelectorAll('.nav-btn');
            buttons.forEach(btn => {
                const section = btn.onclick.toString().match(/'([^']+)'/)[1];
                if (section === activeSection) {
                    btn.className = 'nav-btn px-6 py-3 rounded-full transition-all duration-300 bg-gradient-to-r from-purple-500 to-pink-500 text-white scale-110 shadow-lg shadow-purple-500/50';
                } else {
                    btn.className = 'nav-btn px-6 py-3 rounded-full transition-all duration-300 bg-slate-800/50 text-gray-300 hover:bg-slate-700/70 hover:scale-105';
                }
            });
        }
        
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 50) {
                navbar.style.backgroundColor = 'rgba(15, 23, 42, 0.95)';
                navbar.style.backdropFilter = 'blur(12px)';
                navbar.style.boxShadow = '0 10px 15px -3px rgba(0, 0, 0, 0.1)';
            } else {
                navbar.style.backgroundColor = 'transparent';
                navbar.style.backdropFilter = 'none';
                navbar.style.boxShadow = 'none';
            }
        });

        const observerOptions = {
            root: null,
            rootMargin: '-50% 0px -50% 0px',
            threshold: 0
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    activeSection = entry.target.id;
                    updateNavButtons();
                }
            });
        }, observerOptions);
        
        document.querySelectorAll('section').forEach(section => {
            observer.observe(section);
        });
    </script>
</body>
</html>
'''

# Render the HTML inside Streamlit
html(HTML_TEMPLATE, height=2600, scrolling=True)
