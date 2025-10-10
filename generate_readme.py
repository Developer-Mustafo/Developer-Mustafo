import os
import requests
from datetime import datetime

API_KEY = os.getenv("WAKATIME_API_KEY")
URL = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
HEADERS = {
    "User-Agent": "GitHubAction-WakaTimeUpdater",
    "Authorization": f"Bearer {API_KEY}"
}


def get_wakatime_stats():
    try:
        res = requests.get(URL, headers=HEADERS)
        print("🔍 Status Code:", res.status_code)
        if not res.ok:
            print("❌ Response Body:", res.text)
            raise SystemExit(f"WakaTime API error: {res.status_code}")
        data = res.json()
        return data.get("data", {})
    except Exception as e:
        raise SystemExit(f"❗ Error fetching WakaTime stats: {e}")


def generate_readme(stats):
    total_time = stats.get("human_readable_total", "0 mins")
    lang_stats = stats.get("languages", [])[:5]

    if not lang_stats:
        langs_text = "_No data available yet._"
    else:
        langs_text = "\n".join([
            f"- **{lang['name']}**: {lang['text']} ({lang['percent']:.2f}%)"
            for lang in lang_stats
        ])

    updated_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    readme = f"""# 📊 Weekly Coding Stats

This README is automatically updated using **WakaTime API** and **GitHub Actions**.

## 🕒 Last 7 Days
- Total Coding Time: **{total_time}**

### 💻 Top Languages
{langs_text}

> Auto-updated on **{updated_time}**
"""
    return readme


def save_readme(content: str):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ README.md updated successfully!")


if __name__ == "__main__":
    if not API_KEY:
        raise SystemExit("🚫 WAKATIME_API_KEY environment variable is missing!")
    stats = get_wakatime_stats()
    readme_content = generate_readme(stats)
    save_readme(readme_content)
