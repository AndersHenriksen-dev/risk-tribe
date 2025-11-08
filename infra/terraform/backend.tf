terraform {
  backend "s3" {
    bucket         = "AWS_BUCKET_FOR_TF_STATE"
    key            = "terraform.tfstate"
    region         = "eu-west-1"
    dynamodb_table = "AWS_DYNAMODB_LOCK_TABLE"
    encrypt        = true
  }
}