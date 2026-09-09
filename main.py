
from flask import Flask, render_template_string, request, redirect, flash
import datetime

app = Flask(__name__)
app.secret_key = "teri_dusri_website_secret"

# Data - Isko tu apne hisab se badal sakta hai
MY_DATA = {
    "name":"RUPESH",
    "role": "Python Developer & Builder",
    "about": "Maine apni pehli website banayi, ye meri dusri hai. Ab main complex cheezein bana raha hu.",
}

PROJECTS = [
    {"title": "My First Website", "desc": "Meri pehli website jo Render pe live hai.", "link": "https://my-first-website-x9pu.onrender.com", "tech": "Flask"},
    {"title": "Weather App", "desc": "City daalo, weather bataega.", "link": "#", "tech": "API + Python"},
    {"title": "To-Do Pro", "desc": "Task manager with cool UI.", "link": "#", "tech": "Flask + JS"},
]

BLOGS = [
    {"id": 1, "title": "Maine Pehli Website Kaise Banayi", "date": "09 Sep 2026", "content": "Pehle mujhe laga bahut mushkil hai, par Flask se asaan ho gaya..."},
]

# --- HTML Template (Sab isi me hai, alag file ki zarurat nahi) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ data.name }} - Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
    <style>body{font-family:'Space Grotesk', sans-serif;}</style>
</head>
<body class="bg-[#0a0a0a] text-white">
    <nav class="p-6 flex justify-between max-w-6xl mx-auto">
        <h1 class="text-xl font-bold">.{{ data.name.split()[0] }}</h1>
        <div class="flex gap-6 text-sm text-gray-400"><a href="#projects">Projects</a><a href="#blog">Blog</a><a href="#contact">Contact</a></div>
    </nav>

    <section class="max-w-6xl mx-auto px-6 py-20">
        <h2 class="text-6xl font-bold leading-[1.1]">I build <span class="text-yellow-400">websites</span><br>that people remember.</h2>
        <p class="text-gray-400 mt-6 max-w-xl">{{ data.about }}</p>
        <p class="mt-4 text-sm">Pehli website: <a href="https://my-first-website-x9pu.onrender.com" class="text-yellow-400 underline">my-first-website-x9pu.onrender.com</a></p>
    </section>

    <section id="projects" class="max-w-6xl mx-auto px-6 py-10">
        <h3 class="text-2xl font-bold mb-6">Projects ({{ projects|length }})</h3>
        <div class="grid md:grid-cols-3 gap-4">
            {% for p in projects %}
            <div class="bg-[#1a1a1a] p-6 rounded-2xl border border-white/10 hover:border-yellow-400/50 transition">
                <span class="text-xs bg-yellow-400 text-black px-2 py-1 rounded-full">{{ p.tech }}</span>
                <h4 class="text-lg font-bold mt-4">{{ p.title }}</h4>
                <p class="text-sm text-gray-400 mt-2">{{ p.desc }}</p>
                <a href="{{ p.link }}" class="text-sm mt-4 inline-block underline">Live View -></a>
            </div>
            {% endfor %}
        </div>
    </section>

    <section id="blog" class="max-w-6xl mx-auto px-6 py-10">
        <h3 class="text-2xl font-bold mb-6">Blog</h3>
        {% for b in blogs %}
        <div class="bg-[#1a1a1a] p-6 rounded-2xl mb-4 border border-white/5">
            <div class="flex justify-between"><h4 class="font-bold">{{ b.title }}</h4><span class="text-xs text-gray-500">{{ b.date }}</span></div>
            <p class="text-sm text-gray-400 mt-2">{{ b.content }}</p>
        </div>
        {% endfor %}
    </section>

    <section id="contact" class="max-w-6xl mx-auto px-6 py-20">
        <h3 class="text-3xl font-bold">Have an idea? Let's talk.</h3>
        <form method="POST" action="/contact" class="mt-6 max-w-md flex flex-col gap-3">
            <input name="name" placeholder="Your Name" required class="bg-[#1a1a1a] p-3 rounded-lg border border-white/10">
            <input name="email" placeholder="Your Email" required class="bg-[#1a1a1a] p-3 rounded-lg border border-white/10">
            <textarea name="message" placeholder="Message" required class="bg-[#1a1a1a] p-3 rounded-lg border border-white/10"></textarea>
            <button class="bg-yellow-400 text-black p-3 rounded-lg font-bold">Send Message</button>
        </form>
        {% with messages = get_flashed_messages() %}{% if messages %}<p class="mt-4 text-green-400">{{ messages[0] }}</p>{% endif %}{% endwith %}
    </section>

    <footer class="text-center text-xs text-gray-600 py-10">Built with ❤️ in Patna - 2026</footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, data=MY_DATA, projects=PROJECTS, blogs=BLOGS)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    # Yaha tu email send ka logic laga sakta hai, abhi ke liye bas flash message
    print(f"New Message from {name}: {request.form.get('message')}")
    flash(f"Thanks {name}! Message mil gaya, jaldi reply karunga.")
    return redirect('/#contact')

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=10000 )
