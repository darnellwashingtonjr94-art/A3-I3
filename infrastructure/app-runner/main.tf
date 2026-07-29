provider "aws" {
  region = "us-east-1"
}

resource "aws_apprunner_service" "sol_plex_service" {
  service_name = "sol-plex-problems-api"

  source_configuration {
    authentication_configuration {
      connection_arn = "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection"
    }
    
    code_repository {
      repository_url = "https://github.com/darnellwashingtonjr94-art/Sol-Plex-Problems"
      
      source_code_version {
        type  = "BRANCH"
        value = "main"
      }
      
      code_configuration {
        configuration_source = "REPOSITORY" 
      }
    }
  }
}
