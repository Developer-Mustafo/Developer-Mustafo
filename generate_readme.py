import os
import requests
from datetime import datetime, timezone
from urllib.parse import quote_plus

# -------------------------
# CONFIG
# -------------------------
API_KEY = os.getenv("WAKATIME_API_KEY")
if not API_KEY:
    print("⚠️ WAKATIME_API_KEY topilmadi. Stats bo'lmaydi.")
    
URL = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
HEADERS = {"Authorization": f"Basic {API_KEY}"} if API_KEY else {}

GIF_CANDIDATES = [
    "https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif",
    "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",
    "https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif"
]

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

TYPING_BASE = "https://readme-typing-svg.demolab.com"
TYPING_PARAMS = {"font": "Fira+Code", "pause": "800", "color": "FF6A00", "width": "760", "height": "90"}

DOWNLOAD_GIF = os.getenv("DOWNLOAD_GIF", "false").lower() in ("1", "true", "yes")
LOCAL_GIF_PATH = "assets/animation.gif"

CONTACT_INFO = [
    {"name": "Telegram", "url": "https://t.me/rahim_mustafo_x", "badge_color": "1DA1F2", "logo": "telegram"},
    {"name": "Gmail", "url": "mailto:rahim.mustafo.x@gmail.com", "badge_color": "D14836", "logo": "gmail"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/mustafo-rahim-4a0384324", "badge_color": "0077B5", "logo": "linkedin"}
]

README_PATH = "README.md"

# -------------------------
# HELPERS
# -------------------------
def get_wakatime_stats():
    if not API_KEY:
        return {}
    try:
        r = requests.get(URL, headers=HEADERS, timeout=10)
        return r.json().get("data", {}) if r.status_code == 200 else {}
    except Exception as e:
        print(f"⚠️ WakaTime stats olishda xato: {e}")
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
    lines_joined = ";".join([l.replace(";", ",") for l in lines])
    qs = "&".join(f"{k}={quote_plus(str(v))}" for k, v in params.items())
    return f"{TYPING_BASE}?{qs}&lines={quote_plus(lines_joined)}"

def generate_contact_badges(contacts):
    badges = []
    for c in contacts:
        badges.append(
            f'<a href="{c["url"]}">'
            f'<img src="https://img.shields.io/badge/{c["name"]}-{c["badge_color"]}?style=for-the-badge&logo={c["logo"]}&logoColor=white" />'
            f'</a>'
        )
    return " &nbsp; ".join(badges)

def generate_readme(stats, gif_url=None, local_gif_path=None):
    total_time = stats.get("human_readable_total", "0 mins")
    daily_avg = stats.get("human_readable_daily_average", "0 mins")
    languages = stats.get("languages", [])[:6]

    stats_table = ""
    for lang in languages:
        name = lang.get('name', 'Unknown')
        time = lang.get('text', '0 mins')
        percent = lang.get('percent', 0.0)
        bar = create_progress_bar(percent)
        stats_table += f"`{bar}` **{percent:.1f}%** {name} - {time}\n"

    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    about_svg = make_typing_svg_url(ABOUT_LINES, **TYPING_PARAMS)
    tech_svg  = make_typing_svg_url(TECH_LINES, **TYPING_PARAMS)

    if local_gif_path:
        gif_tag = f'<div align="center">\n<img src="{local_gif_path}" width="680" alt="Coding animation"/>\n</div>\n\n'
    elif gif_url:
        gif_tag = f'<div align="center">\n<img src="{gif_url}" width="680" alt="Coding animation"/>\n</div>\n\n'
    else:
        gif_tag = ""

    badges_md = generate_contact_badges(CONTACT_INFO)

    readme = f"""## 👋 Hello, I'm Mustafo!

### 🚀 Android & Backend Developer | Kotlin, Python & AI Enthusiast

{gif_tag}
---

## 💡 About Me

<div align="center">
  <img src="{about_svg}" alt="About - typing animation"/>
</div>

---

## 🛠️ Tech Stack

<div align="center">
  <img src="{tech_svg}" alt="Tech stack - typing animation"/>
</div>

---

## 📊 Weekly Development Analytics

### ⏱️ Coding Time (Last 7 Days)
- **Total Time**: {total_time}
- **Daily Average**: {daily_avg}

### 💻 Top Languages This Week
{stats_table if stats_table else "_No coding activity this week_"}

---

## 🤝 Contact Me

<div align="center">
  {badges_md}
</div>

---

<div align="center">
### ⚡ Coding Philosophy  
*"Write code that not only works but tells a story!"*  

**📅 Last Updated**: {updated_time}
</div>
"""
    return readme

# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    print("🚀 Generating README with Contact Me section...")

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
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_text)

    print("✅ README.md updated successfully!")
