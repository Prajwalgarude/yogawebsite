# Import the Flask module
from flask import Flask, render_template_string

# Initialize the Flask application
app = Flask(__name__)

# The HTML content for your yoga webpage
# This HTML is embedded directly into the Python code for simplicity,
# but in a larger application, you might use Flask's template rendering
# system with HTML files in a 'templates' folder.
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discover the Path of Yoga</title>
    <!-- Load Tailwind CSS from CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Load Inter font from Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #F8F4F0; /* Light parchment-like background */
        }
        .hero-background {
            /* Dynamic real-world image placeholder for a peaceful yoga scene */
            background-image: url('https://source.unsplash.com/random/1920x800/?yoga,meditation,sunrise');
            background-size: cover;
            background-position: center;
            position: relative;
            z-index: 0;
        }
        .hero-background::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(to bottom, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.3) 50%, rgba(0,0,0,0.6) 100%);
            z-index: -1;
        }
        .section-gradient-blue {
            background: linear-gradient(to right, #6EE7B7, #3B82F6); /* Emerald to Blue */
        }
        .section-gradient-purple {
            background: linear-gradient(to right, #C4B5FD, #8B5CF6); /* Light Purple to Deep Purple */
        }
        .text-gradient {
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .text-gradient-blue-indigo {
            background-image: linear-gradient(to right, #3B82F6, #6366F1); /* Blue to Indigo */
        }
        .card-shadow {
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        .card-hover:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
    </style>
</head>
<body class="text-gray-800">

    <!-- New Orange Header Section -->
    <section class="w-full bg-orange-600 text-white text-center py-4 md:py-6 lg:py-8 shadow-xl">
        <h1 class="text-3xl md:text-5xl lg:text-6xl font-extrabold tracking-wide drop-shadow-md">Yoga Se Hi Hoga</h1>
    </section>

    <!-- Header Section -->
    <header class="bg-gradient-to-r from-teal-500 to-emerald-600 shadow-xl py-4 px-6 md:px-12">
        <nav class="container mx-auto flex justify-between items-center">
            <a href="#" class="text-white text-3xl font-extrabold rounded-lg p-2 hover:bg-white hover:text-emerald-600 transition duration-300">Yoga Essence</a>
            <ul class="hidden md:flex space-x-8">
                <li><a href="#benefits" class="text-white hover:text-teal-200 text-lg transition duration-300 rounded-lg p-2 hover:bg-emerald-700">Benefits</a></li>
                <li><a href="#types" class="text-white hover:text-teal-200 text-lg transition duration-300 rounded-lg p-2 hover:bg-emerald-700">Styles</a></li>
                <li><a href="#start" class="text-white hover:text-teal-200 text-lg transition duration-300 rounded-lg p-2 hover:bg-emerald-700">Beginners</a></li>
                <li><a href="#contact" class="text-white hover:text-teal-200 text-lg transition duration-300 rounded-lg p-2 hover:bg-emerald-700">Contact</a></li>
            </ul>
            <!-- Mobile Menu Button (Hamburger) -->
            <button id="mobile-menu-button" class="md:hidden text-white focus:outline-none">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </nav>
    </header>

    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu-overlay" class="fixed inset-0 bg-gray-900 bg-opacity-95 z-50 hidden flex flex-col items-center justify-center space-y-8">
        <button id="close-menu-button" class="absolute top-6 right-6 text-white focus:outline-none">
            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
        </button>
        <ul class="text-white text-3xl font-semibold space-y-6 text-center">
            <li><a href="#benefits" class="block py-3 hover:text-teal-400 transition duration-300" onclick="mobileMenuOverlay.classList.add('hidden');">Benefits</a></li>
            <li><a href="#types" class="block py-3 hover:text-teal-400 transition duration-300" onclick="mobileMenuOverlay.classList.add('hidden');">Styles</a></li>
            <li><a href="#start" class="block py-3 hover:text-teal-400 transition duration-300" onclick="mobileMenuOverlay.classList.add('hidden');">Beginners</a></li>
            <li><a href="#contact" class="block py-3 hover:text-teal-400 transition duration-300" onclick="mobileMenuOverlay.classList.add('hidden');">Contact</a></li>
        </ul>
    </div>

    <!-- Hero Section -->
    <section class="hero-background h-screen flex items-center justify-center text-center text-white p-4">
        <div class="bg-black bg-opacity-50 rounded-2xl p-8 md:p-14 shadow-2xl max-w-4xl border border-gray-700">
            <h1 class="text-4xl md:text-7xl font-extrabold mb-6 leading-tight drop-shadow-lg text-gradient text-gradient-blue-indigo">Discover Your Inner Harmony</h1>
            <p class="text-lg md:text-2xl mb-8 drop-shadow-md font-light">Unite your mind, body, and spirit through the transformative power of yoga.</p>
            <a href="#start" class="inline-block bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-3 px-8 rounded-full text-xl shadow-lg transform hover:scale-105 transition duration-300 ease-in-out border-2 border-emerald-400">Begin Your Journey</a>
        </div>
    </section>

    <!-- Benefits Section -->
    <section id="benefits" class="py-16 md:py-24 bg-gradient-to-br from-indigo-50 to-blue-100">
        <div class="container mx-auto px-4 md:px-8">
            <h2 class="text-4xl md:text-5xl font-extrabold text-center mb-16 text-blue-900 drop-shadow-md">The Profound Benefits of Yoga</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                <!-- Benefit Card 1 -->
                <div class="bg-white rounded-2xl card-shadow p-8 transform transition duration-300 ease-in-out card-hover border border-indigo-100">
                    <div class="text-blue-600 mb-6 text-6xl flex justify-center">🧘‍♀️</div>
                    <h3 class="text-2xl font-bold mb-4 text-center text-gray-900">Physical Well-being</h3>
                    <ul class="list-disc list-inside text-gray-700 space-y-2 text-lg">
                        <li>Enhanced Flexibility & Strength</li>
                        <li>Improved Balance & Posture</li>
                        <li>Relief from Chronic Pain</li>
                        <li>Boosted Cardiovascular Health</li>
                    </ul>
                </div>
                <!-- Benefit Card 2 -->
                <div class="bg-white rounded-2xl card-shadow p-8 transform transition duration-300 ease-in-out card-hover border border-teal-100">
                    <div class="text-emerald-600 mb-6 text-6xl flex justify-center">🧠</div>
                    <h3 class="text-2xl font-bold mb-4 text-center text-gray-900">Mental Clarity & Peace</h3>
                    <ul class="list-disc list-inside text-gray-700 space-y-2 text-lg">
                        <li>Reduced Stress & Anxiety</li>
                        <li>Improved Concentration</li>
                        <li>Enhanced Emotional Regulation</li>
                        <li>Deeper Relaxation</li>
                    </ul>
                </div>
                <!-- Benefit Card 3 -->
                <div class="bg-white rounded-2xl card-shadow p-8 transform transition duration-300 ease-in-out card-hover border border-purple-100">
                    <div class="text-purple-600 mb-6 text-6xl flex justify-center">✨</div>
                    <h3 class="text-2xl font-bold mb-4 text-center text-gray-900">Spiritual Connection</h3>
                    <ul class="list-disc list-inside text-gray-700 space-y-2 text-lg">
                        <li>Mind-Body-Spirit Unification</li>
                        <li>Cultivated Mindfulness</li>
                        <li>Greater Self-Awareness</li>
                        <li>Inner Harmony & Contentment</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Types of Yoga Section -->
    <section id="types" class="py-16 md:py-24 bg-gradient-to-br from-green-50 to-emerald-100">
        <div class="container mx-auto px-4 md:px-8">
            <h2 class="text-4xl md:text-5xl font-extrabold text-center mb-16 text-emerald-900 drop-shadow-md">Explore Diverse Yoga Styles</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                <!-- Yoga Type Card 1 -->
                <div class="bg-white rounded-2xl card-shadow p-6 border border-emerald-200 transform transition duration-300 ease-in-out card-hover">
                    <img src="https://source.unsplash.com/random/400x250/?hatha-yoga,pose" alt="Hatha Yoga" class="w-full h-48 object-cover rounded-xl mb-4 shadow-md">
                    <h3 class="text-2xl font-bold mb-3 text-gray-900">Hatha Yoga</h3>
                    <p class="text-gray-700 text-lg">A foundational style focusing on basic postures and breathing, perfect for a slow, mindful pace.</p>
                </div>
                <!-- Yoga Type Card 2 -->
                <div class="bg-white rounded-2xl card-shadow p-6 border border-emerald-200 transform transition duration-300 ease-in-out card-hover">
                    <img src="https://source.unsplash.com/random/400x250/?vinyasa-yoga,flow" alt="Vinyasa Yoga" class="w-full h-48 object-cover rounded-xl mb-4 shadow-md">
                    <h3 class="text-2xl font-bold mb-3 text-gray-900">Vinyasa Yoga</h3>
                    <p class="text-gray-700 text-lg">Dynamic, flowing sequences that link breath to movement, offering a more active and creative practice.</p>
                </div>
                <!-- Yoga Type Card 3 -->
                <div class="bg-white rounded-2xl card-shadow p-6 border border-emerald-200 transform transition duration-300 ease-in-out card-hover">
                    <img src="https://source.unsplash.com/random/400x250/?restorative-yoga,relax" alt="Restorative Yoga" class="w-full h-48 object-cover rounded-xl mb-4 shadow-md">
                    <h3 class="text-2xl font-bold mb-3 text-gray-900">Restorative Yoga</h3>
                    <p class="text-gray-700 text-lg">A deeply relaxing practice using props to support the body, promoting passive stretching and rejuvenation.</p>
                </div>
                <!-- Yoga Type Card 4 -->
                <div class="bg-white rounded-2xl card-shadow p-6 border border-emerald-200 transform transition duration-300 ease-in-out card-hover">
                    <img src="https://source.unsplash.com/random/400x250/?ashtanga-yoga,strong" alt="Ashtanga Yoga" class="w-full h-48 object-cover rounded-xl mb-4 shadow-md">
                    <h3 class="text-2xl font-bold mb-3 text-gray-900">Ashtanga Yoga</h3>
                    <p class="text-gray-700 text-lg">A rigorous, athletic style with a fixed series of postures, building heat, strength, and stamina.</p>
                </div>
                <!-- Yoga Type Card 5 -->
                <div class="bg-white rounded-2xl card-shadow p-6 border border-emerald-200 transform transition duration-300 ease-in-out card-hover">
                    <img src="https://source.unsplash.com/random/400x250/?kundalini-yoga,energy" alt="Kundalini Yoga" class="w-full h-48 object-cover rounded-xl mb-4 shadow-md">
                    <h3 class="text-2xl font-bold mb-3 text-gray-900">Kundalini Yoga</h3>
                    <p class="text-gray-700 text-lg">Focuses on energetic awakening through chanting, breathwork, meditation, and specific poses.</p>
                </div>
                <!-- Yoga Type Card 6 -->
                <div class="bg-white rounded-2xl card-shadow p-6 border border-emerald-200 transform transition duration-300 ease-in-out card-hover">
                    <img src="https://source.unsplash.com/random/400x250/?yin-yoga,stretch" alt="Yin Yoga" class="w-full h-48 object-cover rounded-xl mb-4 shadow-md">
                    <h3 class="text-2xl font-bold mb-3 text-gray-900">Yin Yoga</h3>
                    <p class="text-gray-700 text-lg">Long-held, passive poses targeting deep connective tissues, enhancing flexibility and energetic flow.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- How to Get Started Section -->
    <section id="start" class="py-16 md:py-24 bg-gradient-to-br from-indigo-50 to-blue-50">
        <div class="container mx-auto px-4 md:px-8">
            <h2 class="text-4xl md:text-5xl font-extrabold text-center mb-16 text-blue-900 drop-shadow-md">Your First Steps on the Yoga Mat</h2>
            <div class="max-w-4xl mx-auto bg-white rounded-3xl card-shadow p-8 md:p-12 border border-blue-100">
                <p class="text-xl text-gray-700 mb-10 text-center leading-relaxed font-light">
                    Embarking on your yoga journey is a rewarding experience. Here are a few tips to help you begin with confidence and joy:
                </p>
                <div class="space-y-8">
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-blue-600 rounded-full p-4 text-white text-2xl font-bold mr-6 shadow-lg flex items-center justify-center w-14 h-14">1</div>
                        <div>
                            <h3 class="text-2xl font-bold mb-2 text-gray-900">Seek Guidance from a Qualified Instructor</h3>
                            <p class="text-gray-700 text-lg">Joining a beginner-friendly class at a local studio provides invaluable guidance for proper alignment and technique, minimizing injury risk.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-blue-600 rounded-full p-4 text-white text-2xl font-bold mr-6 shadow-lg flex items-center justify-center w-14 h-14">2</div>
                        <div>
                            <h3 class="text-2xl font-bold mb-2 text-gray-900">Gather Minimal Essentials</h3>
                            <p class="text-gray-700 text-lg">A comfortable yoga mat is your primary tool. Opt for breathable, flexible clothing. While props are helpful, they aren't crucial for initial practice.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-blue-600 rounded-full p-4 text-white text-2xl font-bold mr-6 shadow-lg flex items-center justify-center w-14 h-14">3</div>
                        <div>
                            <h3 class="text-2xl font-bold mb-2 text-gray-900">Practice Mindful Listening to Your Body</h3>
                            <p class="text-gray-700 text-lg">Yoga emphasizes self-awareness. Avoid pushing into pain. Modify poses as needed, respecting your unique physical boundaries. Consistency over perfection is key.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 bg-blue-600 rounded-full p-4 text-white text-2xl font-bold mr-6 shadow-lg flex items-center justify-center w-14 h-14">4</div>
                        <div>
                            <h3 class="text-2xl font-bold mb-2 text-gray-900">Embrace Patience and the Journey</h3>
                            <p class="text-gray-700 text-lg">Progress in yoga unfolds gradually. Focus on the present moment, your breath, and the joy of movement. Celebrate every small step towards peace and strength.</p>
                        </div>
                    </div>
                </div>
                <div class="text-center mt-14">
                    <p class="text-xl text-gray-600 italic font-semibold">"Yoga is the journey of the self, through the self, to the self."</p>
                    <p class="text-md text-gray-500 mt-2">— The Bhagavad Gita</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-16 md:py-24 bg-gradient-to-r from-teal-700 to-emerald-800 text-white">
        <div class="container mx-auto px-4 md:px-8 text-center">
            <h2 class="text-4xl md:text-5xl font-extrabold mb-8 drop-shadow-md">Connect With Our Community</h2>
            <p class="text-lg md:text-xl mb-10 font-light">Have questions, need guidance, or wish to share your yoga journey? We'd love to hear from you!</p>
            <div class="flex justify-center space-x-8 mb-10">
                <a href="mailto:info@yogaessence.com" class="text-white hover:text-teal-200 transition duration-300 transform hover:scale-110" aria-label="Email Us">
                    <svg class="w-12 h-12" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M2.003 5.884L10 12l8-6.116C17.218 5.309 16.205 5 15 5H9c-1.205 0-2.218.309-3 .884L2.003 5.884zm-.003 12.238V8.16L12 14.5l10-6.34v9.962C22 18.883 22 19 21 19H3c-1 0-1-.117-1-.878z"></path>
                    </svg>
                </a>
                <a href="https://facebook.com/yogaessence" target="_blank" rel="noopener noreferrer" class="text-white hover:text-teal-200 transition duration-300 transform hover:scale-110" aria-label="Visit us on Facebook">
                    <svg class="w-12 h-12" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm3.154 8.784h-1.92V9.664a.5.5 0 01.5-.5h.692v-1.89h-.813c-2.072 0-2.88 1.547-2.88 2.923v1.697H8.538v2.308h1.282v5.154h2.769v-5.154h1.92l.256-2.308z"></path>
                    </svg>
                </a>
                <a href="https://instagram.com/yogaessence" target="_blank" rel="noopener noreferrer" class="text-white hover:text-teal-200 transition duration-300 transform hover:scale-110" aria-label="Visit us on Instagram">
                    <svg class="w-12 h-12" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 2c2.717 0 3.056.01 4.122.06c1.065.05 1.79.217 2.427.465a4.912 4.912 0 011.77 1.151c.704.704 1.151 1.066 1.151 1.77a4.912 4.912 0 01.465 2.427c.05 1.066.06 1.405.06 4.122s-.01 3.056-.06 4.122a4.912 4.912 0 01-.465 2.427c-.422.704-.704 1.151-1.151 1.77a4.912 4.912 0 01-1.77 1.151c-1.065.465-1.79.704-2.427.915-.05 1.066-.06 1.405-.06 4.122s.01 3.056.06 4.122a4.912 4.912 0 01.465 2.427c.422.704.704 1.151 1.151 1.77a4.912 4.912 0 011.77 1.151c1.065.465 1.79.704 2.427.915.05 1.066.06 1.405.06 4.122s-.01 3.056-.06 4.122a4.912 4.912 0 01-.465 2.427c-.704.422-1.151.704-1.77 1.151a4.912 4.912 0 01-2.427.465c-1.066.05-1.405.06-4.122.06s-3.056-.01-4.122-.06a4.912 4.912 0 01-2.427-.465c-.704-.422-1.151-.704-1.77-1.151a4.912 4.912 0 01-1.151-1.77c-.465-1.065-.704-1.79-.915-2.427-.05-1.066-.06-1.405-.06-4.122s.01-3.056.06-4.122a4.912 4.912 0 01.465-2.427c.422-.704.704-1.151 1.151-1.77a4.912 4.912 0 011.77-1.151c1.065-.465 1.79-.704 2.427-.915.05-1.066.06-1.405.06-4.122zM12 7a5 5 0 100 10 5 5 0 000-10z"></path>
                    </svg>
                </a>
            </div>
            <p class="text-md font-light">&copy; 2025 Yoga Essence. All rights reserved.</p>
            <p class="text-xs mt-2 text-gray-300">Images sourced from Unsplash for demonstration purposes.</p>
        </div>
    </section>

    <!-- JavaScript for Mobile Menu -->
    <script>
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
        const closeMenuButton = document.getElementById('close-menu-button');

        mobileMenuButton.addEventListener('click', () => {
            mobileMenuOverlay.classList.remove('hidden');
        });

        closeMenuButton.addEventListener('click', () => {
            mobileMenuOverlay.classList.add('hidden');
        });

        // The mobileMenuLinks event listener is now embedded directly in the anchor tags
        // using onclick="mobileMenuOverlay.classList.add('hidden');" for simplicity and directness.
    </script>
</body>
</html>
"""

# Define the route for the home page
@app.route('/')
def home():
    # Render the HTML content directly as a string
    return render_template_string(HTML_CONTENT)

# Main entry point for the application
if __name__ == '__main__':
    # In a production OpenShift environment, Gunicorn or uWSGI would typically
    # serve the Flask app, so app.run() is mainly for local development/testing.
    app.run(debug=True, host='0.0.0.0', port=8080)
