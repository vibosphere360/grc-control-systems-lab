# GRC Control Systems Lab

> Open-source GRC platform prototype: Canonical controls, crosswalks, and automated evidence for aerospace, defense, and commercial cloud environments.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Phase 3 Complete](https://img.shields.io/badge/Status-Phase%203%20Complete-blue)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-NIST%7CSOC2%7CISO%7CCMMC%7CAI%20RMF-green)]()

This repository demonstrates how modern compliance platforms (Vanta, Drata, Secureframe) implement continuous compliance and multi-framework governance. It is designed to be cloud-provider agnostic, enabling consistent control validation across AWS, Azure, GCP, Kubernetes, and SaaS environments.

## The Lab Includes

| Module | Status | Description |
| :--- | :--- | :--- |
| **Canonical Control Library** | Complete | 21 canonical controls (core + ITAR + AI governance) |
| **Framework Crosswalk Engine** | Complete | Maps to NIST 800-53/171, CMMC L2, SOC 2, ISO 27001/42001, NIST AI RMF |
| **Evidence Data Dictionary** | Complete | Structured schema for evidence collection + automation flags + multi-cloud providers |
| **Continuous Monitoring Detectors** | Planned | Terraform + OPA detectors for AWS/Azure/K8s control validation |
| **AI-Assisted Compliance Guidance** | Planned | Prompt libraries grounded in canonical controls |
| **Trust Center Architecture** | Planned | Customer-facing artifacts + audit package generation |

## Frameworks Covered

### Core Compliance
- **Federal:** NIST 800-53 Rev 5, NIST 800-171 Rev 2, CMMC 2.0 Level 2, FedRAMP
- **Commercial:** SOC 2 Type II, ISO/IEC 27001:2022
- **AI Governance:** ISO/IEC 42001:2023, NIST AI RMF (GOVERN/MAP/MEASURE/MANAGE)
- **Planned:** NIST CSF, PCI DSS 4.0, HIPAA, GDPR/CCPA

## Multi-Cloud Evidence Strategy

This library separates **control objectives** (universal) from **evidence sources** (provider-specific). This enables consistent governance across hybrid environments.

### Provider-Specific Evidence Sources
| Control | AWS | Azure | GCP | Kubernetes | SaaS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logging** | CloudTrail + S3 | Activity Log + Monitor | Cloud Audit Logs | API Server Audit | Okta/Salesforce Logs |
| **Encryption** | KMS + Config | Key Vault + Policy | Cloud KMS | etcd + KMS Provider | Vendor Attestation |
| **Network** | VPC Flow Logs | NSG Flow Logs | VPC Flow Logs | Network Policies | WAF Logs |
| **IAM** | IAM API + Access Analyzer | Entra ID + PIM | IAM API | RBAC + ServiceAccounts | SSO Provisioning |

### Evidence Dictionary Files
| File | Provider | Controls Mapped | Example Evidence |
| :--- | :--- | :--- | :--- |
| `evidence_schema.csv` | Provider-agnostic | 21 controls | IAM inventory, log integrity, encryption config |
| `evidence_aws.csv` | AWS | 21 controls | CloudTrail, KMS, VPC Flow Logs, Inspector |
| `evidence_azure.csv` | Azure | 21 controls | Entra ID, Key Vault, NSG Flow Logs, Defender |
| `evidence_kubernetes.csv` | Kubernetes | 21 controls | RBAC, Network Policies, etcd encryption |
| `evidence_saas.csv` | SaaS | 5 controls | Okta, GitHub, SecurityScorecard, KnowBe4 |
| `collection-methodology.md` | N/A | N/A | Automation tiers, residency tags, freshness standards |

## Aerospace and Defense Focus

This library is designed for organizations handling Controlled Unclassified Information (CUI) and export-controlled technical data:

- **NIST 800-171:** CUI protection requirements for DoD contractors
- **ITAR/EAR:** Export control patterns for technical data segregation
- **CMMC 2.0 Level 2:** Cybersecurity maturity for Defense Industrial Base
- **Data Residency Tagging:** Controls tagged Global/US/Restricted for boundary enforcement

## AI Governance Extension

- **NIST AI RMF (2023):** Mapped via GOVERN, MAP, MEASURE, MANAGE functions
- **ISO/IEC 42001:2023:** AI Management System controls aligned with ISO 27001 structure
- **Data Residency for AI:** Training vs. inference boundary tagging for cross-border deployment

## Architecture

```mermaid
flowchart TD
    A[Compliance Framework Sources] --> B[Canonical Control Library]
    B --> C[Framework Crosswalk Engine]
    C --> D[NIST 800-53]
    C --> E[NIST 800-171]
    C --> F[SOC2]
    C --> G[ISO 27001]
    C --> H[CMMC Level 2]
    C --> I[AI Governance Frameworks]
    B --> J[Evidence Data Dictionary]
    J --> K[Continuous Monitoring Detectors]
    K --> L[Evidence Store]
    L --> M[AI Compliance Copilot]
    M --> N[Trust Center and Audit Artifacts]
