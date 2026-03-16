# ITAR Segregation Architecture

## Overview
Zone-based compliance model for defense contractors handling Controlled Unclassified Information (CUI) and export-controlled technical data.

## Controls Implemented
| Control ID | Control Name | NIST 800-171 | CIS AWS | Evidence |
|-----------|-------------|-------------|---------|----------|
| CC-EXPORT-01 | Technology Control Plan | 3.1.1; 3.13.11 | 1.1; 2.3.1 | EV-EXPORT-01 |
| CC-EXPORT-02 | Deemed Export Prevention | 3.1.5; 3.9.1 | 1.1; 1.5 | EV-EXPORT-02 |
| CC-SEG-01 | ITAR/Non-ITAR Data Segregation | 3.13.11 | 2.3.1; 2.3.2 | EV-SEG-01 |
| CC-PERSONNEL-01 | Export Control Personnel Screening | 3.9.1 | 1.9 | EV-PERSONNEL-01 |
| CC-RECORD-01 | Export Compliance Recordkeeping | 3.3.2; 3.3.3 | 2.1; 2.2 | EV-RECORD-01 |

## Architecture
```mermaid
graph TD
    A[ITAR-Controlled Data] --> B[Restricted Zone: us-east-1]
    C[Non-ITAR Data] --> D[Global Zone: any region]
    B --> E[VPC Isolation + IAM Attribute Checks]
    D --> F[Standard Security Controls]
    E --> G[Audit Log: CloudTrail + Checksum]
    F --> H[Audit Log: CloudTrail]EOF
