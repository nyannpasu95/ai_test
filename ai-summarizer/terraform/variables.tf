variable "region" {
  description = "AWS region"
  default     = "ap-northeast-1"
}

variable "lambda_function_name" {
  description = "Lambda function name"
  default     = "chatbot"
}

variable "api_gateway_name" {
  description = "API Gateway name"
  default     = "ChatbotAPI"
}
