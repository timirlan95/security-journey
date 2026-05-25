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

## Day 2 — SSH, AWS EC2 & Cloud Security
**Date:** May 25, 2026

### What I did:
- Generated SSH keys (ed25519) and understood public/private key pairs
- Launched first EC2 instance on AWS in Ohio data center
- Connected via SSH to a real cloud server
- Found real attacks in auth.log within hours of server launch
- Analyzed attacker from Rostelecom (Russia) — 26 attempts
- Decoded attacker wordlist: admin, pi, oracle, ftpuser, test1, test2, usuario
- Configured server hardening: ufw, fail2ban, auto-updates
- Set up CloudWatch Agent — centralized log monitoring
- Created metric filter and alarm — email alert on SSH attacks
- Confirmed SNS subscription for security notifications

### Mistakes & lessons:
- Enabled ufw WITHOUT allowing port 22 first → locked out of server
- Correct order: sudo ufw allow 22 → sudo ufw enable
- Recovery: created IAM role + used SSM Session Manager via browser
- IAM AccessDenied on CloudWatch → added CloudWatchAgentServerPolicy to role

### Key concepts:
- **Defense in depth** — Security Group + ufw + fail2ban (3 layers)
- **IAM roles** — permissions for AWS services, not humans
- **Centralized logging** — CloudWatch collects logs from all servers
- **Locked out recovery** — SSM Session Manager bypasses SSH
- **Real attacks happen fast** — server found by bots within hours

### Commands practiced:
```bash
ssh-keygen -t ed25519    # generate SSH keys
ssh -i key.pem user@ip   # connect to remote server
sudo ufw allow 22        # allow SSH before enabling firewall
sudo ufw enable          # enable firewall
sudo ufw deny from IP    # block specific attacker
sudo systemctl status X  # check service status
sudo fail2ban-client status sshd  # check banned IPs
wget URL                 # download file
sudo dpkg -i file.deb    # install local package
```
