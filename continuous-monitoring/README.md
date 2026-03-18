markdown
1234567891011121314151617181920212223
# Continuous Monitoring DetectorsThis module contains automated detectors that validate control state against the evidence schema defined in Phase 3. Detectors can be run locally, in CI/CD pipelines, or on a schedule via Lambda/Cloud Functions.**Philosophy:** Compliance is not point-in-time audit preparation — it's continuous operational governance. Each detector outputs timestamped, checksummed evidence with residency tags and control ownership metadata.---## Quick Start### Prerequisites- Python 3.8+- AWS CLI configured (`aws configure`) for real mode- kubectl configured (for Kubernetes detectors)- Terraform 1.0+ (for IaC deployment)### Run All Detectors (Mock Mode)```bashcd detectors/export MOCK_MODE=truepython3 run_all_detectors.py

Run Single Detector
bash
1
python3 check_cloudtrail.py

Validate Terraform (No Apply)
bash
1234
cd ../terraformterraform initterraform validateterraform plan

Detectors Included
Detector
Control
CIS Benchmark
Automation Tier
Freshness
Residency
check_cloudtrail.py
CC-LOG-01
CIS AWS v1.5: 2.1, 2.2, 2.3
Automated
hourly
US
check_mfa.py
CC-IAM-02
CIS AWS v1.5: 1.4, 1.5, 1.6
Automated
daily
Global
check_k8s_rbac.py
CC-IAM-01
CIS K8s v1.8: 1.1.1, 1.2.1, 1.2.14
Automated
weekly
Global
Planned Detectors:
check_encryption.py (CC-ENC-01/02) — KMS key rotation + TLS config
check_vulnerability.py (CC-VULN-01) — Inspector/Trivy scan results
check_backup.py (CC-BACKUP-01) — Backup job completion + recovery tests
check_network_seg.py (CC-SEG-01) — VPC flow logs + firewall rules (ITAR)
Evidence Output Format
Each detector returns standardized JSON with governance metadata. Here's actual output from running python3 check_cloudtrail.py:
json
1234567891011121314151617181920212223242526
{  "control_id": "CC-LOG-01",  "evidence_id": "EV-LOG-01-AWS",  "status": "PASS",  "timestamp": "2026-03-16T20:14:48.049602Z",  "message": "Mock mode: CloudTrail enabled and validating logs",  "evidence": {    "is_multi_region": true,    "log_file_validation": true,    "s3_bucket_defined": true,    "cloud_watch_logs_defined": true,    "kms_encryption": true,    "cis_aws_2_1": "PASS",    "cis_aws_2_2": "PASS",    "cis_aws_2_3": "PASS"  },  "source": "AWS CloudTrail API (Mock)",  "residency_tag": "US",  "next_check": "2026-03-14T15:30:00Z",  "cis_benchmarks": [    "CIS AWS v1.5: 2.1",    "CIS AWS v1.5: 2.2",    "CIS AWS v1.5: 2.3"  ],  "checksum_sha256": "02d66d311ec4dbdec764d88b0b9490cd7189879e6d9c2a9e56d989eb9d1f88df"}

Key Fields for Governance:
Field
Purpose
Example from Output
residency_tag
Enforces data boundary requirements
"US" → FedRAMP-compliant region only
control_owner
Designated owner for remediation
SecOps Lead (in evidence_schema.csv)
escalation_path
Escalation chain for FAIL status
CISO → Legal → Board
checksum_sha256
Integrity verification for auditors
02d66d311ec4dbdec764d88b0b9490cd7189879e6d9c2a9e56d989eb9d1f88df
cis_benchmarks
CIS AWS Foundations Benchmark mappings
2.1, 2.2, 2.3 (CloudTrail controls)
freshness
SLA for next collection
hourly (next_check timestamp)
Evidence Ownership & Delivery Flow
Output
Owner
Storage
Access
Retention
Detector JSON
Detector Script
Local outputs/ (ephemeral)
Developer
24 hours
Evidence File
Control Owner
S3 / ServiceNow / OSCAL
Control Owner + Assessor
3-7 years
Aggregated Package
GRC Lead
FedRAMP Submission Portal
FedRAMP + Agency
7 years
Dashboard Metrics
SecOps
Grafana / QuickSight
Leadership Team
90 days
Flow Diagram:
1234567891011
Detector Script (Python)    ↓Standardized JSON Output (with checksum + residency tag)    ↓Evidence Store (S3 with Object Lock for CUI)    ↓GRC Platform (ServiceNow GRC / Archer)    ↓Dashboard (Grafana / QuickSight)    ↓Assessor Review (3PAO / FedRAMP)

Residency Enforcement
residency_tag = "US" → S3 bucket in us-east-1 only (FedRAMP)
residency_tag = "Restricted" → S3 bucket with CUI controls + access logging (ITAR)
residency_tag = "Global" → Any approved region (commercial)
Integrity Verification
Every evidence file includes:
SHA-256 checksum in output JSON
Timestamp + detector version
Immutable storage option (S3 Object Lock for CUI)
Access logging via CloudTrail / Azure Monitor
Terraform Infrastructure
Deploy AWS Config rules for continuous monitoring:
bash
1234
cd terraform/terraform initterraform validateterraform plan

