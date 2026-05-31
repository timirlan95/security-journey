## AWS CLI — Working with AWS from Terminal

AWS CLI lets you control AWS services directly from the terminal.
No browser needed.

### Commands learned today

**Check who you are:**
aws sts get-caller-identity

**List S3 buckets:**
aws s3 ls

**Read file from S3:**
aws s3 cp s3://bucket-name/file.txt -

**List IAM users:**
aws iam list-users

**Check CloudTrail trails:**
aws cloudtrail describe-trails

**List Security Groups (table format):**
aws ec2 describe-security-groups --query "SecurityGroups[*].{Name:GroupName,ID:GroupId}" --output table

### Key insight

AWS CLI and boto3 solve different problems.
CLI is for quick one-off checks.
boto3 is for automation — loops, conditions, reports.

### Screenshots
<img width="784" height="842" alt="Screenshot 2026-05-30 223939" src="https://github.com/user-attachments/assets/a3954f26-792d-4c5c-8684-0df34086224b" />
<img width="881" height="169" alt="Screenshot 2026-05-30 224131" src="https://github.com/user-attachments/assets/fb4a3a1f-e846-4349-b43c-0d5c69aae449" />
