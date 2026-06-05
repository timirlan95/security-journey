# Building My Own VPN Server (Before It Was Worth Attacking)

**Date:** June 5, 2026

Before the [hardening writeup](./hardening.md), here's how the server got there in the
first place. I wanted a VPN I actually control — a foreign exit node for my own privacy,
and a way for family back in Russia to reach the open internet. Renting a "just trust us"
VPN wasn't the point. Building it was.

This is the build log, including the parts that cost me hours and aren't in any tutorial.

## Why Hetzner, and why not AWS

I already had an AWS EC2 box as a learning sandbox, but it's the wrong tool for this:
cloud-provider IP ranges are often already flagged, and egress is metered — a VPN there
gets expensive and easy to fingerprint. I went with a Hetzner Cloud VPS in **Helsinki**
instead: cheap (~€5/mo), generous traffic, and a clean European exit outside Russia.

<img width="1096" height="676" alt="Screenshot 2026-06-04 233539" src="https://github.com/user-attachments/assets/d585f5a2-8117-4b5e-bce9-06d7244ba3c1" />

## Lock the basics before anything else

First thing on a fresh box, before installing a single service: close the doors.
- `ufw` — allow only SSH (22) and the VPN port (443), deny everything else
- `fail2ban` — auto-ban IPs that repeatedly fail SSH login

<img width="1206" height="1389" alt="01-ufw-udp-and-cert" src="https://github.com/user-attachments/assets/27a46ebb-aa3c-4ec8-9940-cc54c2ce8992" />

The box started getting brute-forced almost immediately. "Basic hygiene first" isn't
optional — and the hardening writeup is what that turned into once I actually looked
at the logs.

## The panel, kept off the internet

I manage the VPN with **3X-UI**. The decision that matters: I did **not** expose its
web panel to the internet. It listens only on `127.0.0.1`, and I reach it through an
**SSH tunnel** (local port-forward) from my laptop or phone. No public admin page means
one less thing for the bots to find.


## The protocol: VLESS + REALITY

For a server that has to work from inside Russia, plain WireGuard is a dead end — it's
fingerprinted and blocked. I used **VLESS + REALITY (via Xray)**, which makes the traffic
look like an ordinary HTTPS connection to a real, well-known foreign website. The catch:
the "target" site has to be something popular that is *not* blocked or throttled in
Russia. Pick the wrong target and your camouflage works against you.


## The gotchas that actually cost me time

None of these are in the quickstart guides. Each one ate an hour.

**1. fail2ban banned me.** During setup I fat-fingered the SSH password enough times
that fail2ban banned my own IP. Locked out of my own server by my own defense.
Lesson: whitelist your own IP, or you become your own attacker.

**2. "Connection refused" over IPv6.** My SSH client kept reaching for the server's IPv6
address and giving up. Forcing the IPv4 address fixed it instantly. When a connection
"refuses" for no obvious reason, check which address family it's using.

**3. Empty Bind Address = panel won't load.** In the SSH port-forward, leaving the bind
address blank meant the panel never came up. Setting it explicitly to `127.0.0.1` fixed it.

**4. The exported config had `127.0.0.1` baked in.** Because I opened the panel through a
localhost tunnel, every share link 3X-UI generated used `127.0.0.1` as the server address.
Hand that to someone and it points at *their* machine, not the server. I had to swap in
the real public IP every time. Easy to miss, baffling when you hit it.

## Result

A working, censorship-resistant VPN I actually own: VLESS + REALITY on a hardened Helsinki
VPS, the admin panel hidden behind an SSH tunnel, connecting cleanly from the US and from
inside Russia.

Once I looked at how hard the internet was already knocking, this turned into a full
security audit → [hardening writeup](./hardening.md).
