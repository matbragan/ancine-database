variable "aws_region" {
    type    = string
    default = "us-east-1"
}

variable "instance_class" {
    description = "Instance class to Database"
    type        = string
    default     = "db.t3.micro"
}

variable "storage" {
    description = "Allocated storage in GB to Database"
    type        = number
    default     = 20
}

variable "db_username" {
    description = "Database master user"
    type        = string
    default     = "admin"
}

variable "db_password" {
    description = "Database master user password"
    type        = string
    sensitive   = true
}