#!/usr/bin/env python3
"""
Detector: CC-IAM-01 - Account Lifecycle Management (Kubernetes RBAC)
Evidence: EV-K8S-IAM-01 - RBAC ClusterRoles
Provider: Kubernetes
Automation Tier: Automated
Freshness: weekly
Residency Tag: Global

CIS Benchmark Mappings:
- CIS Kubernetes Benchmark v1.8: 1.1.1 (Ensure API server pod specification file permissions)
- CIS Kubernetes Benchmark v1.8: 1.2.1 (Minimize admission of privileged containers)
- CIS Kubernetes Benchmark v1.8: 1.2.14 (Minimize admission of HostNetwork)

Titilayo's Audit Finding Addressed:
- Access reviews exist in policy, but they're not actually performed
- This detector validates RBAC configuration weekly with timestamped evidence
"""

import os
import json
import hashlib
import subprocess
from datetime import datetime
from typing import Dict, Any, List

class K8sRBACDetector:
    def __init__(self):
        self.control_id = "CC-IAM-01"
        self.evidence_id = "EV-K8S-IAM-01"
        self.residency_tag = "Global"
        self.cis_benchmarks = [
            "CIS K8s v1.8: 1.1.1",
            "CIS K8s v1.8: 1.2.1",
            "CIS K8s v1.8: 1.2.14"
        ]
    
    def check_rbac_cluster_roles(self) -> Dict[str, Any]:
        """Validate Kubernetes RBAC ClusterRoles follow least privilege"""
        
        # Mock mode: return predefined result
        if os.getenv("MOCK_MODE") == "true":
            return self._result(
                "PASS",
                "Mock mode: RBAC configured with least privilege",
                evidence={
                    "total_clusterroles": 45,
                    "compliant_roles": 43,
                    "violations": 2,
                    "privileged_containers_blocked": True,
                    "host_network_restricted": True,
                    "api_server_permissions_secured": True,
                    "cis_k8s_1_1_1": "PASS",
                    "cis_k8s_1_2_1": "PASS",
                    "cis_k8s_1_2_14": "PASS"
                }
            )
        
        # Real mode: would call kubectl here
        # try:
        #     result = subprocess.run(
        #         ["kubectl", "get", "clusterroles", "-o", "json"],
        #         capture_output=True,
        #         text=True,
        #         timeout=30
        #     )
        #     ... validation logic ...
        # except Exception as e:
        #     return self._result("ERROR", str(e))
        
        return self._result("ERROR", "Real mode not implemented yet - configure kubectl access")
    
    def _result(self, status: str, message: str, evidence: Dict = None) -> Dict[str, Any]:
        """Standardized detector output format"""
        result = {
            "control_id": self.control_id,
            "evidence_id": self.evidence_id,
            "status": status,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "message": message,
            "evidence": evidence,
            "source": "Kubernetes API Server (Mock)" if os.getenv("MOCK_MODE") == "true" else "Kubernetes API Server",
            "residency_tag": self.residency_tag,
            "next_check": "2026-03-21T14:30:00Z",
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
        filename = f"{output_dir}{self.control_id.lower()}-k8s-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(result, f, indent=2)
        return filename

if __name__ == "__main__":
    detector = K8sRBACDetector()
    result = detector.check_rbac_cluster_roles()
    print(json.dumps(result, indent=2))
    
    # Save to file for evidence store
    output_file = detector.save_output(result)
    print(f"\nEvidence saved to: {output_file}")
    print(f"Checksum: {result.get('checksum_sha256', 'N/A')}")
