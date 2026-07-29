#!/bin/bash
yum update -y
yum install -y docker git

systemctl start docker
systemctl enable docker
usermod -aG docker ec2-user

git clone https://github.com/darnellwashingtonjr94-art/Sol-Plex-Problems.git /home/ec2-user/Sol-Plex-Problems
cd /home/ec2-user/Sol-Plex-Problems

docker build -t sol-plex-problems:v0.1.5 .
docker run -d -p 80:80 --restart unless-stopped --name sol-plex-app sol-plex-problems:v0.1.5
