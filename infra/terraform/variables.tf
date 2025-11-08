variable "project_name" {
  type        = string
  default     = "risk_tribe"
  description = "Name of the project."
}

variable "aws_region" {
  type        = string
  default     = "eu-west-1"
  description = "AWS region to deploy resources."
}

variable "aws_profile" {
  type        = string
  default     = "default"
  description = "AWS CLI profile to use."
}
