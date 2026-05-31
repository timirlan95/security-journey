## Bash Scripts — AWS Security Automation

Bash scripts let you run multiple commands automatically.
Instead of typing 10 commands manually — one file does everything.

### security_check.sh

Runs a full AWS security check in one command.

Checks:
- Who is logged in (aws sts get-caller-identity)
- S3 buckets
- IAM users
- CloudTrail status
- MFA status for every user

### Key concepts learned

**shebang** — #!/bin/bash tells Linux to run this file with Bash

**chmod +x** — gives the file permission to execute.
Without this Linux won't run it.

**for loop** — goes through every IAM user and checks MFA one by one

**$()** — runs a command and uses the result inside another command

**[ -z "$variable" ]** — checks if a variable is empty

### How to run
chmod +x security_check.sh
./security_check.sh

### Screenshot
<img width="557" height="577" alt="Screenshot 2026-05-30 225007" src="https://github.com/user-attachments/assets/142adb4b-d1bb-4ff1-bfee-c41c14108c32" />
