# Continuous Monitoring Detectors

This module contains automated detectors that validate control state against the evidence schema defined in Phase 3. Detectors can be run locally, in CI/CD pipelines, or on a schedule via Lambda/Cloud Functions.

## Architecture
Evidence Schema (Phase 3)
↓
Detector Script (Python/OPA)
↓
Cloud Provider API (AWS/Azure/K8s)
↓
Pass/Fail Result + Evidence Artifact
↓
Evidence Store (S3/Blob Storage)

