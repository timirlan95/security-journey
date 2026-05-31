# S3 Security Lab
**Date:** May 26, 2026

Wanted to understand how S3 storage security works
and why so many data leaks happen through misconfigured buckets.

## Created a bucket

Set up tim-security-lab-2026 with default security settings.
The most important one — Block Public Access is ON by default now.
AWS learned from years of data leaks and made this the default.


<img width="2469" height="1977" alt="2026-05-25_22-39-54" src="https://github.com/user-attachments/assets/7cd66109-9239-4109-8b40-16b7d265447a" />

## Added a bucket policy

Wrote my first JSON bucket policy — forces HTTPS only.
Any connection without encryption gets denied automatically.

<img width="2493" height="1975" alt="2026-05-25_22-42-22" src="https://github.com/user-attachments/assets/32615764-c08c-46fc-b557-a7eb8b85c65b" />

The policy logic:
- Effect: Deny — this is a block, not an allow
- Principal: * — applies to everyone
- Condition: SecureTransport false — only triggers on unencrypted connections

## Uploaded a test file and tried to access it publicly

Uploaded a simple text file, then tried to open it directly
in the browser using the public Object URL.

<img width="821" height="650" alt="Untitled2" src="https://github.com/user-attachments/assets/f32e1cc2-d3cb-4121-bcf4-7357829547b5" />

<img width="821" height="652" alt="Untitled3" src="https://github.com/user-attachments/assets/f531a1d8-d1a7-4107-a3e4-9f14e4ecc7be" />

Got this:

<img width="1787" height="611" alt="2026-05-25_22-48-11" src="https://github.com/user-attachments/assets/ea20b747-2f28-4fcb-b90a-861f09fb33c1" />

Access Denied. The file exists but nobody can reach it from the internet.
This is exactly how it should work.

## Why this matters

Capital One 2019 — 100 million customer records leaked.
Root cause: S3 bucket with public access enabled.
Someone unchecked one checkbox.

The fix is simple. The damage was $80 million in fines.
