# Security Journey 🔐

**Career transition into Cloud Security.** Background in economics and risk analytics, now building hands-on AWS security skills — automation, threat detection, and least-privilege design.

📍 Targeting: Cloud Security / GRC roles
🎯 In progress: CompTIA Security+, AWS Security Specialty

---

## 🛠️ Featured Projects

### AWS Security Audit Toolkit
A set of Python (boto3) scripts that automate common cloud security checks. Each one solves a real problem that causes breaches in the wild.

| Script | What it does | Why it matters |
|--------|--------------|----------------|
| [`s3_audit.py`](scripts/s3_audit.py) | Audits S3 buckets for public access, encryption, versioning | Misconfigured S3 caused the Capital One breach |
| [`iam_key_audit.py`](scripts/iam_key_audit.py) | Flags IAM access keys older than 90 days | Stale keys are a top cause of credential compromise |
| [`cloudtrail_audit.py`](scripts/cloudtrail_audit.py) | Scans CloudTrail for dangerous events (DeleteBucket, StopLogging, etc.) | Detects attacker activity and log tampering |
| [`guardduty_audit.py`](scripts/guardduty_audit.py) | Pulls GuardDuty findings by severity via API | Programmatic threat triage at scale |
| [`security_check.sh`](labs/04-automation/security_check.sh) | One-command full account security check | Fast posture assessment for a SOC |

### Hands-On Labs
Documented practical work, organized by domain:
- [Linux & Networking](labs/01-linux-and-networking) — file permissions, log analysis, password hashing
- [AWS Core](labs/02-aws-core) — S3 bucket policies, HTTPS enforcement
- [AWS Monitoring](labs/03-aws-monitoring) — CloudTrail audit logging
- [Automation](labs/04-automation) — AWS CLI, Bash scripting

---

## 💡 Skills Demonstrated

**Cloud:** AWS (EC2, S3, IAM, VPC, CloudWatch, CloudTrail, GuardDuty)
**Automation:** Python (boto3), Bash, AWS CLI
**Security:** Least privilege, IAM policy design, threat detection, incident response basics, defense in depth
**Tools:** Linux, Git, fail2ban, ufw

---

## 📓 Learning Journal

Daily log of the journey — including mistakes and how I fixed them. The messy reality of learning, kept honest.

---

## Day 1 — Networking & Linux Basics
**Date:** May 23, 2026 | **Time:** ~3 hours

First time touching Linux seriously. More hands-on than I expected.

### What clicked today:
- DNS is basically a phone book — without it you can't reach anything
- Found out TikTok runs through Akamai CDN, not their own servers
- Linux file permissions finally make sense — rwxrwxrwx = 777 = dangerous
- /etc/shadow stores password hashes, not actual passwords
- John the Ripper cracked "password123" in under a second using rockyou.txt

### What confused me at first:
- Difference between cat and ls — one reads files, other lists directories
- Why sudo is needed for some commands but not others
- The difference between 400 and 600 file permissions

### Hands-on:
- Ran nslookup on Google, YouTube, TikTok — compared IPs
- Traced route to Google — 7 hops from my machine
- Built security_lab directory, set proper file permissions
- Read /etc/passwd and /etc/shadow — understood every field
- Analyzed auth.log and found my own failed sudo attempts
- Cracked a password hash using John the Ripper + rockyou.txt wordlist

### Key insight:
Hashing is NOT encryption. You can't reverse a hash —
you can only guess and compare. That's why weak passwords
are dangerous even when "hashed".

---

## Day 2 — SSH, AWS EC2 & Real Attacks
**Date:** May 25, 2026 | **Time:** ~4 hours

First time in a real cloud environment. Things broke. Learned a lot.

### What happened:
Launched my first EC2 instance on AWS.
Within a few hours — found real attacks in the logs.
A bot from Rostelecom (Russia)  tried 26 different usernames:
<img width="1725" height="921" alt="2026-05-25_22-13-50" src="https://github.com/user-attachments/assets/c6caa878-0a95-40ef-ae60-5585771ae1fc" />
admin, pi, oracle, ftpuser, test1, test2, usuario...
<img width="1721" height="924" alt="2026-05-25_22-15-07" src="https://github.com/user-attachments/assets/76b84a86-e09a-4969-94b4-c7717b5426fc" />

Just a script running 24/7 scanning the entire internet.

### The mistake that locked me out:
Enabled ufw firewall WITHOUT allowing SSH port 22 first.
Lost access to the server completely.

