# Flask App on AWS ECS Fargate

## Project Overview
This project demonstrates deploying a Python Flask app on AWS using Docker, ECS Fargate, and Terraform. The app is fully containerized and managed with Infrastructure-as-Code. Logs are collected in CloudWatch, and security best practices are applied.


## Features
- Containerized Flask app using Docker
- Deployed to AWS ECS Fargate
- Infrastructure managed with Terraform
- Secure IAM roles for ECS tasks
- CloudWatch logs and alarms for monitoring
- Security Groups restrict traffic to only required ports

## Setup Instructions

### Prerequisites
- AWS account with admin privileges
- Terraform installed
- Docker installed
- AWS CLI configured

### Infrastructure Deployment
```bash
terraform init
terraform plan
terraform apply

 
