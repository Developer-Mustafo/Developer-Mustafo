```python
import os
import requests
from datetime import datetime, timezone

# API keyni environment variables dan olish
API_KEY = os.getenv("WAKATIME_API_KEY")

# API kalitni tekshirish
if not API_KEY:
    raise SystemExit("🚫 WAKATIME_API_KEY environment variable is missing!")

URL = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
HEADERS = {
    "Authorization": f"Basic {API_KEY}"
}

def get_wakatime_stats():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {})
        else:
            print(f"❌ API Error {response.status_code}")
            return {}
            
    except Exception as e:
        print(f"⚠️ Warning: {e}")
        return {}

def create_progress_bar(percentage, length=15):
    """Progress bar yaratish"""
    filled = int(round(length * percentage / 100))
    bar = '█' * filled + '░' * (length - filled)
    return bar

def generate_readme(stats):
    # Asosiy statistikalar
    total_time = stats.get("human_readable_total", "0 mins") if stats else "0 mins"
    daily_avg = stats.get("human_readable_daily_average", "0 mins") if stats else "0 mins"
    
    # Til statistikasi
    languages = stats.get("languages", [])[:6] if stats else []
    
    if languages:
        stats_table = "\n"
        for lang in languages:
            name = lang['name']
            time = lang.get('text', '0 mins')
            percent = lang.get('percent', 0)
            bar = create_progress_bar(percent)
            stats_table += f"`{bar}` **{percent:.1f}%** {name} - {time}\n"
    else:
        stats_table = "_No coding activity this week_"

    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    readme_content = f"""## 👋 Hello, I'm Mustafo!

### 🚀 Android Developer & Kotlin Enthusiast

I'm a passionate Android developer specializing in modern mobile technologies. I love creating clean, efficient, and user-friendly applications.

## 📊 Weekly Development Analytics

### ⏱️ Coding Time (Last 7 Days)
- **Total Time**: {total_time}
- **Daily Average**: {daily_avg}

### 💻 Top Languages This Week
{stats_table}

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

![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=Developer-Mustafo&theme=radical&hide_border=true)

</div>

## 🤝 Let's Connect

- **📧 Email**: your.email@example.com
- **💼 LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- **📱 Telegram**: [@yourusername](https://t.me/yourusername)
- **🌐 Portfolio**: [yourportfolio.com](https://yourportfolio.com)

---

<div align="center">

### ⚡ Coding Philosophy
*"Write code that not only works but tells a story!"*

**📅 Last Updated**: {updated_time}

*This README is automatically updated with WakaTime stats*

</div>
"""
    return readme_content

if __name__ == "__main__":
    print("🚀 Starting WakaTime stats update...")
    
    # Stats olish
    stats_data = get_wakatime_stats()
    
    # README yaratish
    readme_text = generate_readme(stats_data)
    
    # Faylga yozish
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_text)
    
    print("✅ README.md updated successfully!")
    print("🎉 Process completed successfully!")
```
