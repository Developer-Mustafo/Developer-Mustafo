import requests
import matplotlib.pyplot as plt
from collections import defaultdict

# GitHub foydalanuvchi nomi
USERNAME = "Developer-Mustafo"

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    repos = requests.get(url).json()
    return repos

def get_languages(repos):
    langs = defaultdict(int)
    for repo in repos:
        if repo.get("language"):
            langs[repo["language"]] += 1
    return langs

def make_chart(langs):
    labels = list(langs.keys())
    sizes = list(langs.values())

    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Repositories by Language")
    plt.savefig("languages.png")

if __name__ == "__main__":
    repos = get_repos(USERNAME)
    langs = get_languages(repos)
    make_chart(langs)
