#!/bin/bash

echo "========================================"
echo "AWS SECURITY CHECK"
echo "========================================"
echo ""

echo "### Who am I ###"
aws sts get-caller-identity
echo ""

echo "### S3 Buckets ###"
aws s3 ls
echo ""

echo "### IAM Users ###"
aws iam list-users --query "Users[*].{User:UserName,Created:CreateDate}" --output table
echo ""

echo "### CloudTrail Status ###"
aws cloudtrail describe-trails --query "trailList[*].{Name:Name,MultiRegion:IsMultiRegionTrail,Logging:LogFileValidationEnabled}" --output table
echo ""

echo "========================================"
echo "### MFA Status ###"
for user in $(aws iam list-users --query "Users[*].UserName" --output text); do
    mfa=$(aws iam list-mfa-devices --user-name $user --query "MFADevices[*].SerialNumber" --output text)
    if [ -z "$mfa" ]; then
        echo "  ❌ $user — NO MFA"
    else
        echo "  ✅ $user — MFA enabled"
    fi
done
echo ""
echo "CHECK COMPLETE"
echo "========================================"
