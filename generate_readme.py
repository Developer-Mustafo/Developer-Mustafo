import os
import requests
from datetime import datetime

API_KEY = os.getenv("WAKATIME_API_KEY")
USER_AGENT = "github-readme-updater"

def get_wakatime_stats():
    url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
    headers = {"User-Agent": USER_AGENT, "Authorization": f"Bearer {API_KEY}"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()["data"]

def generate_readme(stats):
    total_time = stats["human_readable_total"]
    lang_stats = stats["languages"][:5]

    langs = "\n".join([
        f"- **{l['name']}**: {l['text']} ({l['percent']:.2f}%)"
        for l in lang_stats
    ])

    readme = f"""# 📊 Weekly Coding Stats

This README is automatically updated every 24 hours using **GitHub Actions** and **WakaTime API**.

## 🕒 Last 7 Days
- Total Coding Time: **{total_time}**

### 💻 Languages
{langs}

> Auto-updated on {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
"""
    return readme

if __name__ == "__main__":
    stats = get_wakatime_stats()
    readme = generate_readme(stats)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
