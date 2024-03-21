output "arn" {
    value = aws_db_instance.ancine_rds.arn
}

output "endpoint" {
    value = aws_db_instance.ancine_rds.endpoint
}

output "vpc_security_group_ids" {
    value = aws_db_instance.ancine_rds.vpc_security_group_ids
}

output "ingress_cidr_blocks" {
    value = aws_security_group.mysql_access.ingress.cidr_blocks
}