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

```bash
python3 s3_audit.py
```

### Output example

<img width="505" height="389" alt="Screenshot 2026-05-26 235633" src="https://github.com/user-attachments/assets/14627922-0d86-466d-8a82-ca96feb1d123" />


### Why I built this

Checking S3 and IAM settings manually in AWS console
takes forever when you have multiple resources.
This script does it in seconds and flags anything suspicious.

Real use case: run this after any infrastructure change
to make sure nothing was accidentally misconfigured.
