from datetime import datetime, timezone
from urllib.parse import quote_plus

# =========================
# USER CONFIG
# =========================
USER = {
    "name": "Mustafo Rahim",
    "github_username": "Developer-Mustafo",
    "email": "mustaforahimov30@gmail.com",
    "telegram": "https://t.me/rahim_mustafo_x",
    "linkedin": "https://www.linkedin.com/in/mustafo-rahim-4a0384324",
    "portfolio": "http://davomat-app.uz",
    "about_lines": [
        "🚀 Android Developer",
        "🤖 Telegram Bot Developer",
        "⚡ Backend API Builder",
        "💡 Clean Code Enthusiast"
    ],
    "skills": {
        "Languages": ["java", "kotlin", "javascript", "python", "html", "css"],
        "Frameworks": ["spring", "android", "nodejs"],
        "Tools": ["git", "github", "postgresql", "ubuntu", "vscode"],
        "Platforms": ["linux", "android"]
    }
}

# =========================
# HELPERS
# =========================
def make_typing_svg(text, size=22, color="00FF2B", width=600):
    encoded = quote_plus(text)
    return (
        "https://readme-typing-svg.demolab.com"
        f"?font=Fira+Code&size={size}&pause=1000"
        f"&color={color}&center=true&vCenter=true"
        f"&width={width}&lines={encoded}"
    )

def skill_icons(items):
    return f"https://skillicons.dev/icons?i={','.join(items)}"

# =========================
# README GENERATOR
# =========================
def generate_readme(user):
    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    about_section = "\n".join(
        f'<p align="center"><img src="{make_typing_svg(line, size=20)}"/></p>'
        for line in user["about_lines"]
    )

    readme = f"""
<div align="center">

<h1>👋 Hi, I'm {user['name']}</h1>

{about_section}

<img src="{make_typing_svg('Full Stack Android Developer', size=24, color='58A6FF', width=700)}"/>

<p>
<img src="https://komarev.com/ghpvc/?username={user['github_username']}&style=flat-square"/>
<img src="https://img.shields.io/github/followers/{user['github_username']}?style=flat-square"/>
</p>

</div>

---

## 🛠 Tech Stack

<div align="center">

| Languages & Frameworks | Tools & Platforms |
|----------------------|------------------|
| <img src="{skill_icons(user['skills']['Languages'] + user['skills']['Frameworks'])}" /> | <img src="{skill_icons(user['skills']['Tools'] + user['skills']['Platforms'])}" /> |

</div>

---

## 📊 GitHub Stats

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username={user['github_username']}&show_icons=true&theme=radical&hide_border=true"/>
<img width="49%" src="https://github-readme-streak-stats.herokuapp.com/?user={user['github_username']}&theme=radical&hide_border=true"/>

<img width="49%" src="https://github-readme-stats.vercel.app/api/top-langs/?username={user['github_username']}&layout=compact&theme=radical&hide_border=true"/>
<img width="49%" src="https://github-readme-activity-graph.vercel.app/graph?username={user['github_username']}&theme=react-dark&hide_border=true"/>

</div>

---

## 🏆 GitHub Trophies

<div align="center">

<img src="https://github-profile-trophy.vercel.app/?username={user['github_username']}&theme=radical&no-frame=true&row=1&column=7"/>

</div>

---

## 📫 Connect With Me

<div align="center">

<a href="{user['telegram']}">
<img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
</a>
<a href="mailto:{user['email']}">
<img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>
<a href="{user['linkedin']}">
<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>
<a href="{user['portfolio']}">
<img src="https://img.shields.io/badge/Portfolio-FF7139?style=for-the-badge&logo=google-chrome&logoColor=white"/>
</a>

</div>

---

<div align="center">

### 💻 "Code is like humor. When you have to explain it, it's bad."

**Last Updated:** {updated_time}

</div>
"""
    return readme.strip()

# =========================
# RUN
# =========================
if __name__ == "__main__":
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(generate_readme(USER))
    print("✅ README.md muvaffaqiyatli yaratildi!")
