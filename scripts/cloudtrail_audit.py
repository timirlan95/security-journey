import boto3
from datetime import datetime, timezone, timedelta

def check_cloudtrail(ct):
    print("=" * 40)
    print("CLOUDTRAIL SECURITY AUDIT")
    print("=" * 40 + "\n")

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(days=1)

    suspicious_events = [
        'DeleteBucket',
        'DeleteTrail',
        'StopLogging',
        'DeleteUser',
        'AttachUserPolicy',
    ]

    response = ct.lookup_events(
        StartTime=start_time,
        EndTime=end_time,
    )

    events = response['Events']
    print(f"Found {len(events)} events in last 24 hours\n")

    for event in events:
        event_name = event['EventName']
        user = event.get('Username', 'Unknown')
        time = event['EventTime'].strftime('%Y-%m-%d %H:%M')

        if event_name in suspicious_events:
            print(f"  ❌ SUSPICIOUS: {event_name} by {user} at {time}")
        else:
            print(f"  ✅ {event_name} at {time}")

if __name__ == "__main__":
    ct = boto3.client('cloudtrail')
    check_cloudtrail(ct)
