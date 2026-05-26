# Windows Security Audit
**Date:** May 26, 2026

After seeing real attacks on my AWS server I got curious —
what's actually happening on my own machine?
Decided to run a quick audit.

## Network connections

Ran netstat to see who's connecting where.

<img width="903" height="597" alt="1" src="https://github.com/user-attachments/assets/565a0c1c-761b-46b3-9abc-ff954f5ded9c" />

Lots of connections on port 443 — that's HTTPS, all encrypted.
One process had the most connections. Turned out to be my browser.

## Checking processes

Looked up every Process ID from netstat output.

<img width="1891" height="1705" alt="2026-05-25_22-27-10" src="https://github.com/user-attachments/assets/14d88797-2faf-466c-9c72-e918cbe634ec" />

<img width="1915" height="1699" alt="2026-05-25_22-28-25" src="https://github.com/user-attachments/assets/3ee57747-035e-4595-876a-b842d6b4901f" />

Everything was legit — browser, Apple services, Dell diagnostics,
standard Windows stuff. One process turned out to be Claude.
That made me laugh.

## Startup programs

<img width="1883" height="371" alt="2026-05-25_22-30-09" src="https://github.com/user-attachments/assets/d458b98f-8079-4355-954a-6e83879d23d0" />

Found Yandex Browser in startup. Not malicious but it's a Russian
browser — not great for privacy. Going to remove it.

## Verdict: Clean ✅
