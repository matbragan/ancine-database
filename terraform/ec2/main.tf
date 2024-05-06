data "http" "public_ip" {
    url = "http://ifconfig.me"
}

resource "aws_security_group" "airflow_access" {
    name        = "allow_airflow_access"
    description = "Security group to allow airflow access in personal machine"

    ingress {
        from_port   = 8080
        to_port     = 8080
        protocol    = "tcp"
        cidr_blocks = ["${data.http.public_ip.response_body}/32"]
    }

    ingress {
        from_port   = 22
        to_port     = 22
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

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_key_pair" "ancine_key" {
  key_name   = "ec2-ancine-key"
  public_key = file(var.ssh_public_key)
}

resource "aws_instance" "ancine_orchestration" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_class
  key_name               = aws_key_pair.ancine_key.key_name
  vpc_security_group_ids = [aws_security_group.airflow_access.id]

  tags = {
    Name = "ancine-orchestration"
  }
}