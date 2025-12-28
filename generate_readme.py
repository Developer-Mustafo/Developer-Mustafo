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
        "🚀 I am an Android Developer",
        "🤖 I write Telegram bots",
        "⚡ I build backend APIs",
        "💡 I love clean code & architecture"
    ],
    "skills": {
        "Languages": ["java", "kotlin", "javascript", "python", "html", "css"],
        "Frameworks": ["spring", "androidstudio", "nodejs"],
        "Tools": ["git", "github", "postgresql", "ubuntu"],
        "Platforms": ["linux", "android", "vscode"]
    }
}

# -------------------------
# TYPING SVG GENERATOR
# -------------------------
def make_typing_svg(text, size=22, color="00FF2B", width=600):
    text_encoded = text.replace(" ", "+")
    return f"https://readme-typing-svg.demolab.com?font=Fira+Code&size={size}&pause=1000&color={color}&center=true&vCenter=true&width={width}&lines={text_encoded}"

# -------------------------
# README GENERATION
# -------------------------
def generate_readme(user):
    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    # Skills Table with proper 2-column layout
    skills_table = "| Languages & Frameworks | Tools & Platforms |\n"
    skills_table += "|:----------------------:|:-----------------:|\n"
    
    # Left column
    left_icons = []
    left_icons.extend([f'<img src="https://skillicons.dev/icons?i={icon}" alt="{icon}" width="40" height="40" />' 
                      for icon in user['skills']['Languages']])
    left_icons.extend([f'<img src="https://skillicons.dev/icons?i={icon}" alt="{icon}" width="40" height="40" />' 
                      for icon in user['skills']['Frameworks']])
    
    # Right column
    right_icons = []
    right_icons.extend([f'<img src="https://skillicons.dev/icons?i={icon}" alt="{icon}" width="40" height="40" />' 
                       for icon in user['skills']['Tools']])
    right_icons.extend([f'<img src="https://skillicons.dev/icons?i={icon}" alt="{icon}" width="40" height="40" />' 
                       for icon in user['skills']['Platforms']])
    
    skills_table += f"| {' '.join(left_icons)} | {' '.join(right_icons)} |\n"

    # About section with separate typing animations
    about_typing = '\n'.join([
        f'<p align="center"><img src="{make_typing_svg(line, size=20)}" /></p>'
        for line in user['about_lines']
    ])

    readme = f"""<div align="center">

<h1>👋 Hi, I'm {user['name']}</h1>

{about_typing}

<br/>

<img src="{make_typing_svg('Full Stack Android Developer', size=24, color='58A6FF', width=700)}" />

<br/><br/>

<p>
  <img src="https://komarev.com/ghpvc/?username={user['github_username']}&color=00FF2B&style=flat-square&label=Profile+Views" />
  <img src="https://img.shields.io/github/followers/{user['github_username']}?color=58A6FF&label=Followers&style=flat-square" />
  <img src="https://img.shields.io/github/stars/{user['github_username']}?color=00FF2B&style=flat-square&label=Stars" />
</p>

</div>

---

## 🛠️ Tech Stack

<div align="center">

{skills_table}

</div>

---

## 📊 GitHub Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username={user['github_username']}&show_icons=true&theme=radical&hide_border=true&bg_color=0D1117&title_color=00FF2B&icon_color=58A6FF&text_color=FFFFFF" width="49%" />
<img src="https://github-readme-streak-stats.herokuapp.com/?user={user['github_username']}&theme=radical&hide_border=true&background=0D1117&ring=00FF2B&fire=58A6FF&currStreakLabel=00FF2B" width="49%" />

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={user['github_username']}&layout=compact&theme=radical&hide_border=true&bg_color=0D1117&title_color=00FF2B&text_color=FFFFFF" width="49%" />
<img src="https://github-readme-activity-graph.vercel.app/graph?username={user['github_username']}&theme=react-dark&hide_border=true&bg_color=0D1117&color=00FF2B&line=58A6FF&point=FFFFFF" width="49%" />

</div>

---

## 🏆 GitHub Trophies

<div align="center">

<img src="https://github-profile-trophy.vercel.app/?username={user['github_username']}&theme=radical&no-frame=true&row=1&column=7&margin-w=15&margin-h=15" width="100%" />

</div>

---

## 📫 Connect With Me

<div align="center">

<a href="{user['telegram']}">
  <img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" />
</a>
<a href="mailto:{user['email']}">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>
<a href="{user['linkedin']}">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="{user['portfolio']}">
  <img src="https://img.shields.io/badge/Portfolio-FF7139?style=for-the-badge&logo=google-chrome&logoColor=white" />
</a>

</div>

---

<div align="center">

### 💻 "Code is like humor. When you have to explain it, it's bad." – Cory House

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%" />

**Last Updated:** {updated_time}

</div>
"""
    return readme


if __name__ == "__main__":
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(generate_readme(USER))
    print("✅ README.md generated Successfully!")
