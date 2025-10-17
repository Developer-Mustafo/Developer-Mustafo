import os
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

# .env faylni yuklash
load_dotenv()

# API keyni .env dan olish
API_KEY = os.getenv("WAKATIME_API_KEY")

# API kalitni tekshirish
if not API_KEY:
    raise SystemExit("🚫 WAKATIME_API_KEY environment variable is missing!")

if not API_KEY.startswith("waka_"):
    raise SystemExit("🚫 WAKATIME_API_KEY format is invalid! Make sure it starts with 'waka_'.")

URL = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
HEADERS = {
    "Authorization": f"Basic {API_KEY}"
}


def get_wakatime_stats():
    try:
        print(f"🔑 API Key (first 10 chars): {API_KEY[:10]}...")

        response = requests.get(URL, headers=HEADERS)

        print(f"🔍 Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            return data.get("data", {})
        elif response.status_code == 401:
            print("❌ 401 Unauthorized - API key not valid")
            print("💡 Solutions:")
            print("   1. Go to https://wakatime.com/api-key")
            print("   2. Generate a NEW API key")
            print("   3. Update your .env file with the new key")
            print(f"   4. Current key format: {API_KEY[:10]}...")
            raise SystemExit("Authentication failed")
        else:
            print(f"❌ API Error {response.status_code}: {response.text}")
            raise SystemExit(f"API request failed with status {response.status_code}")

    except Exception as e:
        raise SystemExit(f"❗ Error: {e}")


def create_progress_bar(percentage, length=20):
    """Progress bar yaratish"""
    filled = int(round(length * percentage / 100))
    bar = '█' * filled + '░' * (length - filled)
    return bar


def generate_readme(stats):
    if not stats:
        total_time = "0 mins"
        langs_text = "_No coding activity this week_"
        stats_table = ""
    else:
        total_time = stats.get("human_readable_total", "0 mins")
        languages = stats.get("languages", [])
        daily_average = stats.get("human_readable_daily_average", "0 mins")

        if languages:
            # Progress bar bilan chiroyli jadval
            stats_table = "\n"
            for lang in languages[:6]:
                name = lang['name']
                time = lang.get('text', '0 mins')
                percent = lang.get('percent', 0)
                bar = create_progress_bar(percent)
                stats_table += f"`{bar}` {percent:.1f}% **{name}** - {time}\n"

            # Text formatda ham
            langs_text = "\n".join([
                f"- **{lang['name']}**: {lang.get('text', '0 mins')} ({lang.get('percent', 0):.1f}%)"
                for lang in languages[:5]
            ])
        else:
            stats_table = ""
            langs_text = "_No language data available_"

    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    readme_content = f"""# 👋 Hello, I'm Mustafo!

## 🚀 Android Developer & Kotlin Enthusiast

I'm a passionate Android developer specializing in modern mobile technologies. I love creating clean, efficient, and user-friendly applications.

## 📊 Weekly Development Analytics

### ⏱️ Coding Time (Last 7 Days)
- **Total Time**: {total_time}
- **Daily Average**: {stats.get('human_readable_daily_average', '0 mins') if stats else '0 mins'}

### 💻 Top Languages This Week
{stats_table if stats_table else langs_text}

### 🎯 Current Focus
- **Primary Language**: Kotlin
- **Specialization**: Android Development
- **Interests**: Mobile Apps, Clean Architecture, Jetpack Compose

## 🛠️ Tech Stack

**Mobile Development:**
- **Kotlin** - Primary language for Android development
- **Java** - Enterprise-level Android applications  
- **XML** - UI/UX design and layouts
- **Jetpack Compose** - Modern declarative UI
- **Room Database** - Local data persistence
- **Retrofit** - REST API integration
- **Coroutines & Flow** - Asynchronous programming

**Other Technologies:**
- **Python** - Scripting and automation
- **Git** - Version control
- **Android Studio** - Primary IDE

## 📈 GitHub Stats

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Developer-Mustafo&show_icons=true&theme=radical&hide_border=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Developer-Mustafo&layout=compact&theme=radical&hide_border=true)

</div>

## 🔥 Current Streak

<div align="center">

![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=Developer-Mustafo&theme=radical&hide_border=true)

</div>

## 🤝 Let's Connect

- **📧 Email**: your.email@example.com
- **💼 LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- **📱 Telegram**: [@yourusername](https://t.me/yourusername)
- **🌐 Portfolio**: [yourportfolio.com](https://yourportfolio.com)

## 💡 Currently Learning

- Advanced Kotlin Coroutines
- Jetpack Compose Mastery  
- Clean Architecture Patterns
- Testing in Android
- CI/CD for Mobile Apps

---

<div align="center">

### ⚡ Coding Philosophy
*"Write code that not only works but tells a story!"*

**📅 Last Updated**: {updated_time}

*This README is automatically updated with WakaTime stats*

</div>
"""
    return readme_content


def save_readme(content):
    try:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ README.md successfully updated!")
    except Exception as e:
        raise SystemExit(f"❌ Error saving README: {e}")


if __name__ == "__main__":
    print("🚀 Starting WakaTime stats update...")

    # Stats olish
    stats_data = get_wakatime_stats()

    # README yaratish
    readme_text = generate_readme(stats_data)

    # Faylga yozish
    save_readme(readme_text)

    print("🎉 Process completed successfully!")