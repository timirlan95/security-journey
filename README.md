# Security Journey 🔐
My path from zero to Cloud Security Engineer

---

## День 1 — Основы сетей и Linux
**Дата:** 23 мая 2026

### Что изучил:
- Как работает DNS, IP, порты, TCP, HTTPS
- CDN и reverse proxy — нашёл что TikTok работает через Akamai
- Структура файловой системы Linux
- Права доступа: chmod, chown, ls -la
- Пользователи и группы: /etc/passwd, /etc/shadow
- Логи: auth.log — восстановил хронологию событий
- Cron: планировщик задач, persistence техника хакеров

### Команды которые освоил:
nslookup, tracert, ping, pwd, ls, cat
chmod, chown, grep, tail, find, sudo
crontab, whoami, groups, passwd

### Практика:
- Нашёл реальный IP Google и YouTube через nslookup
- Определил что TikTok использует Akamai CDN
- Создал security_lab, настроил права файлов
- Прочитал /etc/shadow и /etc/passwd
- Проанализировал auth.log и нашёл свои неудачные попытки sudo
- Прочитал первый bash-скрипт — logrotate

### Ключевые концепции:
- Least Privilege — минимум прав для каждого
- Credential exposure — пароли не должны быть в файлах с правами 644
- Persistence — как хакеры остаются в системе через cron
- Log analysis — восстановление событий по логам
