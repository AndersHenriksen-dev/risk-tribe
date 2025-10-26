output "s3_bucket_name" {
  description = "Name of the S3 bucket created"
  value       = aws_s3_bucket.project_bucket.bucket
}

output "region" {
  description = "AWS region used for deployment"
  value       = var.aws_region
}
