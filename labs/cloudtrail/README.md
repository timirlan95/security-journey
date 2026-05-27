# CloudTrail — AWS Audit Logging
**Date:** May 27, 2026

Before today I had no idea AWS records literally everything you do.
Turns out every API call, every config change, every login —
it all gets logged automatically once you set up a trail.

## What I set up

Created a trail called management-events.
Logs go to an S3 bucket that AWS created automatically.
Added KMS encryption for the log files and enabled log file validation.

Log file validation was interesting — AWS digitally signs every log file.
If someone tries to delete or modify logs to cover their tracks,
the signature breaks and you know something was tampered with.

<img width="1188" height="901" alt="Screenshot 2026-05-27 003424" src="https://github.com/user-attachments/assets/a45fb295-9e4c-4983-b0f0-babf4bbe2506" />

## Checked the event history

Within minutes of creating the trail, event history already had entries.
Every action I took today was recorded — creating the trail itself,
setting up KMS keys, IAM changes.

<img width="1183" height="812" alt="Screenshot 2026-05-27 002923" src="https://github.com/user-attachments/assets/0a115c91-4417-468a-9253-d2e026d67b62" />


## Opened one event — CreateAlias

Clicked on CreateAlias and saw the full record:

- Who did it: root
- When: May 27, 2026 00:26:19
- From where: 136.52.76.101 (my IP)
- MFA used: true

That last one matters. CloudTrail records whether MFA was used.
For compliance audits this is gold — you can prove every action
was properly authenticated.

<img width="1207" height="947" alt="Screenshot 2026-05-27 003051" src="https://github.com/user-attachments/assets/4640f334-13a7-4302-8733-5493a259cc96" />


## Why this matters

If someone steals credentials and starts doing things in your AWS account —
CloudTrail tells you exactly what they did, when, and from which IP.

Without CloudTrail you're blind. With it you have a full audit trail.
In regulated industries this isn't optional — it's required by law.
