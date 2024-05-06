data "http" "local_public_ip" {
    url = "http://ifconfig.me"
}

data "aws_instance" "orchestration_instance" {
    filter {
        name   = "tag:Name"
        values = ["ancine-orchestration"]
    }
}

resource "aws_security_group" "postgres_access" {
    name        = "allow_postgres_access"
    description = "Security group to allow postgres access in personal machine"

    ingress {
        from_port   = 5432
        to_port     = 5432
        protocol    = "tcp"
        cidr_blocks = ["${data.http.local_public_ip.response_body}/32", "${data.aws_instance.orchestration_instance.private_ip}/32"]
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_db_instance" "ancine_rds" {
    db_name                = "ancine"
    engine                 = "postgres"
    engine_version         = "16.1"
    instance_class         = var.instance_class
    allocated_storage      = var.storage
    username               = var.db_username
    password               = var.db_password
    skip_final_snapshot    = true
    publicly_accessible    = true
    vpc_security_group_ids = [aws_security_group.postgres_access.id]
}