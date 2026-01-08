# Flask App on AWS ECS Fargate

## Project Overview
This project demonstrates deploying a Python Flask app on AWS using Docker, EC2, and Terraform. The app is fully containerized and managed with Infrastructure-as-Code. Logs are collected in CloudWatch, and security best practices are applied.


## Features
- Containerized Flask app using Docker
- Deployed to AWS EC2 Instance
- Infrastructure managed with Terraform


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

 
