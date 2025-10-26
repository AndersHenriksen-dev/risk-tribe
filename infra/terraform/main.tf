terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Example resource: an S3 bucket named after the project
resource "aws_s3_bucket" "project_bucket" {
  bucket = "${var.repo_name}-bucket"
  tags = {
    Name        = var.repo_name
    Environment = var.environment
  }
}
