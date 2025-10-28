# Project variables (templated by Cookiecutter)
variable "project_name" {
  description = "Human-readable project name"
  type        = string
  default     = "risk_tribe"
}

# Environment configuration
variable "environment" {
  description = "Deployment environment (e.g. dev, staging, prod)"
  type        = string
  default     = "dev"
}

# AWS settings
variable "aws_region" {
  description = "AWS region to deploy resources in"
  type        = string
  default     = "us-east-1"
}

# 
variable "repo_name" {
  description = "The name of the repo"
  type        = string
  default     = "risk-tribe"
}