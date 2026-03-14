# GRC Control Systems Lab

> Open-source GRC platform prototype: Canonical controls, crosswalks, and automated evidence for aerospace, defense, and commercial cloud environments.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Phase 2 Complete](https://img.shields.io/badge/Status-Phase%202%20Complete-blue)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-NIST%7CSOC2%7CISO%7CCMMC%7CAI%20RMF-green)]()

This repository demonstrates how modern compliance platforms (Vanta, Drata, Secureframe) implement continuous compliance and multi-framework governance.

## The Lab Includes

| Module | Status | Description |
| :--- | :--- | :--- |
| **Canonical Control Library** | Complete | 21 canonical controls (core + ITAR + AI governance) |
| **Framework Crosswalk Engine** | Complete | Maps to NIST 800-53/171, CMMC L2, SOC 2, ISO 27001/42001, NIST AI RMF |
| **Evidence Data Dictionary** | In Progress | Structured schema for evidence collection + automation flags |
| **Continuous Monitoring Detectors** | Planned | Terraform + OPA detectors for AWS control validation |
| **AI-Assisted Compliance Guidance** | Planned | Prompt libraries grounded in canonical controls |
| **Trust Center Architecture** | Planned | Customer-facing artifacts + audit package generation |

## Frameworks Covered

### Core Compliance
- **Federal:** NIST 800-53 Rev 5, NIST 800-171 Rev 2, CMMC 2.0 Level 2, FedRAMP
- **Commercial:** SOC 2 Type II, ISO/IEC 27001:2022
- **AI Governance:** ISO/IEC 42001:2023, NIST AI RMF (GOVERN/MAP/MEASURE/MANAGE)
- **Planned:** NIST CSF, PCI DSS 4.0, HIPAA, GDPR/CCPA

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


The architecture below illustrates how canonical controls enable multi-framework governance, automated evidence collection, and AI-assisted compliance workflows.

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

Author
Victor Adeleke
Security Risk and Compliance Architect | Cloud, AI and Export Control Governance
Portfolio: grcsecuritycontrols.com
LinkedIn: linkedin.com/in/victor-adeleke-214083177
Email: victorsreops@gmail.com

