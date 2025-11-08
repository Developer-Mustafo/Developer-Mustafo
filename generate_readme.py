import os
import requests
from datetime import datetime, timezone
from urllib.parse import quote_plus

# -------------------------
# CONFIG
# -------------------------
API_KEY = os.getenv("WAKATIME_API_KEY")
if not API_KEY:
    raise SystemExit("🚫 WAKATIME_API_KEY environment variable is missing!")

URL = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
HEADERS = {"Authorization": f"Basic {API_KEY}"}

# GIF candidates (fallbacks) — ishlaydigan birinchisini tanlaydi
GIF_CANDIDATES = [
    "https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif",
    "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",
    "https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif"
]

# README uchun typing lines (bu yerga kerakli izohli/jasosiy satrlarni qo'shing)
ABOUT_LINES = [
    "Android Developer — Kotlin & Jetpack Compose expert",
    "Backend Developer — Spring Boot & Ktor",
    "Telegram Bots — Aiogram, automation & AI integrations",
    "Passionate about clean architecture, tests & performance"
]

TECH_LINES = [
    "Kotlin — Primary Android language, concise and safe",
    "Jetpack Compose — Declarative UI for faster delivery",
    "Room — Reliable local persistence with SQL",
    "Retrofit — Clean REST clients with OkHttp",
    "Python (Aiogram) — Telegram bots & automation",
    "PostgreSQL — Production-grade relational DB"
]

# Typing SVG settings
TYPING_BASE = "https://readme-typing-svg.demolab.com"
TYPING_PARAMS = {
    "font": "Fira+Code",
    "pause": "800",
    "color": "FF6A00",
    "width": "760",
    "height": "90"
}

# GIF download toggle: agar LOCAL_GIF=true bo'lsa yuklab olinadi va README localga bog'lanadi
DOWNLOAD_GIF = os.getenv("DOWNLOAD_GIF", "false").lower() in ("1", "true", "yes")
LOCAL_GIF_PATH = "assets/animation.gif"  # agar DOWNLOAD_GIF=true bo'lsa shu joyga yuklanadi

