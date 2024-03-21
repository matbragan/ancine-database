data "http" "public_ip" {
    url = "http://ifconfig.me"
}

resource "aws_security_group" "mysql_access" {
    name        = "allow_mysql_access"
    description = "Security group to allow mysql access in personal machine"

    ingress {
        from_port   = 3306
        to_port     = 3306
        protocol    = "tcp"
        cidr_blocks = ["${data.http.public_ip.response_body}/32"]
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_db_instance" "ancine_rds" {
    allocated_storage      = 10
    db_name                = "ancinedb"
    engine                 = "mysql"
    engine_version         = "8.0.35"
    instance_class         = "db.t3.micro"
    username               = var.db_username
    password               = var.db_password
    parameter_group_name   = "default.mysql8.0"
    skip_final_snapshot    = true
    publicly_accessible    = true
    vpc_security_group_ids = [aws_security_group.mysql_access.id]
}