from github import Github
import os
import re

# GitHub token (Secrets orqali oling)
g = Github(os.environ["GITHUB_TOKEN"])
user = g.get_user()
repos = user.get_repos()  # Public va private farqi yo'q

# Icon mapping (dynamic, mashhur tillar uchun)
lang_icons = {
    "Python": "🐍",
    "Java": "☕",
    "Kotlin": "🤖",
    "Rust": "🦀",
    "C++": "💻",
    "JavaScript": "📜",
    "Go": "🐹",
    "TypeScript": "🔷",
}

# Tillarni hisoblash
lang_count = {}
total = 0
for repo in repos:
    lang = repo.language
    if lang:
        lang_count[lang] = lang_count.get(lang, 0) + 1
        total += 1

def progress_bar(percentage):
    bars = int(percentage // 5)  # 20 barli progress
    return "█" * bars + "░" * (20 - bars)

# README Languages section
readme_lang_section = "### 📊 Languages Usage\n\n"
for lang, count in lang_count.items():
    percent = round((count / total) * 100)
    icon = lang_icons.get(lang, "📌")
    readme_lang_section += f"- {icon} {lang:<10} {progress_bar(percent)} {percent}%\n"

# README.md faylini yangilash
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"### 📊 Languages Usage\n.*?\n\n"
if re.search(pattern, content, flags=re.DOTALL):
    content = re.sub(pattern, readme_lang_section + "\n", content, flags=re.DOTALL)
else:
    content += "\n" + readme_lang_section + "\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
