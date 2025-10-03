import os
import requests

GITHUB_USERNAME = "Developer-Mustafo"
README_PATH = "README.md"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Get all repos (public + private)
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
repos_url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100&type=owner"
repos = requests.get(repos_url, headers=headers).json()

lang_count = {}
for repo in repos:
    lang = repo["language"]
    if lang:
        lang_count[lang] = lang_count.get(lang, 0) + 1

# Calculate percentage
total = sum(lang_count.values())
lang_percent = {lang: int(count/total*100) for lang, count in lang_count.items()}

# Build markdown
lang_md = "\n".join([f"- {lang}: {percent}%" for lang, percent in lang_percent.items()])

# Update README
with open(README_PATH, "r", encoding="utf-8") as f:
    readme = f.read()

if "<!-- LANGUAGES USAGE WILL BE UPDATED AUTOMATICALLY -->" in readme:
    new_readme = readme.replace(
        "<!-- LANGUAGES USAGE WILL BE UPDATED AUTOMATICALLY -->",
        lang_md
    )

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_readme)

print("README.md updated successfully.")