Tags Applied to All Resources
Tag
Purpose
Example
ControlID
Maps to canonical control library
CC-LOG-01
EvidenceID
Maps to evidence dictionary
EV-LOG-01-AWS
ResidencyTag
Enforces data boundary requirements
US, Restricted
CISBenchmark
Tracks CIS AWS Foundations Benchmark coverage
CIS AWS v1.5: 2.1
AutomationTier
Indicates automation level
Automated, Partial, Manual
Cost Estimate
Resource
Monthly Cost (USD)
Notes
AWS Config Rules
~$25
6 rules @ ~$4/rule
S3 Storage (evidence)
~$5
10 GB @ $0.023/GB
CloudWatch Logs
~$10
Detector execution logs
Total
~$40/month
vs. $16K/month ServiceNow GRC
Addressing Common Audit Findings
This module directly addresses audit failures identified by practitioners (Titilayo Adamu, Kimly Hong):
Audit Finding
How This Module Addresses It
Access reviews documented but not performed
Detectors validate MFA/RBAC daily with timestamped evidence
Policies exist but not enforced
Automated validation checks actual state vs. policy
Evidence missing at audit time
Continuous collection + checksummed output
Risk registers not updated
Detector output can feed risk register updates via API
Vendor reviews incomplete
CC-VENDOR-01 evidence schema tracks third-party assessments
ITAR boundaries not enforced
residency_tag = "Restricted" enforces CUI boundary at collection layer
AI governance siloed
CC-AI-* controls follow same architecture as core controls
Real-Time Compliance Dashboard (Planned)
Detector output feeds a live dashboard showing:
Metric
Description
Example
Overall Posture
% controls PASS/FAIL by framework
"NIST 800-171: 92% PASS, 8% FAIL"
ITAR Boundary Status
Restricted-zone controls green/red
"CC-SEG-01: ✅ PASS (no cross-zone routing)"
Evidence Freshness
Last collection timestamp per control
"EV-LOG-01: collected 2 hours ago (hourly SLA)"
Risk Exposure
High-risk controls with FAIL status highlighted
"RISK-AI-01: CC-AI-02 FAIL → escalation triggered"
Tech Stack Options
Option
Cost
Setup Time
Best For
Grafana + Prometheus
~$50/month (self-hosted)
1-2 weeks
Startups, cost-conscious teams
AWS QuickSight
~$200/month (managed)
3-5 days
AWS-native environments
ServiceNow Performance Analytics
Included in GRC license
1-2 weeks
Enterprise ServiceNow customers
Sample Query (Grafana/Prometheus)
promql
12
# Show % of ITAR controls PASS in last 24 hourssum(residency_tag="Restricted" and status="PASS") / sum(residency_tag="Restricted") * 100

Interview Talking Point
"Compliance isn't point-in-time — it's continuous. My detector output can feed a real-time dashboard showing ITAR boundary status, evidence freshness, and risk exposure. For AnySignal, I'd deploy Grafana in Week 1 so leadership always knows our compliance posture — no waiting for quarterly audit reports."
Extensibility
To Add a New Detector
Create detectors/check_<control>.py following the standard output schema
Add CIS Benchmark mappings to docstring
Add control_owner and escalation_path fields
Add to run_all_detectors.py detector list
Update this README
To Add a New Provider
Create provider-specific evidence file in evidence-dictionary/
Implement detector using provider's API/CLI (e.g., az for Azure, gcloud for GCP)
Add Terraform module in terraform/ if applicable
Update multi-cloud evidence table in main README
Example: Azure MFA Detector
python
1234567891011
# detectors/check_mfa_azure.pyimport subprocessimport jsondef check_azure_mfa():    result = subprocess.run(        ["az", "ad", "user", "list", "--query", "[].{user:userPrincipalName,mfa:signInActivity}"],        capture_output=True,        text=True    )    # Parse and return standardized JSON output

Integration with Risk Register
Detector output integrates with the unified risk register (../risk-register.md):
Risk ID
Linked Controls
Detector Output → Risk Update
RISK-ITAR-01
CC-SEG-01, CC-EXPORT-01, CC-PERSONNEL-01
FAIL → Risk exposure score increases → Legal notified
RISK-AI-01
CC-AI-01, CC-AI-02, CC-AI-03
FAIL → Model deployment blocked → AI Ethics Board notified
RISK-CLOUD-01
CC-ENC-01, CC-LOG-01, CC-BACKUP-01
FAIL → Cloud security posture degraded → CISO notified
Automated Risk Update Flow
1
Detector FAIL → Webhook → ServiceNow GRC → Risk Register Updated → Escalation Triggered

Author
Victor Adeleke
FedRAMP Certification Manager | Cloud Compliance Engineer | HSM & PKI Governance
Portfolio: grcsecuritycontrols.com
GitHub: github.com/vibosphere360/grc-control-systems-lab
LinkedIn: linkedin.com/in/victor-adeleke-214083177
Email: victorsreops@gmail.com
