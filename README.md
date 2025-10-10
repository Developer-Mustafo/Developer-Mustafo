# WakaTime profile summary — @mustaforahim2009

⚠️ Diqqat: Bu fayl brauzer yoki internet orqali sahifani to'g'ridan-to'g'ri yuklab olishga uringan holda avtomatik yaratilmadi.
Sizga keyingi bosqichlarni bajarish uchun zarur bo‘lgan fayllar `generate_readme.py` bilan birga berilmoqda.

## Nima bor
- `generate_readme.py` — WakaTime profilidan README.md yaratish uchun Python skripti.
- `WAKATIME_PROFILE.info` — profil URL haqida kichik metadata.
- `README.md` — hozirgi placeholder/fayl (bu faylni avtomatik to'ldirish uchun pastdagi ko'rsatmalarga qarang).

## Qanday ishlatish
1. Terminalda Python3 o'rnatilganiga ishonch hosil qiling.
2. Zarur kutubxonalarni o'rnating:
   ```bash
   pip3 install requests beautifulsoup4
   ```
3. Skriptni ishga tushiring:
   ```bash
   python3 generate_readme.py
   ```
   Skript `README.md` faylini yaratadi va `wakatime_readme.tar` arxivini hosil qiladi.
4. Arxivni chiqarish:
   ```bash
   tar -xvf wakatime_readme.tar
   ```
   Ichida `README.md`, `generate_readme.py`, va `WAKATIME_PROFILE.info` bo‘ladi.

## Qo'shimcha
Agar siz to‘liq, JS bilan render qilingan statistikani xohlasangiz (til bo‘yicha chartlar, soatlik graflar), `generate_readme.py` ni Playwright yoki WakaTime rasmiy API (token talab qiladi) bilan kengaytirish kerak.

Profile URL: https://wakatime.com/@mustaforahim2009

_— Siz uchun tayyorlangan arxiv (ichida skript va placeholder README)._
