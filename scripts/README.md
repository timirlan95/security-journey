# Security Audit Scripts

## s3_audit.py

Automated security audit for AWS S3 buckets and IAM users.

Checks:
- S3 public access settings
- S3 encryption status
- S3 versioning status
- IAM users MFA status
- IAM access keys status
- IAM last login

### How to run
python3 s3_audit.py

### Output example
<img width="505" height="389" alt="s3_audit output" src="https://github.com/user-attachments/assets/14627922-0d86-466d-8a82-ca96feb1d123" />

---

## iam_key_audit.py

Script checks all IAM users for access keys older than 90 days.

Checks:
- Lists all IAM users
- Checks each access key age
- Skips inactive keys
- Flags keys older than 90 days as critical

### How to run
python3 iam_key_audit.py

### Output example
<img width="719" height="413" alt="iam_key_audit output" src="https://github.com/user-attachments/assets/952a081d-adf1-49f3-849c-a9a0e010f0ad" />

---

## cloudtrail_audit.py

Analyzes AWS CloudTrail events for the last 24 hours and flags suspicious activity.

Checks:
- DeleteBucket
- DeleteTrail
- StopLogging
- DeleteUser
- AttachUserPolicy

### How to run
python3 cloudtrail_audit.py

### Output example
<img width="949" height="910" alt="Screenshot 2026-05-28 235006" src="https://github.com/user-attachments/assets/347e36b6-9132-40d9-9e9b-9d63e680c85d" />
