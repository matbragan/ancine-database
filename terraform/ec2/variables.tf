variable "aws_region" {
    type    = string
    default = "us-east-1"
}

variable "instance_class" {
    description = "Instance class to EC2"
    type        = string
    default     = "t2.small"
}

variable "ssh_public_key" {
  description = "Path to the SSH public key file"
  type        = string
  default     = "~/.ssh/id_ed25519.pub"
}