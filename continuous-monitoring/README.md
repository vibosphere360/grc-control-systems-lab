# Continuous Monitoring Detectors

This module contains automated detectors that validate control state against the evidence schema defined in Phase 3. Detectors can be run locally, in CI/CD pipelines, or on a schedule via Lambda/Cloud Functions.

## Quick Start

### Prerequisites
- Python 3.8+
- AWS CLI configured (`aws configure`) for real mode
- kubectl configured (for Kubernetes detectors)
- Terraform 1.0+ (for IaC deployment)

### Run All Detectors (Mock Mode)
```bash
cd detectors/
export MOCK_MODE=true
python3 run_all_detectors.py
