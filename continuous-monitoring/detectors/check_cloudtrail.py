#!/usr/bin/env python3
"""
Detector: CC-LOG-01 - Security Event Logging
Evidence: EV-LOG-01-AWS - CloudTrail Log Integrity
Provider: AWS
Automation Tier: Automated
Freshness: hourly
Residency Tag: US

CIS Benchmark Mappings:
- CIS AWS Foundations Benchmark v1.5: 2.1 (Ensure CloudTrail is enabled in all regions)
- CIS AWS Foundations Benchmark v1.5: 2.2 (Ensure CloudTrail log file validation is enabled)
- CIS AWS Foundations Benchmark v1.5: 2.3 (Ensure CloudTrail logs are encrypted at rest)

Titilayo's Audit Finding Addressed:
- Policies exist, but there's no proof they're being enforced
- This detector provides timestamped, checksummed evidence of actual enforcement
"""

import os
import json
import sys
import hashlib
from datetime import datetime
from typing import Dict, Any

class CloudTrailDetector:
    def __init__(self, region: str = "us-east-1"):
        self.client = None  # Would be boto3.client("cloudtrail") in real mode
        self.region = region
        self.control_id = "CC-LOG-01"
        self.evidence_id = "EV-LOG-01-AWS"
        self.residency_tag = "US"
        self.cis_benchmarks = [
            "CIS AWS v1.5: 2.1",
            "CIS AWS v1.5: 2.2",
            "CIS AWS v1.5: 2.3"
        ]
    
    def check_cloudtrail_enabled(self) -> Dict[str, Any]:
        """Validate CloudTrail is enabled with log file validation"""
        
        # Mock mode: return predefined result without hitting AWS API
        if os.getenv("MOCK_MODE") == "true":
            return self._result(
                "PASS",
                "Mock mode: CloudTrail enabled and validating logs",
                evidence={
                    "is_multi_region": True,
                    "log_file_validation": True,
                    "s3_bucket_defined": True,
                    "cloud_watch_logs_defined": True,
                    "kms_encryption": True,
                    "cis_aws_2_1": "PASS",
                    "cis_aws_2_2": "PASS",
                    "cis_aws_2_3": "PASS"
                }
            )
        
        # Real mode: would call boto3 here
        # try:
        #     response = self.client.describe_trails()
        #     ... validation logic ...
        # except Exception as e:
        #     return self._result("ERROR", str(e))
        
        return self._result("ERROR", "Real mode not implemented yet - configure AWS credentials")
    
    def _result(self, status: str, message: str, evidence: Dict = None) -> Dict[str, Any]:
        """Standardized detector output format"""
        result = {
            "control_id": self.control_id,
            "evidence_id": self.evidence_id,
            "status": status,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "message": message,
            "evidence": evidence,
            "source": "AWS CloudTrail API (Mock)" if os.getenv("MOCK_MODE") == "true" else "AWS CloudTrail API",
            "residency_tag": self.residency_tag,
            "next_check": "2026-03-14T15:30:00Z",
            "cis_benchmarks": self.cis_benchmarks
        }
        
        # Add checksum for integrity verification
        json_str = json.dumps(result, sort_keys=True)
        result["checksum_sha256"] = hashlib.sha256(json_str.encode()).hexdigest()
        
        return result
    
    def save_output(self, result: Dict[str, Any], output_dir: str = "../outputs/") -> str:
        """Save detector result to JSON file with checksum"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{output_dir}{self.control_id.lower()}-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(result, f, indent=2)
        return filename

if __name__ == "__main__":
    detector = CloudTrailDetector()
    result = detector.check_cloudtrail_enabled()
    print(json.dumps(result, indent=2))
    
    # Save to file for evidence store
    output_file = detector.save_output(result)

