import os
from datetime import datetime, timezone

# -------------------------
# DEVELOPER PROFILE
# -------------------------
DEVELOPER = {
    "name": "Mustafo Rahim",
    "title": "Android & Backend Developer",
    "location": "Urgench, Khorezm, Uzbekistan",
    "bio": "Passionate about Android and backend programming, working with Kotlin and Java. Goal-oriented, curious, and strives to create projects with real value. Aims to become a strong developer in the future.",
    "focus": "Building practical Android apps with modern architectures and scalable backend systems",
    "experience": "3+ years",
    "status": "Open to challenging projects and collaborations",
    "contact": {
        "email": "mustaforahimov30@gmail.com",
        "telegram": "https://t.me/rahim_mustafo_x",
        "linkedin": "https://www.linkedin.com/in/mustafo-rahim-4a0384324",
        "github": "https://github.com/Developer-Mustafo",
        "portfolio": "http://davomat-app.uz"
    }
}

# -------------------------
# TECHNICAL SKILLS WITH ICONS
# -------------------------
TECH_SKILLS = {
    "📱 Mobile Development": [
        {"name": "Kotlin", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kotlin/kotlin-original.svg", "level": "Advanced"},
        {"name": "Java", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg", "level": "Advanced"},
        {"name": "Android Studio", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/androidstudio/androidstudio-original.svg", "level": "Advanced"},
        {"name": "Jetpack Compose", "icon": "https://developer.android.com/static/images/jetpack/compose/logo-compose.svg", "level": "Intermediate"},
        {"name": "Material Design", "icon": "https://material.io/design/static/images/logo-mobile.svg", "level": "Intermediate"}
    ],
    "⚡ Backend Development": [
        {"name": "Spring Boot", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg", "level": "Intermediate"},
        {"name": "PostgreSQL", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg", "level": "Intermediate"},
        {"name": "REST API", "icon": "https://img.icons8.com/color/48/000000/api.png", "level": "Intermediate"}
    ],
    "🤖 Telegram Bot Development": [
        {"name": "Aiogram", "icon": "https://docs.aiogram.dev/en/dev-3.x/_static/logo.png", "level": "Intermediate"},
        {"name": "Telegram Bot API", "icon": "https://telegram.org/img/t_logo.svg", "level": "Advanced"},
        {"name": "python-telegram-bot", "icon": "https://python-telegram-bot.org/static/logo.png", "level": "Intermediate"}
    ],
    "🔧 Languages & Tools": [
        {"name": "Python", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", "level": "Intermediate"},
        {"name": "JavaScript", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", "level": "Intermediate"},
        {"name": "HTML5", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", "level": "Intermediate"},
        {"name": "CSS3", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg", "level": "Intermediate"},
        {"name": "Git", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg", "level": "Intermediate"},
        {"name": "Linux", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg", "level": "Intermediate"}
    ]
}

# -------------------------
# PROJECT EXPERIENCE
# -------------------------
PROJECTS = [
    {
        "name": "Davomat App",
        "description": "Smart attendance tracking system for educational institutions",
        "technologies": ["Spring Boot", "Aiogram", "PostgreSQL", "Kotlin", "Material Design"],
        "features": ["Real-time attendance tracking", "Telegram bot integration", "Admin dashboard", "Reports generation", "User management"],
        "status": "Completed",
        "year": "2023",
        "highlight": True
    },
    {
        "name": "Telegram Bots Suite",
        "description": "Various Telegram bots for automation, notifications, and business processes",
        "technologies": ["Aiogram", "Python", "PostgreSQL"],
        "features": ["Automated responses", "User management", "Database integration", "Admin controls", "Scheduling"],
        "status": "Ongoing",
        "year": "2022-Present",
        "highlight": True
    },
    {
        "name": "Android Applications",
        "description": "Multiple Android apps using both traditional and modern approaches",
        "technologies": ["Kotlin", "Java", "MVVM", "Room", "Material Design"],
        "features": ["Clean Architecture", "Local database", "Material Design UI", "Testing", "API integration"],
        "status": "Ongoing",
        "year": "2021-Present",
        "highlight": False
    }
]

# -------------------------
# ANDROID DEVELOPMENT APPROACHES
# -------------------------
ANDROID_APPROACHES = {
    "Traditional Approach": [
        "Java programming language",
        "XML layouts",
        "Activities & Fragments",
        "AsyncTask for background tasks",
        "SQLite with raw queries"
    ],
    "Modern Approach": [
        "Kotlin programming language",
        "Jetpack Compose for UI",
        "MVVM/MVI architecture",
        "Coroutines & Flow",
        "Room database with DAOs",
        "Retrofit for networking",
        "Dependency Injection (Hilt)"
    ]
}

# -------------------------
# GENERATE README
# -------------------------
def generate_readme():
    """Generate complete README with images and detailed information"""
    updated_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    # Header with animated banner
    header = f"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&section=header&text=Mustafo%20Rahim&fontSize=50&fontColor=fff&animation=fadeIn" width="100%" />

<h2>Android & Backend Developer</h2>
<h3>📍 {DEVELOPER['location']} | 🎯 {DEVELOPER['experience']} Experience</h3>

<p>{DEVELOPER['bio']}</p>

![Profile Views](https://komarev.com/ghpvc/?username=Developer-Mustafo&color=blue&style=flat-square)
![GitHub Followers](https://img.shields.io/github/followers/Developer-Mustafo?style=social)
![Android Developer](https://img.shields.io/badge/Android%20Developer-Kotlin%20%2F%20Java-green)
![Spring Boot](https://img.shields.io/badge/Backend-Spring%20Boot-orange)

</div>

---

## 🛠️ Technical Stack

<div align="center">
"""
    
    # Skills section with icons
    skills_section = ""
    for category, skills in TECH_SKILLS.items():
        skills_section += f"\n### {category}\n\n"
        skills_section += '<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; margin: 20px 0;">\n'
        
        for skill in skills:
            skills_section += f"""
<div align="center" style="margin: 10px;">
    <img src="{skill['icon']}" alt="{skill['name']}" width="50" height="50" />
    <br/>
    <strong>{skill['name']}</strong>
    <br/>
    <small>{skill['level']}</small>
</div>
"""
        skills_section += "</div>\n"
    
    # Projects section
    projects_section = """
## 🚀 Featured Projects

<div align="center">
"""
    
    for project in PROJECTS:
        if project.get('highlight', False):
            tech_badges = " ".join([f"![{tech}](https://img.shields.io/badge/-{tech}-gray?style=flat)" for tech in project['technologies'][:4]])
            
            projects_section += f"""
<div style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); padding: 25px; border-radius: 15px; margin: 25px 0; border: 1px solid #2d3436; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <h3>🔥 {project['name']}</h3>
    <p>{project['description']}</p>
    
    <div align="left" style="margin: 15px 0;">
        <strong>📅 Year:</strong> {project['year']}<br/>
        <strong>📊 Status:</strong> {project['status']}<br/>
        <strong>✨ Features:</strong><br/>
        {''.join([f"• {feature}<br/>" for feature in project['features'][:3]])}
    </div>
    
    <div style="margin: 20px 0;">
        {tech_badges}
    </div>
</div>
"""
    
    projects_section += "</div>\n"
    
    # Android Approaches Comparison
    android_section = """
## 📱 Android Development Approaches

<div align="center">

<table>
<tr>
<th width="50%">Traditional Android</th>
<th width="50%">Modern Android</th>
</tr>
<tr>
<td valign="top">
<ul>
"""
    
    for approach in ANDROID_APPROACHES["Traditional Approach"]:
        android_section += f"<li>{approach}</li>\n"
    
    android_section += """</ul>
</td>
<td valign="top">
<ul>
"""
    
    for approach in ANDROID_APPROACHES["Modern Approach"]:
        android_section += f"<li>{approach}</li>\n"
    
    android_section += """</ul>
</td>
</tr>
</table>

<p><em>Currently focused on mastering Modern Android Development approaches</em></p>

</div>
"""
    
    # GitHub Stats
    stats_section = f"""
---

## 📊 GitHub Analytics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Developer-Mustafo&show_icons=true&theme=dark&hide_border=true&bg_color=0D1117&title_color=00FF2B&icon_color=58A6FF&include_all_commits=true" width="49%" />
<img src="https://github-readme-streak-stats.herokuapp.com/?user=Developer-Mustafo&theme=dark&hide_border=true&background=0D1117&ring=00FF2B&fire=58A6FF" width="49%" />

<br/><br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Developer-Mustafo&layout=compact&theme=dark&hide_border=true&bg_color=0D1117&title_color=00FF2B&langs_count=8" width="45%" />
<img src="https://github-readme-activity-graph.vercel.app/graph?username=Developer-Mustafo&theme=react-dark&hide_border=true&bg_color=0D1117&color=00FF2B&line=58A6FF&point=FFFFFF&area=true" width="52%" />

</div>
"""
    
    # Contact Section
    contact_section = f"""
---

## 📫 Connect With Me

<div align="center">

<table>
<tr>
<td align="center" width="120">
<a href="mailto:{DEVELOPER['contact']['email']}">
<img src="https://img.icons8.com/color/96/000000/gmail.png" width="40" />
<br/>
Email
</a>
</td>
<td align="center" width="120">
<a href="{DEVELOPER['contact']['telegram']}">
<img src="https://img.icons8.com/color/96/000000/telegram-app.png" width="40" />
<br/>
Telegram
</a>
</td>
<td align="center" width="120">
<a href="{DEVELOPER['contact']['linkedin']}" target="_blank">
<img src="https://img.icons8.com/color/96/000000/linkedin.png" width="40" />
<br/>
LinkedIn
</a>
</td>
<td align="center" width="120">
<a href="{DEVELOPER['contact']['github']}" target="_blank">
<img src="https://img.icons8.com/color/96/000000/github.png" width="40" />
<br/>
GitHub
</a>
</td>
<td align="center" width="120">
<a href="{DEVELOPER['contact']['portfolio']}" target="_blank">
<img src="https://img.icons8.com/color/96/000000/domain.png" width="40" />
<br/>
Portfolio
</a>
</td>
</tr>
</table>

<p>
<strong>Professional Links:</strong><br/>
<a href="{DEVELOPER['contact']['linkedin']}" target="_blank">LinkedIn Profile</a> • 
<a href="{DEVELOPER['contact']['github']}" target="_blank">GitHub Profile</a> • 
<a href="{DEVELOPER['contact']['portfolio']}" target="_blank">Portfolio Website</a>
</p>

<p>
<em>Feel free to reach out for collaboration, project discussions, or technical questions!</em>
</p>

</div>
"""
    
    # Footer
    footer = f"""
---

<div align="center">

### 🎯 Current Focus Areas
- **Android Development:** Modern architectures with Kotlin & Jetpack Compose
- **Backend:** Spring Boot applications with PostgreSQL
- **Telegram Bots:** Building scalable bots with Aiogram
- **API Design:** RESTful API development and documentation

### 📚 Learning Goals 2024
1. Master Clean Architecture in Android
2. Deepen Spring Boot expertise
3. Build complex Telegram bot ecosystems
4. Contribute to open-source projects

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" width="100%" />

<small>**Last Updated:** {updated_time}</small><br/>
<small>© {datetime.now().year} • Built with passion from {DEVELOPER['location']}</small>

</div>
"""
    
    # Combine all sections
    full_readme = header + skills_section + projects_section + android_section + stats_section + contact_section + footer
    
    return full_readme

# -------------------------
# MAIN EXECUTION
# -------------------------
if __name__ == "__main__":
    # Generate README
    readme_content = generate_readme()
    
    # Save to file
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✅ README.md generated successfully!")
    print("📁 File saved to: README.md")
    print("\n📋 Profile Summary:")
    print(f"   Name: {DEVELOPER['name']}")
    print(f"   Location: {DEVELOPER['location']}")
    print(f"   Experience: {DEVELOPER['experience']}")
    print(f"   Email: {DEVELOPER['contact']['email']}")
    print(f"   LinkedIn: {DEVELOPER['contact']['linkedin']}")
    print(f"   Portfolio: {DEVELOPER['contact']['portfolio']}")
    
    print("\n🛠️ Updated Technical Stack:")
    print("   • Mobile: Kotlin, Java, Android Studio, Jetpack Compose")
    print("   • Backend: Spring Boot, PostgreSQL, REST API")
    print("   • Telegram Bots: Aiogram, Telegram Bot API")
    print("   • Languages: Python, JavaScript, HTML5, CSS3")
    print("   • Tools: Git, Linux")
    
    print("\n🚀 Removed from skills:")
    print("   • Node.js")
    print("   • Docker")
    
    print("\n✅ LinkedIn link added successfully!")
    print("🎯 README is now ready to showcase your Android & Backend expertise!")
