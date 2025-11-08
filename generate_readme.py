import datetime

# --- SETTINGS ---
USERNAME = "YOUR_GITHUB_USERNAME"  # ❗ O'z GitHub username'ingizni yozing
GIF_URL = "https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif"  # Animatsion GIF
CURRENT_YEAR = datetime.datetime.now().year

# --- TYPING ANIMATION FUNCTION ---
def typing_svg(lines, color="FF6F00", font="JetBrains+Mono", width=435):
    text = ";".join(lines)
    return f"https://readme-typing-svg.demolab.com?font={font}&pause=1000&color={color}&width={width}&lines={text}"

# --- README GENERATION ---
def generate_readme():
    about_lines = [
        "👋 Hi there! I'm Mustafo",
        "💻 Android & Backend Developer",
        "🧠 Currently exploring AI + Kotlin + Java",
        "🚀 Building modern apps with Compose & Spring Boot"
    ]

    readme = f"""<div align="center">
  <img src="{GIF_URL}" width="300"/>

  <h1>Assalamu alaykum 👋, I'm Mustafo</h1>
  <p><b>Android & Backend Developer | Kotlin | Java | Spring Boot | AI Learner</b></p>
</div>

---

### 🧠 About Me
<p align="center">
  <img src="{typing_svg(about_lines)}"/>
</p>

---

### 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Kotlin-0095D5?logo=kotlin&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Android-3DDC84?logo=android&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Jetpack%20Compose-4285F4?logo=jetpackcompose&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Dagger%20Hilt-9C27B0?logo=dagger&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Room%20DB-1976D2?logo=sqlite&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Ktor-0095D5?logo=kotlin&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Retrofit-FF5722?logo=square&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/MapLibre-00BFFF?logo=openstreetmap&logoColor=white&style=for-the-badge"/>
  <img src="https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white&style=for-the-badge"/>
</p>

---

<h2 align="center">💻 Coding Time</h2>

<p align="center">
  <img src="{typing_svg([
    'Writing clean and modern Kotlin code...',
    'Building beautiful Compose UIs...',
    'Exploring AI and backend integration...',
    'Always learning and improving!'
  ])}"/>
</p>

---

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={USERNAME}&theme=tokyo-night&hide_border=true"/>
</p>

---

<h2 align="center">📊 GitHub Stats</h2>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&theme=radical&hide_border=true"/>
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={USERNAME}&theme=radical&hide_border=true"/>
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&theme=radical&hide_border=true"/>
</p>

---

<p align="center">✨ Generated with ❤️ by a Python script — {CURRENT_YEAR}</p>
"""
    return readme


if __name__ == "__main__":
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(generate_readme())
    print("✅ README.md generated successfully!")
