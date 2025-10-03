import requests
import matplotlib.pyplot as plt
from collections import defaultdict
import os
from datetime import datetime

# GitHub configuration
USERNAME = "Developer-Mustafo"
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def get_repos(username):
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching repos: {response.status_code}")
            break
        page_repos = response.json()
        if not page_repos:
            break
        repos.extend(page_repos)
        page += 1
    return repos

def analyze_languages(repos):
    language_bytes = defaultdict(int)
    for repo in repos:
        if repo.get('language'):
            language_bytes[repo['language']] += repo.get('size', 1)
    return language_bytes

def create_language_chart(languages, username):
    if not languages:
        print("No language data found")
        return
    
    # PAPKA YARATISH - BU YERNI QO'SHING
    os.makedirs('scripts', exist_ok=True)
    
    labels, sizes = [], []
    colors = plt.cm.Set3.colors
    for lang, bytes_count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
        labels.append(lang)
        sizes.append(bytes_count)
    plt.figure(figsize=(12, 8))
    wedges, texts, autotexts = plt.pie(
        sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        colors=colors[:len(labels)], textprops={'fontsize': 12}
    )
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    plt.title(f'Programming Languages Distribution\n@{username}', fontsize=16, fontweight='bold', pad=20)
    plt.legend(wedges, [f'{label}: {size:,} KB' for label, size in zip(labels, sizes)],
               title="Languages", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.tight_layout()
    
    # Endi faqat scripts/ papkasiga saqlaymiz
    path = 'scripts/languages.png'
    plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"📈 Chart saved to {path}")
    plt.close()

def generate_stats_summary(repos, languages):
    summary = f"""
# GitHub Language Statistics
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Username:** {USERNAME}
**Total Repositories:** {len(repos)}
**Languages Used:** {len(languages)}

## Language Distribution:
"""
    total_bytes = sum(languages.values())
    for lang, bytes_count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
        percentage = (bytes_count / total_bytes) * 100
        summary += f"- **{lang}:** {percentage:.1f}% ({bytes_count:,} KB)\n"
    return summary

if __name__ == "__main__":
    print("🚀 Starting GitHub language analysis...")
    
    # PAPKA YARATISH - BU YERNI HAM QO'SHING
    os.makedirs('scripts', exist_ok=True)
    
    repos = get_repos(USERNAME)
    print(f"📁 Found {len(repos)} repositories")
    if repos:
        languages = analyze_languages(repos)
        print(f"📊 Found {len(languages)} programming languages")
        create_language_chart(languages, USERNAME)
        summary = generate_stats_summary(repos, languages)
        print(summary)
        
        # Markdown faylini saqlash
        with open('scripts/language_stats.md', 'w') as f:
            f.write(summary)
        print("✅ Stats saved to scripts/language_stats.md")
    else:
        print("❌ No repositories found or error fetching data")