# -------------------------
# HELPERS
# -------------------------
def get_wakatime_stats():
    try:
        r = requests.get(URL, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            return r.json().get("data", {})
        else:
            print(f"❌ WakaTime API Error: {r.status_code} - {r.text}")
            return {}
    except Exception as e:
        print(f"⚠️ Warning while fetching WakaTime stats: {e}")
        return {}

def create_progress_bar(percentage, length=15):
    filled = int(round(length * percentage / 100))
    return '█' * filled + '░' * (length - filled)

def validate_image_url(url, timeout=5):
    try:
        head = requests.head(url, timeout=timeout, allow_redirects=True)
        if head.status_code == 200 and 'image' in head.headers.get('Content-Type', ''):
            return True
        get = requests.get(url, stream=True, timeout=timeout)
        return get.status_code == 200 and 'image' in get.headers.get('Content-Type', '')
    except Exception:
        return False

def choose_working_gif(candidates):
    for u in candidates:
        if validate_image_url(u):
            return u
    return None

def download_gif(url, path=LOCAL_GIF_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with requests.get(url, stream=True, timeout=20) as r:
            r.raise_for_status()
            with open(path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        return path
    except Exception as e:
        print(f"⚠️ GIF yuklashda xato: {e}")
        return None

def make_typing_svg_url(lines, **params):
    """readme-typing-svg uchun URL yaratadi. 'lines' ro'yxat."""
    lines_joined = ";".join([l.replace(";", ",") for l in lines])
    p = params.copy()
    p["lines"] = lines_joined
    qs = "&".join(f"{k}={quote_plus(str(v))}" for k, v in p.items() if v is not None)
    return f"{TYPING_BASE}?{qs}"

# -------------------------
# README GENERATION
# -------------------------
def generate_readme(stats, gif_url=None, local_gif_path=None):
    total_time = stats.get("human_readable_total", "0 mins") if stats else "0 mins"
    daily_avg = stats.get("human_readable_daily_average", "0 mins") if stats else "0 mins"
    languages = stats.get("languages", [])[:6] if stats else []

    # languages table
    if languages:
        stats_table = "\n"
        for lang in languages:
            name = lang.get('name', 'Unknown')
            time = lang.get('text', '0 mins')
            percent = lang.get('percent', 0.0)
            bar = create_progress_bar(percent)
            stats_table += f"\n`{bar}` **{percent:.1f}%** {name} - {time}\n"
    else:
        stats_table = "_No coding activity this week_"

    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Typing SVG URLs
    about_svg = make_typing_svg_url(ABOUT_LINES, **TYPING_PARAMS)
    tech_svg  = make_typing_svg_url(TECH_LINES, **TYPING_PARAMS)

    # GIF tag (prioritize local path if exists)
    if local_gif_path:
        gif_tag = f'<div align="center">  \n  <img src="{local_gif_path}" width="680" alt="Coding animation"/>\n</div>\n\n'
    elif gif_url:
        gif_tag = f'<div align="center">  \n  <img src="{gif_url}" width="680" alt="Coding animation"/>\n</div>\n\n'
    else:
        gif_tag = ""

    readme = f"""## 👋 Hello, I'm Mustafo!

### 🚀 Android & Backend Developer | Kotlin, Python & AI Enthusiast

I’m a passionate developer who loves building modern, high-performance applications — from **Android apps with Jetpack Compose** to **AI-powered Telegram bots** using Python.  
Clean architecture, elegant UI, and smart automation are what I always aim for.

{gif_tag}
---

## 💡 About Me

<div align="center">
  <img src="{about_svg}" alt="About - typing animation"/>
</div>

- 🎯 **Android Developer** — Kotlin, Jetpack Compose & performant apps  
- ⚙️ **Backend Developer** — Spring Boot & Ktor services  
- 🤖 **Telegram Bots** — Aiogram, automation & AI integrations  
- 🧠 **Focus** — Clean architecture, testing, and maintainability

---

## 🛠️ Tech Stack (with quick notes)

<div align="center">
  <img src="{tech_svg}" alt="Tech stack - typing animation"/>
</div>

- **Kotlin** — Primary Android language, concise and null-safe.  
- **Jetpack Compose** — Declarative UI for fast iteration and smoother UX.  
- **Room** — Local SQL storage; stable and easy to migrate.  
- **Retrofit** — Robust HTTP client for REST APIs (with OkHttp).  
- **Python (Aiogram)** — Telegram bots, automation tasks, quick prototypes.  
- **PostgreSQL** — Reliable relational database for production workloads.

---

## 📊 Weekly Development Analytics

### ⏱️ Coding Time (Last 7 Days)
- **Total Time**: {total_time}
- **Daily Average**: {daily_avg}

### 💻 Top Languages This Week
{stats_table}

---

## 📈 GitHub Stats

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Developer-Mustafo&show_icons=true&theme=radical&hide_border=true)  
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Developer-Mustafo&layout=compact&theme=radical&hide_border=true)

</div>

---

## 🤝 Let's Connect

- 📧 **Email**: [rahim.mustafo.x@gmail.com](mailto:rahim.mustafo.x@gmail.com)  
- 💼 **LinkedIn**: [linkedin.com/in/mustafo-rahim-4a0384324](https://www.linkedin.com/in/mustafo-rahim-4a0384324)  
- 💬 **Telegram**: [t.me/rahim_mustafo_x](https://t.me/rahim_mustafo_x)  

---

<div align="center">

### ⚡ Coding Philosophy  
*"Write code that not only works but tells a story!"*  

**📅 Last Updated**: {updated_time}

*This README is automatically updated with WakaTime stats.*

</div>
"""
    return readme

# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    print("🚀 Generating animated README...")

    stats = get_wakatime_stats()
    selected_gif = choose_working_gif(GIF_CANDIDATES)
    local_gif = None

    if selected_gif:
        print(f"ℹ️ Using GIF: {selected_gif}")
        if DOWNLOAD_GIF:
            p = download_gif(selected_gif)
            if p:
                local_gif = p
    else:
        print("⚠️ Hech qanday GIF topilmadi — README GIF bo'lmaydi.")

    readme_text = generate_readme(stats, gif_url=selected_gif if not local_gif else None, local_gif_path=local_gif)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_text)

    print("✅ README.md updated with animations!")
    if local_gif:
        print(f"✅ GIF saved to: {local_gif}")
    print("🎉 Barchasi tayyor, aka!")
