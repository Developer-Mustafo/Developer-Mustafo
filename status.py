import requests
import matplotlib.pyplot as plt
from collections import defaultdict
import os
from datetime import datetime

# GitHub configuration
USERNAME = "Developer-Mustafo"
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def get_repos(username):
    """Fetch all repositories for a user"""
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
    """Analyze language distribution"""
    language_bytes = defaultdict(int)
    
    for repo in repos:
        if repo.get('language'):
            # Use size as weight instead of simple count
            language_bytes[repo['language']] += repo.get('size', 1)
    
    return language_bytes

def create_language_chart(languages, username):
    """Create a beautiful language distribution chart"""
    if not languages:
        print("No language data found")
        return
    
    # Prepare data
    labels = []
    sizes = []
    colors = plt.cm.Set3.colors
    
    for lang, bytes_count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
        labels.append(lang)
        sizes.append(bytes_count)
    
    # Create figure
    plt.figure(figsize=(12, 8))
    
    # Create pie chart
    wedges, texts, autotexts = plt.pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%',
        startangle=90,
        colors=colors[:len(labels)],
        textprops={'fontsize': 12}
    )
    
    # Style percentage texts
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    plt.title(
        f'Programming Languages Distribution\n@{username}', 
        fontsize=16, 
        fontweight='bold', 
        pad=20
    )
    
    # Add legend
    plt.legend(
        wedges, 
        [f'{label}: {size:,} KB' for label, size in zip(labels, sizes)],
        title="Languages",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1)
    )
    
    plt.tight_layout()
    
    # Save in multiple locations
    save_paths = ['languages.png', 'scripts/languages.png']
    for path in save_paths:
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
    
    print(f"Chart generated for {len(languages)} languages")
    plt.close()

def generate_stats_summary(repos, languages):
    """Generate a summary of statistics"""
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
    
    # Fetch repositories
    repos = get_repos(USERNAME)
    print(f"📁 Found {len(repos)} repositories")
    
    if repos:
        # Analyze languages
        languages = analyze_languages(repos)
        print(f"📊 Found {len(languages)} programming languages")
        
        # Create visualization
        create_language_chart(languages, USERNAME)
        
        # Generate summary
        summary = generate_stats_summary(repos, languages)
        print(summary)
        
        # Save summary to file
        with open('scripts/language_stats.md', 'w') as f:
            f.write(summary)
            
    else:
        print("❌ No repositories found or error fetching data")
