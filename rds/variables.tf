variable "aws_region" {
    type    = string
    default = "us-east-1"
}

variable "db_username" {
    description = "Database master user"
    type        = string
    sensitive   = true
}

variable "db_password" {
    description = "Database master user password"
    type        = string
    sensitive   = true
}