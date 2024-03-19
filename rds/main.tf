data "http" "public_ip" {
    url = "http://ifconfig.me"
}

resource "aws_security_group" "allow_host" {
    name        = "allow_host_to_mysql"
    description = "Security group to allow mysql port access from host machine"

    ingress {
        from_port   = 3306
        to_port     = 3306
        protocol    = "tcp"
        cidr_blocks = ["${data.http.public_ip.response_body}/32"]
    }
}

resource "aws_db_instance" "ancine_rds" {
    allocated_storage      = 10
    db_name                = "ancinedb"
    engine                 = "mysql"
    engine_version         = "8.0"
    instance_class         = "db.t3.micro"
    username               = var.db_username
    password               = var.db_password
    parameter_group_name   = "default.mysql8.0"
    skip_final_snapshot    = true
    vpc_security_group_ids = [aws_security_group.allow_host.id]
}