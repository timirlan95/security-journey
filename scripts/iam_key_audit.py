import boto3
from datetime import datetime, timezone

def check_key_age(iam):
    print("=" * 40)
    print("IAM KEY ROTATION AUDIT")
    print("=" * 40 + "\n")
    
    users = iam.list_users()['Users']
    
    for user in users:
        name = user['UserName']
        print(f"User: {name}")
        
        keys = iam.list_access_keys(UserName=name)['AccessKeyMetadata']
        
        for key in keys:
            key_id = key['AccessKeyId']
            status = key['Status']
            created = key['CreateDate']
            
            now = datetime.now(timezone.utc)
            if status == 'Inactive':
                print(f"  ⚠️  Key {key_id[:8]}... is Inactive — skipping")
                continue
            age_days = (now - created).days
            
            if age_days > 90:
                print(f"  ❌ Key {key_id[:8]}... is {age_days} days old — ROTATE NOW")
            else:
                print(f"  ✅ Key {key_id[:8]}... is {age_days} days old — OK")

if __name__ == "__main__":
    iam = boto3.client('iam')
    check_key_age(iam)
