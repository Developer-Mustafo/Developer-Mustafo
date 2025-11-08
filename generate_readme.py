import os
from datetime import datetime, timezone

# -------------------------
# CONFIG / USER DATA
# -------------------------
USER = {
    "name": "Mustafo Rahim",
    "github_username": "Developer-Mustafo",
    "email": "rahim.mustafo.x@gmail.com",
    "telegram": "t.me/rahim_mustafo_x",
    "linkedin": "https://www.linkedin.com/in/mustafo-rahim-4a0384324",
    "portfolio": "http://davomat-app.uz",
    "top_projects": [
        {"name": "Urgench Smart City", "link": "https://urganchshahar.uz"},
        {"name": "E-Ijro Platform", "link": "http://90.156.199.148:7072/login"}
    ],
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
        {"category": "Languages", "icons": ["java","kotlin","js","html","css","python"]},
        {"category": "Frameworks", "icons": ["spring","springboot","tailwind","thymeleaf"]},
        {"category": "IDEs", "icons": ["androidstudio","vscode","intellij"]},
        {"category": "Tools", "icons": ["git","github","gitlab"]},
        {"category": "Operating Systems", "icons": ["windows","ubuntu"]}
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
    skills_table = "| " + " | ".join([f"[![Typing SVG]({make_typing_svg_url([cat['category']], size=25, width=200)})](https://git.io/typing-svg)" for cat in user["skills_icons"]]) + " |\n"
    skills_table += "| " + " | ".join(["----"] * len(user["skills_icons"])) + " |\n"
    
    icons_row = "| " + " | ".join([
        "<div align='center'>" + "".join([f'<a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i={i}" title="{i}"/></a>' for i in cat["icons"]]) + "</div>"
        for cat in user["skills_icons"]
    ]) + " |\n"

    # Top projects
    top_projects_md = ""
    for p in user["top_projects"]:
        top_projects_md += f"**📋 [{p['name']}]({p['link']})**\n\n"

    readme = f"""<div align="center">
<img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" alt="Snake animation" />
<a href="https://git.io/typing-svg">
  <img src="{make_typing_svg_url(['Men haqimda :'], size=28, width=1000)}" alt="Typing SVG"/>
</a>
<a href="https://git.io/typing-svg">
  <img src="{make_typing_svg_url(['{0}, Android va Backend Developer'.format(user['name'])], size=15)}" alt="Typing SVG"/>
</a>
</div>

---

## 🛠️ Skills & Technologies
{skills_table}
{icons_row}

---

## 🌐 Portfolio
<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="{make_typing_svg_url(['Portfolio:'], size=15, width=850)}" alt="Typing SVG" />
  </a>
</div>
**🔗 [{user['portfolio']}]({user['portfolio']})**

---

## 🚀 Top Projects
<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="{make_typing_svg_url(['Top Projects:'], size=15, width=850)}" alt="Typing SVG" />
  </a>
</div>
{top_projects_md}

---

## 📞 Contact Me
<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="{make_typing_svg_url(['Contact with me:'], size=15, width=950)}" alt="Typing SVG" />
  </a>
</div>

<div align="center">
  <a href="{user['telegram']}">
    <img src="https://img.shields.io/badge/Telegram-1DA1F2?style=for-the-badge&logo=telegram&logoColor=white" />
  </a>&nbsp;
  <a href="mailto:{user['email']}">
    <img src="https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>&nbsp;
  <a href="{user['linkedin']}">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>&nbsp;
</div>

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username={user['github_username']}&color=00FF2B&style=flat-square&label=Profile+Views" alt="Profile Views" />
</div>

**📅 Last Updated**: {updated_time}
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
