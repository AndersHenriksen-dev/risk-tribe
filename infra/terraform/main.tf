resource "aws_s3_bucket" "example" {
  bucket = "${var.project_name}-example"
}

output "example_bucket_name" {
  value = aws_s3_bucket.example.bucket
}
