# Configure AWS
provider "aws" {
  region = "eu-west-2"
}

# Security group - allows HTTP traffic
resource "aws_security_group" "web" {
  name = "allow-http"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 instance with web server
resource "aws_instance" "web" {
  ami           = "ami-0b9932f4918a00c4f"
  instance_type = "t2.micro"
  
  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = <<-EOF
              #!/bin/bash
              yum install -y httpd
              systemctl start httpd
              echo "<h1>Hello from Terraform!</h1>" > /var/www/html/index.html
              EOF

  tags = {
    Name = "terraform-web-server"
  }
}

# Output the web URL
output "website_url" {
  value = "http://${aws_instance.web.public_ip}"
} 