Spent time figuring out recovery:
created IAM role → attached SSM policy → rebooted →
connected via Session Manager through browser.

The correct order I'll never forget:
sudo ufw allow 22   ← ALWAYS first
sudo ufw enable     ← only then

### What I built:
- EC2 server in AWS Ohio region
- SSH key-based authentication (ed25519)
- ufw firewall with attacker IP blocked
- fail2ban — auto-blocks brute force attempts
- Automatic security updates
- CloudWatch Agent — logs shipped to AWS
- Email alert when attack threshold exceeded

### What clicked:
IAM roles are not about humans — they're permissions
for AWS services to talk to each other.
My server needed a role to send logs to CloudWatch.
Without it: AccessDenied.

### Takeaway:
Real attacks start within hours of launching a server.
Defense in depth matters — Security Group + ufw + fail2ban
are three separate layers, each catches what the other misses.


My EC2 instance running in AWS Ohio:

<img width="1045" height="388" alt="1" src="https://github.com/user-attachments/assets/6ac447ff-a9a9-4b41-9adb-e0929e091c91" />

CloudWatch showing real-time logs from the server —
you can see the server shutdown, restart, and my SSH connection:

<img width="896" height="597" alt="2" src="https://github.com/user-attachments/assets/64f3602b-494d-47d1-beb8-d23f5a13ab91" />

---

## Day 3 — S3, IAM, VPC

**Date:** May 26, 2026

Long day. Started with auditing my own Windows machine before touching anything in AWS.
Ran netstat, checked startup programs. Found Yandex Browser sitting in startup — removed it.
Felt weird auditing my own computer but it made sense to start there.

Then moved to S3. Created a bucket and immediately wrote a policy to block HTTP —
any unencrypted connection gets AccessDenied. Tested it myself by opening the file URL
in a browser as an anonymous user.

<img width="1787" height="611" alt="2026-05-25_22-48-11" src="https://github.com/user-attachments/assets/ef17d08d-f457-447c-b2df-b738a2a30773" />

Got blocked. That's the Capital One breach in reverse — they had a misconfigured bucket, I didn't.

IAM was eye-opening. Noticed tim-admin had AdministratorAccess attached directly
to the user, not through a group. That's bad practice — if you have 10 admins
and need to change permissions, you'd have to touch 10 users individually.
Moved everything to a group.

<img width="2462" height="1062" alt="2026-05-25_23-09-10" src="https://github.com/user-attachments/assets/48a31f6c-9d78-4977-b8d6-814d1cd8e900" />

Also noticed tim-admin has access to 449 AWS services. I use maybe 5.
Classic overprivileged account — something to fix when I learn custom IAM policies.

VPC finally clicked today. I always knew there was "some network stuff" between
the internet and my server but never understood what. Now I do:

Internet → Internet Gateway → Route table → Subnet → Security Group → EC2 → ufw → fail2ban → SSH

The route table is the key. One line — 0.0.0.0/0 → igw-xxx — is what makes a subnet public.
Remove it and the subnet goes dark. That simple.

<img width="2377" height="1325" alt="2026-05-25_23-19-38" src="https://github.com/user-attachments/assets/8fdaef6f-a75c-447b-9b45-f34d98aea2c8" />

Default VPC has all subnets public. Fine for learning, bad for production.

---

## Day 4 — Python Scripts & CloudTrail

**Date:** May 28, 2026

Wrote two scripts today. First time actually building something from scratch
rather than just running commands.

iam_key_audit.py checks if any IAM access keys are older than 90 days.
Sounds simple but this is a real thing — companies get breached because
someone left an old key sitting around for years and never rotated it.

cloudtrail_audit.py pulls the last 24 hours of AWS activity and flags
dangerous events — someone deleting a bucket, stopping logging, messing with IAM.
Ran it and found 50 events. Nothing suspicious. But now I have a script
that would catch it if something did happen.

One thing that finally made sense — boto3 scripts run from my laptop, not from EC2.
My local machine connects directly to AWS API over the internet.
I kept thinking I needed the server running to use boto3. I didn't.
EC2 is just a VM. IAM, S3, CloudTrail — completely separate services.

---

## Day 5 — AWS CLI & Bash Scripts & IAM Policies

**Date:** May 31, 2026

Three things today, all connected.

