resource "aws_s3_bucket" "static_files" {
  bucket = "chatbot-static-files-20240523"

  website {
    index_document = "index.html"
  }
}