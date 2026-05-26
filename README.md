# Security Journey 🔐
My path from zero to Cloud Security Engineer

Started from absolute zero — no IT background.
Currently working in economics and risk analytics,
making a career transition into cloud security.

---

## Day 1 — Networking & Linux Basics
**Date:** May 23, 2026 | **Time:** ~3 hours

First time touching Linux seriously. More hands-on than I expected.

### What clicked today:
- DNS is basically a phone book — without it you can't reach anything
- Found out TikTok runs through Akamai CDN, not their own servers
- Linux file permissions finally make sense — rwxrwxrwx = 777 = dangerous
- /etc/shadow stores password hashes, not actual passwords
- John the Ripper cracked "password123" in under a second using rockyou.txt

### What confused me at first:
- Difference between cat and ls — one reads files, other lists directories
- Why sudo is needed for some commands but not others
- The difference between 400 and 600 file permissions

### Hands-on:
- Ran nslookup on Google, YouTube, TikTok — compared IPs
- Traced route to Google — 7 hops from my machine
- Built security_lab directory, set proper file permissions
- Read /etc/passwd and /etc/shadow — understood every field
- Analyzed auth.log and found my own failed sudo attempts
- Cracked a password hash using John the Ripper + rockyou.txt wordlist

### Key insight:
Hashing is NOT encryption. You can't reverse a hash —
you can only guess and compare. That's why weak passwords
are dangerous even when "hashed".

---

## Day 2 — SSH, AWS EC2 & Real Attacks
**Date:** May 25, 2026 | **Time:** ~4 hours

First time in a real cloud environment. Things broke. Learned a lot.

### What happened:
Launched my first EC2 instance on AWS.
Within a few hours — found real attacks in the logs.
A bot from Rostelecom (Russia) tried 26 different usernames:
admin, pi, oracle, ftpuser, test1, test2, usuario...
Just a script running 24/7 scanning the entire internet.

### The mistake that locked me out:
Enabled ufw firewall WITHOUT allowing SSH port 22 first.
Lost access to the server completely.

Spent time figuring out recovery:
created IAM role → attached SSM policy → rebooted →
connected via Session Manager through browser.

The correct order I'll never forget:
sudo ufw allow 22   ← ALWAYS first
sudo ufw enable     ← only then

### What I built:
- EC2 server in AWS Ohio region
- SSH key-based authentication (ed25519)
- ufw firewall with attacker IP blocked
- fail2ban — auto-blocks brute force attempts
- Automatic security updates
- CloudWatch Agent — logs shipped to AWS
- Email alert when attack threshold exceeded

### What clicked:
IAM roles are not about humans — they're permissions
for AWS services to talk to each other.
My server needed a role to send logs to CloudWatch.
Without it: AccessDenied.

### Takeaway:
Real attacks start within hours of launching a server.
Defense in depth matters — Security Group + ufw + fail2ban
are three separate layers, each catches what the other misses.
