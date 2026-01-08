provider "aws" {
  region = "eu-north-1"
}

# Existing security group
variable "sg_id" {
  default = "sg-0c25cc22bda184ea6"
}

# EC2 instance with Flask app
resource "aws_instance" "TerraformDemoInstance" {
  ami           = "ami-074211ec8e88502be" # Amazon Linux 2 AMI
  instance_type = "t3.micro"
  key_name      = "new"  # your key pair name

  vpc_security_group_ids = [var.sg_id]

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y python3 python3-pip
              pip3 install flask
              
              # Create the app directory
              mkdir -p /home/ec2-user/templates
              
              # Copy the main app file
              cat << 'APP' > /home/ec2-user/app.py
              ${file("app.py")}
              APP
              
              # Copy the index.html template
              cat << 'INDEX' > /home/ec2-user/templates/index.html
              ${file("templates/index.html")}
              INDEX
              
              # Copy the result.html template
              cat << 'RESULT' > /home/ec2-user/templates/result.html
              ${file("templates/result.html")}
              RESULT
              
              # Set permissions
              chmod +x /home/ec2-user/app.py
              chown -R ec2-user:ec2-user /home/ec2-user
              
              # Run the Flask app
              cd /home/ec2-user
              nohup python3 app.py > app.log 2>&1 
              EOF

  tags = {
    Name = "TerraformDemoInstance"
  }
}



# Output URL for Flask
output "website_url" {
  value = "http://${aws_instance.TerraformDemoInstance.public_ip}:5000"
}


