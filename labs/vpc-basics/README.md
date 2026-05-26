# VPC Basics — Understanding Cloud Networking
**Date:** May 26, 2026

Wanted to understand how my EC2 server actually connects to the internet.
Turns out there's a whole chain of components involved.

## My VPC structure

Default VPC: vpc-0a524bfb55d323d70
Address space: 172.31.0.0/16 (65,536 IP addresses)

3 subnets across 3 availability zones:
- us-east-2a → 172.31.0.0/20
- us-east-2b → 172.31.16.0/20
- us-east-2c → 172.31.32.0/20 ← my server was here

<img width="2455" height="1443" alt="2026-05-25_23-14-45" src="https://github.com/user-attachments/assets/dd35993a-8b6c-4730-bc9d-6aebcc62668d" />

## How traffic reaches my server

Looked at the route table for my subnet. Two rules:

<img width="2377" height="1325" alt="2026-05-25_23-19-38" src="https://github.com/user-attachments/assets/7a5e0d4e-4aa9-44a4-9297-a221cc964e51" />

First rule: 172.31.0.0/16 → local
Traffic between servers in the same VPC stays internal.

Second rule: 0.0.0.0/0 → igw-0fd3ef10f318781ca
Everything else goes through the Internet Gateway.
This one line is what makes a subnet public.
Remove it and the subnet has zero internet access.

## The full traffic chain

Internet
→ Internet Gateway
→ Route table
→ Subnet us-east-2c
→ Security Group (port 22 allowed from my IP only)
→ EC2 instance
→ ufw (port 22 allowed)
→ fail2ban (blocks brute force)
→ SSH daemon

## What I'd do differently in production

Default VPC has all subnets public — not ideal.
Real architecture would look like:

Public subnets: load balancers, bastion host
Private subnets: web servers, API servers  
Isolated subnets: databases (no internet access at all)

Database in a private subnet = attacker can't reach it directly
even if they know the IP address.

## Key terms learned
- VPC — isolated network inside AWS
- Subnet — segment of the VPC
- Internet Gateway — door between VPC and internet
- Route table — rules for where traffic goes
- CIDR — IP address range notation (172.31.0.0/16)
- Public subnet — has route to internet gateway
- Private subnet — no route to internet gateway
