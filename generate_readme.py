import os
from datetime import datetime, timezone

# -------------------------
# CONFIG / USER DATA
# -------------------------
USER = {
    "name": "Mustafo Rahim",
    "github_username": "Developer-Mustafo",
    "email": "mustaforahimov30@gmail.com",
    "telegram": "https://t.me/rahim_mustafo_x",
    "linkedin": "https://www.linkedin.com/in/mustafo-rahim-4a0384324",
    "portfolio": "http://davomat-app.uz",
    "about_lines": [
        "🚀 Full Stack Android Developer",
        "🤖 Telegram Bot Specialist",
        "⚡ Backend API Architect",
        "💡 Clean Code Enthusiast"
    ],
    "skills": {
        "Languages": ["java", "kotlin", "javascript", "python"],
        "Mobile & Web": ["androidstudio", "react", "nodejs", "html", "css"],
        "Backend & Tools": ["spring", "postgresql", "git", "github"],
        "Platforms": ["linux", "ubuntu", "vscode", "docker"]
    },
    "featured_projects": [
        {
            "name": "Davomat App",
            "description": "Smart attendance tracking system",
            "tech": "Android • Kotlin • Firebase"
        }
    ]
}

# -------------------------
# TYPING SVG GENERATOR
# -------------------------
def make_typing_svg(text, size=22, color="00FF2B", width=600, multiline=False):
    if multiline:
        lines = text if isinstance(text, list) else [text]
        lines_encoded = ";".join([line.replace(" ", "+") for line in lines])
        return f"https://readme-typing-svg.demolab.com?font=Fira+Code&size={size}&pause=1000&color={color}&center=true&vCenter=true&width={width}&lines={lines_encoded}"
    text_encoded = text.replace(" ", "+")
    return f"https://readme-typing-svg.demolab.com?font=Fira+Code&size={size}&pause=1000&color={color}&center=true&vCenter=true&width={width}&lines={text_encoded}"

# -------------------------
# README GENERATION
# -------------------------
def generate_readme(user):
    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    # Enhanced Skills Table with 4 columns
    skills_html = '<table align="center">\n<tr>\n'
    
    for category, icons in user['skills'].items():
        skills_html += f'<td align="center" width="200">\n<h3>{category}</h3>\n'
        for icon in icons:
            skills_html += f'<img src="https://skillicons.dev/icons?i={icon}" alt="{icon}" width="48" height="48" /> '
        skills_html += '\n</td>\n'
    
    skills_html += '</tr>\n</table>'

    # About section with combined typing animation
    about_typing = make_typing_svg(user['about_lines'], size=20, width=700, multiline=True)

    # Featured Projects section
    projects_section = ""
    if user.get('featured_projects'):
        projects_section = "\n---\n\n## 🎯 Featured Projects\n\n<div align=\"center\">\n\n"
        for project in user['featured_projects']:
            projects_section += f"""<div style="display: inline-block; margin: 10px; padding: 20px; border: 2px solid #00FF2B; border-radius: 10px;">
<h3>🔥 {project['name']}</h3>
<p>{project['description']}</p>
<p><code>{project['tech']}</code></p>
</div>\n\n"""
        projects_section += "</div>\n"

    readme = f"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text={user['name'].replace(' ', '%20')}&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35" width="100%" />

<br/>

<img src="{about_typing}" />

<br/><br/>

<p>
  <img src="https://komarev.com/ghpvc/?username={user['github_username']}&color=00FF2B&style=for-the-badge&label=PROFILE+VIEWS" />
  <img src="https://img.shields.io/github/followers/{user['github_username']}?color=58A6FF&label=FOLLOWERS&style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/github/stars/{user['github_username']}?color=00FF2B&style=for-the-badge&label=TOTAL+STARS&logo=github" />
</p>

</div>

---

## 🛠️ Tech Stack & Skills

<div align="center">

{skills_html}

</div>
{projects_section}
---

## 📊 GitHub Analytics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username={user['github_username']}&show_icons=true&theme=radical&hide_border=true&bg_color=0D1117&title_color=00FF2B&icon_color=58A6FF&text_color=FFFFFF&include_all_commits=true&count_private=true" width="49%" />
<img src="https://github-readme-streak-stats.herokuapp.com/?user={user['github_username']}&theme=radical&hide_border=true&background=0D1117&ring=00FF2B&fire=58A6FF&currStreakLabel=00FF2B&sideLabels=FFFFFF" width="49%" />

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={user['github_username']}&layout=compact&theme=radical&hide_border=true&bg_color=0D1117&title_color=00FF2B&text_color=FFFFFF&langs_count=8" width="49%" />
<img src="https://github-readme-activity-graph.vercel.app/graph?username={user['github_username']}&theme=react-dark&hide_border=true&bg_color=0D1117&color=00FF2B&line=58A6FF&point=FFFFFF&area=true" width="49%" />

</div>

---

## 🏆 GitHub Achievements

<div align="center">

<img src="https://github-profile-trophy.vercel.app/?username={user['github_username']}&theme=radical&no-frame=true&no-bg=true&row=1&column=7&margin-w=15&margin-h=15" width="100%" />

</div>

---

## 📈 Contribution Graph

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username={user['github_username']}&bg_color=0D1117&color=00FF2B&line=58A6FF&point=FFFFFF&area_color=00FF2B&area=true&hide_border=true&custom_title=Contribution%20Graph" width="95%" />

</div>

---

## 📫 Let's Connect!

<div align="center">

<a href="{user['telegram']}">
  <img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white&labelColor=1a1a1a" />
</a>
<a href="mailto:{user['email']}">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white&labelColor=1a1a1a" />
</a>
<a href="{user['linkedin']}">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=1a1a1a" />
</a>
<a href="{user['portfolio']}">
  <img src="https://img.shields.io/badge/Portfolio-FF7139?style=for-the-badge&logo=google-chrome&logoColor=white&labelColor=1a1a1a" />
</a>
<a href="https://github.com/{user['github_username']}">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=1a1a1a" />
</a>

</div>

---

<div align="center">

### 💭 Quote of the Day

<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical" />

<br/><br/>

### 🎯 "Code is like humor. When you have to explain it, it's bad." – Cory House

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%" />

**🔄 Auto-Updated:** {updated_time}  
**⭐ If you like my work, consider starring my repos!**

</div>
"""
    return readme


if __name__ == "__main__":
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(generate_readme(USER))
    print("✅ README.md generated successfully!")
    print("📁 File saved to: README.md")
    print("🚀 Push to GitHub to see the magic!")
