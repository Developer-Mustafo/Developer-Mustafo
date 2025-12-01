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
        "I am an Android Developer",
        "I write Telegram bots",
        "I build backend APIs",
        "I love clean code & architecture"
    ],
    "skills_icons": [
        {"category": "Languages", "icons": ["java","kotlin","javascript","python","html","css"]},
        {"category": "Frameworks", "icons": ["spring","springboot","android","compose","aiogram"]},
        {"category": "Tools", "icons": ["git","github","postgresql","ubuntu"]},
        {"category": "Platforms", "icons": ["linux","androidstudio","vscode"]}
    ]
}

# -------------------------
# TYPING SVG GENERATOR
# -------------------------
TYPING_BASE = "https://readme-typing-svg.demolab.com"

def make_typing_svg_url(lines, font="Fira+Code", size=18, pause=1000, color="00FF2B", width=500, height=50):
    lines_joined = "%0A".join([line.strip().replace(" ", "+") for line in lines])
    url = f"{TYPING_BASE}?font={font}&size={size}&pause={pause}&color={color}&width={width}&height={height}&lines={lines_joined}&center=true&multiline=true&repeat=false"
    return url

# -------------------------
# README GENERATION
# -------------------------
def generate_readme(user):
    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    skills_table = ""
    for i in range(0, len(user["skills_icons"]), 2):
        row_categories = user["skills_icons"][i:i+2]

        headers = "| " + " | ".join([
            f"<div align='center'><h3>{cat['category']}</h3></div>"
            for cat in row_categories
        ]) + " |\n"
        
        separators = "| " + " | ".join(["----"] * len(row_categories)) + " |\n"
        
        icons_row = "| " + " | ".join([
            "<div align='center'>" + "".join([
                f'<img src="https://skillicons.dev/icons?i={icon}" alt="{icon}" height="40" />' 
                for icon in cat["icons"]
            ]) + "</div>"
            for cat in row_categories
        ]) + " |\n"
        
        skills_table += headers + separators + icons_row + "\n"

    about_lines_typing = "\n".join([
        f'<img src="{make_typing_svg_url([line], size=24, width=600, color="00FF2B")}" />' 
        for line in user['about_lines']
    ])

    readme = f"""<div align="center">

<img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%" />

{about_lines_typing}

<img src="{make_typing_svg_url(['Full Stack Android Developer'], size=18, width=700, color='58A6FF')}" />

<p align="center">
  <img src="https://komarev.com/ghpvc/?username={user['github_username']}&color=00FF2B&style=flat-square&label=Profile+Views" />
  <img src="https://img.shields.io/github/followers/{user['github_username']}?color=58A6FF&label=Followers&style=flat-square" />
</p>

</div>

---

## 🛠️ Tech Stack

{skills_table}

---

## 📊 GitHub Stats

<div align="center">

<!-- Stats -->
<img src="https://github-readme-stats-git-masterorgs-github-readme-stats-team.vercel.app/api?username=Developer-Mustafo&show_icons=true&theme=dark&hide_border=true" height="165" />

<!-- Top langs -->
<img src="https://github-readme-stats-git-masterorgs-github-readme-stats-team.vercel.app/api/top-langs/?username=Developer-Mustafo&layout=compact&theme=dark&hide_border=true" height="165" />

<!-- Activity Graph -->
<img src="https://github-readme-activity-graph.vercel.app/graph?username=Developer-Mustafo&theme=react-dark&hide_border=true" width="100%" />

</div>

---

## 📫 Connect With Me

<div align="center">
<a href="{user['telegram']}"><img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram" /></a>
<a href="mailto:{user['email']}"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail" /></a>
<a href="{user['linkedin']}"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin" /></a>
<a href="{user['portfolio']}"><img src="https://img.shields.io/badge/Portfolio-FF7139?style=for-the-badge&logo=firefox" /></a>
</div>

---

<div align="center">
<b>Last Updated:</b> {updated_time}
</div>
"""
    return readme


if __name__ == "__main__":
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(generate_readme(USER))
    print("✅ README.md generated Successfully!")
