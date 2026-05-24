# Security Journey 🔐
My path from zero to Cloud Security Engineer

---

## Day 1 — Networking Fundamentals & Linux Basics
**Date:** May 23, 2026

### What I learned:
- How DNS, IP, ports, TCP, and HTTPS work
- CDN and reverse proxy — discovered TikTok runs through Akamai
- Linux file system structure
- File permissions: chmod, chown, ls -la
- Users and groups: /etc/passwd, /etc/shadow
- Log analysis: auth.log — reconstructed a full timeline of events
- Cron jobs: task scheduling and how hackers use it for persistence

### Commands practiced:
```bash
nslookup    # DNS lookup
tracert     # trace network route
ping        # test connectivity
pwd         # print working directory
ls -la      # list files with permissions
cat         # read file contents
chmod       # change file permissions
chown       # change file owner
grep        # search text in files
tail        # read end of file
find        # search files by criteria
sudo        # execute as root
whoami      # current user
groups      # user group membership
passwd      # change password
crontab     # manage scheduled tasks
```

### Hands-on practice:
- Found real IPs of Google and YouTube via nslookup
- Identified TikTok uses Akamai CDN through reverse lookup
- Built security_lab directory and configured file permissions
- Read /etc/shadow and /etc/passwd, understood every field
- Analyzed auth.log and found my own failed sudo attempts
- Read my first bash script — logrotate

### Key concepts:
- **Least Privilege** — every user/process gets minimum required access
- **Credential exposure** — secrets must never sit in files with 644 permissions
- **Persistence** — how attackers survive reboots using cron jobs
- **Log analysis** — reconstructing events from system logs
