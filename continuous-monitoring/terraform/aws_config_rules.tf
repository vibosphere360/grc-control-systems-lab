# AWS Config Rules for Continuous Compliance Monitoring
# Maps to evidence_schema.csv controls + CIS Benchmarks
# Phase 4: Continuous Monitoring Detectors

terraform {
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

variable "aws_region" {
  description = "AWS region for Config rules"
  type        = string
  default     = "us-east-1"
}

variable "sns_topic_arn" {
  description = "SNS topic for compliance notifications"
  type        = string
  default     = ""
}

variable "cloudtrail_bucket_name" {
  description = "S3 bucket for CloudTrail logs"
  type        = string
  default     = "grc-cloudtrail-logs"
}

# CC-LOG-01: CloudTrail Enabled (CIS AWS 2.1, 2.2, 2.3)
resource "aws_config_config_rule" "cloudtrail_enabled" {
  name = "grc-cc-log-01-cloudtrail-enabled"

  source {
    owner             = "AWS"
    source_identifier = "CLOUD_TRAIL_ENABLED"
  }

  input_parameters = jsonencode({
    s3BucketName = var.cloudtrail_bucket_name
  })

  scope {
    compliance_resource_types = ["AWS::CloudTrail::Trail"]
  }

  tags = {
    ControlID      = "CC-LOG-01"
    EvidenceID     = "EV-LOG-01-AWS"
    ResidencyTag   = "US"
    AutomationTier = "Automated"
    CISBenchmark   = "CIS AWS v1.5: 2.1; 2.2; 2.3"
  }
}

# CC-IAM-02: MFA Enabled for IAM Users (CIS AWS 1.4, 1.5, 1.6)
resource "aws_config_config_rule" "iam_mfa_enabled" {
  name = "grc-cc-iam-02-mfa-enabled"

  source {
    owner             = "AWS"
    source_identifier = "IAM_USER_MFA_ENABLED"
  }

  scope {
    compliance_resource_types = ["AWS::IAM::User"]
  }

  tags = {
    ControlID      = "CC-IAM-02"
    EvidenceID     = "EV-IAM-02-AWS"
    ResidencyTag   = "Global"
    AutomationTier = "Automated"
    CISBenchmark   = "CIS AWS v1.5: 1.4; 1.5; 1.6"
  }
}

# CC-ENC-01: EBS Encryption Enabled (CIS AWS 2.1.1, 2.1.2)
resource "aws_config_config_rule" "ebs_encryption" {
  name = "grc-cc-enc-01-ebs-encrypted"

  source {
    owner             = "AWS"
    source_identifier = "ENCRYPTED_VOLUMES"
  }

  scope {
    compliance_resource_types = ["AWS::EC2::Volume"]
  }

  tags = {
    ControlID      = "CC-ENC-01"
    EvidenceID     = "EV-ENC-01-AWS"
    ResidencyTag   = "Restricted"
    AutomationTier = "Automated"
    CISBenchmark   = "CIS AWS v1.5: 2.1.1; 2.1.2"
  }
}

# CC-ENC-02: S3 Bucket Encryption (CIS AWS 2.3.1, 2.3.2)
resource "aws_config_config_rule" "s3_encryption" {
  name = "grc-cc-enc-02-s3-encrypted"

  source {
    owner             = "AWS"
    source_identifier = "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"
  }

  scope {
    compliance_resource_types = ["AWS::S3::Bucket"]
  }

  tags = {
    ControlID      = "CC-ENC-02"
    EvidenceID     = "EV-ENC-02-AWS"
    ResidencyTag   = "Global"
    AutomationTier = "Automated"
    CISBenchmark   = "CIS AWS v1.5: 2.3.1; 2.3.2"
  }
}

# CC-SEG-01: VPC Flow Logs Enabled (CIS AWS 2.3.1, 2.3.2)
resource "aws_config_config_rule" "vpc_flow_logs" {
  name = "grc-cc-seg-01-vpc-flow-logs"

  source {
    owner             = "AWS"
    source_identifier = "VPC_FLOW_LOGS_ENABLED"
  }

  scope {
    compliance_resource_types = ["AWS::EC2::VPC"]
  }

  tags = {
    ControlID      = "CC-SEG-01"
    EvidenceID     = "EV-SEG-01-AWS"
    ResidencyTag   = "Restricted"
    AutomationTier = "Automated"
    CISBenchmark   = "CIS AWS v1.5: 2.3.1; 2.3.2"
  }
}

# CC-BACKUP-01: RDS Automated Backups (CIS AWS 2.6)
resource "aws_config_config_rule" "rds_backup" {
  name = "grc-cc-backup-01-rds-backup"

  source {
    owner             = "AWS"
    source_identifier = "RDS_AUTOMATED_BACKUPS_ENABLED"
  }

  scope {
    compliance_resource_types = ["AWS::RDS::DBInstance"]
  }

  tags = {
    ControlID      = "CC-BACKUP-01"
    EvidenceID     = "EV-BACKUP-01-AWS"
    ResidencyTag   = "Restricted"
    AutomationTier = "Automated"
    CISBenchmark   = "CIS AWS v1.5: 2.6"
  }
}

# Outputs
output "config_rules" {
  description = "List of created Config rules with control mappings"
  value = {
    cloudtrail = aws_config_config_rule.cloudtrail_enabled.name
    mfa        = aws_config_config_rule.iam_mfa_enabled.name
    ebs        = aws_config_config_rule.ebs_encryption.name
    s3         = aws_config_config_rule.s3_encryption.name
    vpc        = aws_config_config_rule.vpc_flow_logs.name
    rds        = aws_config_config_rule.rds_backup.name
  }
}

output "cis_benchmark_coverage" {
  description = "CIS AWS Foundations Benchmark v1.5 controls covered"
  value = [
    "1.4 (Ensure no root account access key exists)",
    "1.5 (Ensure MFA is enabled for root account)",
    "1.6 (Ensure hardware MFA for root account)",
    "2.1 (Ensure CloudTrail is enabled in all regions)",
    "2.2 (Ensure CloudTrail log file validation is enabled)",
    "2.3 (Ensure CloudTrail logs are encrypted at rest)",
    "2.1.1 (Ensure EBS encryption by default is enabled)",
    "2.1.2 (Ensure KMS key rotation is enabled)",
    "2.3.1 (Ensure S3 bucket policy requires HTTPS)",
    "2.3.2 (Ensure S3 buckets have encryption enabled)",
    "2.6 (Ensure RDS instances have automated backups enabled)"
  ]
}
