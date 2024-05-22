output "arn" {
    value = aws_instance.ancine_orchestration.arn
}

output "public_ip" {
    value = aws_instance.ancine_orchestration.public_ip
}

output "public_dns" {
    value = aws_instance.ancine_orchestration.public_dns
}

output "vpc_security_group_ids" {
    value = aws_instance.ancine_orchestration.vpc_security_group_ids
}