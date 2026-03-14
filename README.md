# 🛡️ GRC Control Systems Lab

> **Open-source GRC platform prototype: Canonical controls, crosswalks, and automated evidence for aerospace, defense, and commercial cloud environments.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Phase 2 Complete](https://img.shields.io/badge/Status-Phase%202%20Complete-blue)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-NIST%7CSOC2%7CISO%7CCMMC%7CAI%20RMF-green)]()

This repository demonstrates how modern compliance platforms (Vanta, Drata, Secureframe) implement continuous compliance and multi-framework governance.

## 📦 The Lab Includes

| Module | Status | Description |
| :--- | :--- | :--- |
| **Canonical Control Library** | ✅ Complete | 21 canonical controls (core + ITAR + AI governance) |
| **Framework Crosswalk Engine** | ✅ Complete | Maps to NIST 800-53/171, CMMC L2, SOC 2, ISO 27001/42001, NIST AI RMF |
| **Evidence Data Dictionary** | 🟡 In Progress | Structured schema for evidence collection + automation flags |
| **Continuous Monitoring Detectors** | ⚪ Planned | Terraform + OPA detectors for AWS control validation |
| **AI-Assisted Compliance Guidance** | ⚪ Planned | Prompt libraries grounded in canonical controls |
| **Trust Center Architecture** | ⚪ Planned | Customer-facing artifacts + audit package generation |

## 🗺️ Frameworks Covered

### Core Compliance
- **Federal:** NIST 800-53 Rev 5, NIST 800-171 Rev 2, CMMC 2.0 Level 2, FedRAMP
- **Commercial:** SOC 2 Type II, ISO/IEC 27001:2022
- **AI Governance:** ISO/IEC 42001:2023, NIST AI RMF (GOVERN/MAP/MEASURE/MANAGE)
- **Planned:** NIST CSF, PCI DSS 4.0, HIPAA, GDPR/CCPA

## 🎯 Aerospace & Defense Focus

This library is designed for organizations handling Controlled Unclassified Information (CUI) and export-controlled technical data:

- **NIST 800-171:** CUI protection requirements for DoD contractors
- **ITAR/EAR:** Export control patterns for technical data segregation
- **CMMC 2.0 Level 2:** Cybersecurity maturity for Defense Industrial Base
- **Data Residency Tagging:** Controls tagged `Global`/`US`/`Restricted` for boundary enforcement

## 🤖 AI Governance Extension

- **NIST AI RMF (2023):** Mapped via GOVERN, MAP, MEASURE, MANAGE functions
- **ISO/IEC 42001:2023:** AI Management System controls aligned with ISO 27001 structure
- **Data Residency for AI:** Training vs. inference boundary tagging for cross-border deployment

## 🏗️ Architecture

```mermaid
graph TD
    A[Authoritative Sources] -->|Ingest| B(Canonical Control Library)
    B -->|Map| C{Crosswalk Engine}
    C -->|NIST 800-171| D[ITAR/EAR]
    C -->|SOC 2| E[FedRAMP]
    C -->|ISO 27001| F[CMMC L2]
    B -->|Define| G(Evidence Data Dictionary)
    G -->|Validate| H[Continuous Monitoring Detectors]
    H -->|Output| I[Evidence Store]
    I -->|Ground| J[AI Compliance Copilot]
    J -->|Publish| K[Trust Center / Audit Package]    

👤 Author
Victor Adeleke
Security Risk & Compliance Architect | Cloud, AI & Export Control Governance
🌐 grcsecuritycontrols.com
💼 LinkedIn
📧 victorsreops@gmail.com