Started with AWS CLI — basically the same as opening the AWS console
but from the terminal. One command instead of five clicks.
First thing I ran into: my config had output = аутпоыjson written in Cyrillic.
Classic copy-paste mistake from switching keyboard layouts.
Fixed it in ~/.aws/config and everything worked.

aws sts get-caller-identity is now my first command whenever I open a new session.
It's just whoami for AWS — confirms I'm connected and who I am.

<img width="784" height="842" alt="Screenshot 2026-05-30 223939" src="https://github.com/user-attachments/assets/bff4b4eb-ad0d-438c-a113-1e7f3b17ae3d" />


Then wrote a Bash script that runs a full security check in one shot —
who's logged in, what buckets exist, IAM users, CloudTrail status, MFA status.
Before this I was running each command separately. Now it's one file.

The MFA check was the interesting part — a for loop goes through every IAM user
and asks AWS if they have an MFA device registered. If the list comes back empty,
no MFA. Simple but effective. Something like this would actually run in a real SOC.

<img width="557" height="577" alt="Screenshot 2026-05-30 225007" src="https://github.com/user-attachments/assets/c46c3cbd-981c-4a95-8f50-ffab08a7d6f9" />


Last thing — IAM Policies. Wrote my first custom policy from scratch in JSON.
Created SecurityAnalystReadOnly — gives access to read CloudTrail logs and nothing else.
Three actions: LookupEvents, GetTrailStatus, DescribeTrails. That's it.
449 services blocked by default. Least privilege in action.

<img width="1187" height="772" alt="Screenshot 2026-05-30 235301" src="https://github.com/user-attachments/assets/6f340619-8338-48df-9b3a-b3db16d42a84" />

Deny always beats Allow — that's the rule I'll remember from today.
Doesn't matter how many policies say yes, one Deny shuts everything down.

Also learned basic Git from the terminal today — clone, add, commit, push.

Tried to restructure the labs folder and ran into two problems.
First attempt failed — moved files with mv and two READMEs got lost in the process.
Had to revert the whole commit and start over.

Second problem was my own mistake — accidentally pasted my GitHub token into the chat
while asking for help. Had to immediately delete it on GitHub and generate a new one.
Classic security fail while learning security.

Second attempt worked — used cp instead of mv so nothing got overwritten,
then deleted the old folders separately. All files survived this time.

Lesson: revert is not scary. Git keeps everything.
And never paste tokens anywhere except the terminal.
<img width="595" height="298" alt="Screenshot 2026-05-31 003240" src="https://github.com/user-attachments/assets/b8bffec0-d69f-469e-a7b4-b8043cd155a4" />
<img width="509" height="140" alt="Screenshot 2026-05-31 003316" src="https://github.com/user-attachments/assets/27f29acd-3dc7-4a2b-9859-d183eb447af3" />

---

## Day 6 — GuardDuty

**Date:** June 2, 2026

Finally got GuardDuty working — had to sort out the AWS account first.

Enabled it and immediately generated 404 sample findings to see what real threats look like.
AWS has a built-in function for this — one click and you get the full catalog of everything
GuardDuty can detect. Good way to learn the threat landscape without waiting for actual attackers.

<img width="1178" height="928" alt="Screenshot 2026-06-02 214610" src="https://github.com/user-attachments/assets/01d5c27e-175c-4616-bba7-2caedee1ea72" />

Two findings that stuck with me:

EC2 communicating with a Tor entry node — HIGH severity.
Your server talking to Tor is not normal. Means it's probably compromised and someone
is using it to hide their tracks. First move in real life: isolate the instance, then investigate.

<img width="729" height="875" alt="Screenshot 2026-06-02 214753" src="https://github.com/user-attachments/assets/9c27c8d4-7e66-41e0-ba4f-6bd40c34ac3b" />


IAMUser invoking anomalous APIs — LOW severity but interesting.
GuardDuty learns what's normal for each user and flags anything unusual.
This one showed AccessDenied on two calls — attacker tried but got blocked.
Resource affected was an Access Key, not a console login. Someone got hold of a key, not a password.

Then wrote guardduty_audit.py — pulls findings via boto3 instead of clicking through the console.
Filters by severity (Medium and above), shows type and description for each one.
Same data as the console, but now I can automate it or plug it into a bigger workflow.

<img width="878" height="647" alt="Screenshot 2026-06-02 220439" src="https://github.com/user-attachments/assets/7945fe8b-e48f-460c-99f4-40f0f75e0675" />

