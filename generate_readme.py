import os
from datetime import datetime, timezone

# -------------------------
# CONFIG / USER DATA
# -------------------------
USER = {
    "name": "Mustafo Rahim",
    "github_username": "Developer-Mustafo",
    "email": "mustaforahimov30@gmail.com",
    "telegram": "t.me/rahim_mustafo_x",
    "linkedin": "https://www.linkedin.com/in/mustafo-rahim-4a0384324",
    "portfolio": "http://davomat-app.uz",
    "about_lines": [
        "Android Developer — Kotlin & Jetpack Compose expert",
        "Backend Developer — Spring Boot & Ktor",
        "Telegram Bots — Aiogram, automation & AI integrations",
        "Passionate about clean architecture, tests & performance"
    ],
    "tech_stack": [
        "Kotlin — Primary Android language, concise and safe",
        "Jetpack Compose — Declarative UI for faster delivery",
        "Spring Boot & Ktor — Backend APIs",
        "Room & PostgreSQL — Reliable persistence",
        "Python (Aiogram) — Telegram bots & automation"
    ],
    "skills_icons": [
        {"category": "Languages", "icons": ["java","kotlin","javascript","python","html","css"]},
        {"category": "Frameworks", "icons": ["spring","springboot","android","compose","aiogram"]},
        {"category": "Tools", "icons": ["git","github","postgresql","ubuntu"]},
        {"category": "Platforms", "icons": ["linux","androidstudio","intellij","vscode"]}
    ]
}

TYPING_BASE = "https://readme-typing-svg.demolab.com"

def make_typing_svg_url(lines, font="Fira+Code", size=15, pause=1000, color="00FF2B", width=950, height=75):
    lines_joined = ";".join([l.replace(";", ",") for l in lines])
    params = f"font={font}&size={size}&pause={pause}&color={color}&width={width}&height={height}&lines={lines_joined}&center=true&vCenter=true&multiline=true&repeat=false&random=false"
    return f"{TYPING_BASE}?{params}"

# -------------------------
# README GENERATION
# -------------------------
def generate_readme(user):
    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    # Skills icons table
    skills_table = ""
    for i, category in enumerate(user["skills_icons"]):
        if i % 2 == 0:
            skills_table += "| " + " | ".join([
                f"<div align='center'><h3>{cat['category']}</h3></div>"
                for cat in user["skills_icons"][i:i+2]
            ]) + " |\n"
            skills_table += "| " + " | ".join(["----"] * 2) + " |\n"
            skills_table += "| " + " | ".join([
                "<div align='center'>" + "".join([f'<img src="https://skillicons.dev/icons?i={icon}" alt="{icon}" title="{icon}" height="40" />' for icon in cat["icons"]]) + "</div>"
                for cat in user["skills_icons"][i:i+2]
            ]) + " |\n\n"

    # About me section
    about_me_md = "\n".join([f"• {line}" for line in user["about_lines"]])

    readme = f"""<div align="center">

<!-- Snake Animation -->
<img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" alt="Snake animation" width="100%" />

<!-- Typing Intro -->
<a href="https://git.io/typing-svg">
  <img src="{make_typing_svg_url(['Salom, Men Mustafo Rahimman 👋'], size=28, width=600, color='00FF2B')}" alt="Typing SVG"/>
</a>

<!-- Subtitle -->
<a href="https://git.io/typing-svg">
  <img src="{make_typing_svg_url(['Full Stack Android Developer'], size=18, width=700, color='58A6FF')}" alt="Typing SVG"/>
</a>

<!-- Stats -->
<p align="center">
  <img src="https://komarev.com/ghpvc/?username={user['github_username']}&color=00FF2B&style=flat-square&label=Profile+Views" alt="Profile Views" />
  <img src="https://img.shields.io/github/followers/{user['github_username']}?color=58A6FF&label=Followers&style=flat-square" alt="GitHub Followers" />
</p>

</div>

---

## 👨‍💻 About Me

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="{make_typing_svg_url(['About Me:'], size=20, width=300, color='00FF2B')}" alt="Typing SVG" />
  </a>
</div>

{about_me_md}

---

## 🛠️ Tech Stack

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="{make_typing_svg_url(['Technologies & Tools:'], size=20, width=400, color='00FF2B')}" alt="Typing SVG" />
  </a>
</div>

{skills_table}

---

## 📊 GitHub Stats

<div align="center">

<!-- GitHub Stats -->
<img src="https://github-readme-stats.vercel.app/api?username={user['github_username']}&show_icons=true&theme=dark&hide_border=true&bg_color=0D1117&title_color=00FF2B&icon_color=00FF2B" alt="GitHub Stats" height="160" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={user['github_username']}&layout=compact&theme=dark&hide_border=true&bg_color=0D1117&title_color=00FF2B" alt="Top Languages" height="160" />

<!-- Streak Stats -->
<img src="https://github-readme-streak-stats.herokuapp.com/?user={user['github_username']}&theme=dark&hide_border=true&background=0D1117&stroke=00FF2B&ring=00FF2B&fire=00FF2B&currStreakLabel=00FF2B" alt="GitHub Streak" />

</div>

---

## 📫 Connect With Me

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="{make_typing_svg_url(['Get In Touch:'], size=20, width=300, color='00FF2B')}" alt="Typing SVG" />
  </a>
</div>

<div align="center">

<!-- Contact Badges -->
<a href="{user['telegram']}">
  <img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram" />
</a>
<a href="mailto:{user['email']}">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
</a>
<a href="{user['linkedin']}">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>
<a href="https://github.com/{user['github_username']}">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
</a>
<a href="{user['portfolio']}">
  <img src="https://img.shields.io/badge/Portfolio-FF7139?style=for-the-badge&logo=firefox&logoColor=white" alt="Portfolio" />
</a>

</div>

---

<div align="center">

### 🎯 "Code is like humor. When you have to explain it, it's bad." - Cory House

**Last Updated:** {updated_time}

</div>

"""
    return readme

# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    readme_content = generate_readme(USER)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("✅ README.md generated successfully!")
