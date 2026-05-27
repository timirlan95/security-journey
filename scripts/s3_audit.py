
import boto3

def check_s3_security(s3):
    print("=" * 40)
    print("S3 SECURITY AUDIT")
    print("=" * 40 + "\n")

    buckets = s3.list_buckets()['Buckets']
    print(f"Found {len(buckets)} bucket(s)\n")

    for bucket in buckets:
        name = bucket['Name']
        print(f"Bucket: {name}")

        # Public access
        try:
            pab = s3.get_public_access_block(Bucket=name)
            config = pab['PublicAccessBlockConfiguration']
            block_all = all([
                config.get('BlockPublicAcls', False),
                config.get('IgnorePublicAcls', False),
                config.get('BlockPublicPolicy', False),
                config.get('RestrictPublicBuckets', False)
            ])
            if block_all:
                print("  ✅ Public access: BLOCKED")
            else:
                print("  ❌ Public access: EXPOSED — CRITICAL RISK")
        except Exception:
            print("  ⚠️  Could not check public access")

        # Encryption
        try:
            enc = s3.get_bucket_encryption(Bucket=name)
            algo = enc['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
            print(f"  ✅ Encryption: {algo}")
        except Exception:
            print("  ❌ Encryption: NOT CONFIGURED")

        # Versioning
        try:
            ver = s3.get_bucket_versioning(Bucket=name)
            status = ver.get('Status', 'Disabled')
            if status == 'Enabled':
                print("  ✅ Versioning: Enabled")
            else:
                print("  ⚠️  Versioning: Disabled")
        except Exception:
            print("  ⚠️  Could not check versioning")

        print()


def check_iam_security(iam):
    print("=" * 40)
    print("IAM SECURITY AUDIT")
    print("=" * 40 + "\n")

    users = iam.list_users()['Users']
    print(f"Found {len(users)} user(s)\n")

    issues_found = 0

    for user in users:
        name = user['UserName']
        print(f"User: {name}")

        # Check MFA
        mfa_devices = iam.list_mfa_devices(UserName=name)['MFADevices']
        if mfa_devices:
            print("  ✅ MFA: Enabled")
        else:
            print("  ❌ MFA: NOT ENABLED — HIGH RISK")
            issues_found += 1

        # Check access keys
        keys = iam.list_access_keys(UserName=name)['AccessKeyMetadata']
        if keys:
            for key in keys:
                status = key['Status']
                key_id = key['AccessKeyId']
                if status == 'Active':
                    print(f"  ⚠️  Access key active: {key_id[:8]}...")
                else:
                    print(f"  ✅ Access key inactive: {key_id[:8]}...")
        else:
            print("  ✅ No access keys")

        # Check last login
        try:
            last_login = user.get('PasswordLastUsed', None)
            if last_login:
                print(f"  ℹ️  Last login: {last_login.strftime('%Y-%m-%d')}")
            else:
                print("  ⚠️  Never logged in")
        except Exception:
            pass

        print()

    if issues_found == 0:
        print("✅ No critical IAM issues found\n")
    else:
        print(f"❌ Found {issues_found} critical issue(s)\n")


if __name__ == "__main__":
    s3 = boto3.client('s3')
    iam = boto3.client('iam')

    check_s3_security(s3)
    check_iam_security(iam)
