import boto3

def check_guardduty(gd):
    print("=" * 40)
    print("GUARDDUTY FINDINGS AUDIT")
    print("=" * 40 + "\n")

    # Get detector ID
    detectors = gd.list_detectors()['DetectorIds']
    
    if not detectors:
        print("GuardDuty is not enabled!")
        return
    
    detector_id = detectors[0]
    print(f"Detector ID: {detector_id}\n")

    # Get findings
    finding_ids = gd.list_findings(
        DetectorId=detector_id,
        FindingCriteria={
            'Criterion': {
                'severity': {
                    'Gte': 4  # Medium and above
                }
            }
        }
    )['FindingIds']

    print(f"Found {len(finding_ids)} findings (Medium and above)\n")

    if not finding_ids:
        print("No findings found!")
        return

    # Get finding details
    findings = gd.get_findings(
        DetectorId=detector_id,
        FindingIds=finding_ids[:10]  # First 10 only
    )['Findings']

    for finding in findings:
        severity = finding['Severity']
        title = finding['Title']
        type_ = finding['Type']
        
        if severity >= 7:
            label = "❌ HIGH"
        elif severity >= 4:
            label = "⚠️  MEDIUM"
        else:
            label = "ℹ️  LOW"
        
        print(f"{label} | {type_}")
        print(f"  {title}\n")

if __name__ == "__main__":
    gd = boto3.client('guardduty', region_name='us-east-2')
    check_guardduty(gd)
