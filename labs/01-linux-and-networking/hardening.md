# Hardening the VPN Server Under Active Attack

**Date:** June 5, 2026

This is the follow-up to the [build log](./vpn-build.md). Once the server was up and
running, I ran a real security audit on it — and found it was already under constant
brute-force attack. So this became hardening on a live server, not a lab exercise.

## The problem: live brute-force

Checked the auth logs and the server was being hammered around the clock — bots trying
to log in as root and common usernames (trader, solana, admin...) from dozens of
different IPs. Same thing I saw on my EC2 back on Day 2, but this time on a server I
actually depend on.

<img width="1027" height="227" alt="Screenshot 2026-06-04 224351" src="https://github.com/user-attachments/assets/d064be05-9783-4b09-a140-2c21585a79fd" />

773 failed login attempts total. The internet is hostile by default.

## What was already protecting it

fail2ban was running and doing its job — auto-banning IPs after repeated failures.
125 IPs banned over time, 3 active bans at the moment I checked.

<img width="456" height="139" alt="Screenshot 2026-06-04 224418" src="https://github.com/user-attachments/assets/b8d94efb-e8f2-4647-afb1-89aa83251082" />

But fail2ban only reacts after attempts happen. As long as password login is open,
bots keep trying forever. Time to close the door completely.

## The hidden config that almost fooled me

The main sshd_config looked like password auth was just default. But there was a second
config file — `/etc/ssh/sshd_config.d/50-cloud-init.conf` — overriding it with
`PasswordAuthentication yes`. Hetzner's cloud-init drops it there. If I'd only edited
the main file, nothing would have changed and I wouldn't have understood why.

Lesson: always check `sshd_config.d/`, not just `sshd_config`.

<img width="464" height="29" alt="Screenshot 2026-06-04 224504" src="https://github.com/user-attachments/assets/26632bab-5209-451c-b35f-29e7c0bb06c4" />

## What I changed

1. Disabled password authentication entirely — key-only login now
2. Restricted root login to key-only (`PermitRootLogin prohibit-password`)

<img width="446" height="43" alt="Screenshot 2026-06-04 224525" src="https://github.com/user-attachments/assets/bb2d814e-8dcd-48ef-8c00-b97331238f5e" />

## Applying SSH changes without locking myself out

I learned this the hard way — both the ufw lockout on Day 2, and fail2ban banning my
own IP during the build. This time I did it carefully:
- Backed up the config first (`cp sshd_config sshd_config.backup`)
- Validated syntax before restarting (`sshd -t` — silent means OK)
- Restarted SSH but kept my current session open
- Tested a fresh login from a second window before trusting it

<img width="355" height="29" alt="Screenshot 2026-06-04 224557" src="https://github.com/user-attachments/assets/e1351d14-2ec8-4faf-a315-3c6c707f1d1f" />

## Key-based access from two devices

Set up key login for both my laptop and my iPhone — a separate key per device.
The laptop uses an ed25519 key. The iPhone uses a Secure Enclave key unlocked by
Face ID, so the private key physically never leaves the phone's secure chip.

<img width="1127" height="56" alt="Screenshot 2026-06-04 224650" src="https://github.com/user-attachments/assets/efa025af-cc79-45a4-8920-3cbdba1d26d5" />

Principle: never copy one private key between devices. One key per device means if I
lose one, I revoke just that key and everything else stays safe.

## Result

Password brute-force is now impossible — login is key-only. The bots can keep knocking;
the door no longer has a password lock to pick.
