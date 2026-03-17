# GRC Control Systems Lab

> Open-source GRC platform prototype: Canonical controls, crosswalks, and automated evidence for aerospace, defense, and commercial cloud environments.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Phase 4 Complete](https://img.shields.io/badge/Status-Phase%204%20Complete-blue)]()
[![Frameworks](https://img.shields.io/badge/Frameworks-NIST%7CSOC2%7CISO%7CCMMC%7CAI%20RMF-green)]()

This repository demonstrates how modern compliance platforms (Vanta, Drata, Secureframe) implement continuous compliance and multi-framework governance. It is designed to be cloud-provider agnostic, enabling consistent control validation across AWS, Azure, GCP, Kubernetes, and SaaS environments.

**Philosophy:** Compliance isn't point-in-time audit preparation — it's continuous operational governance. Controls should emerge from system architecture, not be retrofitted later.

---

## The Lab Includes

| Module | Status | Description |
| :--- | :--- | :--- |
| **Canonical Control Library** | ✅ Complete | 21 canonical controls (core + ITAR + AI governance) |
| **Framework Crosswalk Engine** | ✅ Complete | Maps to NIST 800-53/171, CMMC L2, SOC 2, ISO 27001/42001, NIST AI RMF |
| **Evidence Data Dictionary** | ✅ Complete | Structured schema for evidence collection + automation flags + multi-cloud providers |
| **Continuous Monitoring Detectors** | ✅ Complete | Python detectors + Terraform for AWS/Azure/K8s control validation |
| **Evidence Automation Framework** | ✅ Complete | Audit-ready evidence collection with governance metadata (ownership, escalation, residency) |
| **AI-Assisted Compliance Guidance** | 🟡 Planned | Prompt libraries grounded in canonical controls |
| **Trust Center Architecture** | 🟡 Planned | Customer-facing artifacts + audit package generation |
| **FedRAMP 20x Alignment** | 🔜 Phase 5 | OSCAL export + KSI-AFR mappings for pilot authorization |

---

## Expected Business Outcomes

| Metric | Target Impact | How We Measure |
|--------|--------------|----------------|
| **Audit prep time** | 40% reduction | Hours spent gathering evidence pre/post automation |
| **Recurring findings** | 35% reduction | POA&M closure rate, repeat audit issues |
| **Contract velocity** | Faster security reviews | Time from customer request to evidence package |
| **Engineering friction** | Zero compliance gates | PR merge time, deployment frequency |
| **Cost efficiency** | ~$40/month vs. $16K/month | AWS costs vs. enterprise GRC licensing |

---

## Proposed Compliance Operating Model

| Function | Owner | Cadence | Output |
|----------|-------|---------|--------|
| **Control Testing** | SecOps + Engineering | Automated (hourly/daily) | PASS/FAIL + evidence JSON |
| **Risk Review** | CISO + Legal | Monthly | Updated risk register |
| **Audit Prep** | Compliance Lead | Quarterly | Pre-packaged evidence bundle |
| **Training** | Compliance + HR | Annual + onboarding | Completion records + attestations |
| **ITAR Enforcement** | Security Architect + Legal | Continuous + on-change | Access logs + escalation alerts |

---

## Core Compliance Frameworks

### Federal
- NIST 800-53 Rev 5
- NIST 800-171 Rev 2
- CMMC 2.0 Level 2
- FedRAMP (Moderate/High)

### Commercial
- SOC 2 Type II
- ISO/IEC 27001:2022

### AI Governance
- ISO/IEC 42001:2023
- NIST AI RMF (GOVERN/MAP/MEASURE/MANAGE)

### Planned
- NIST CSF 2.0
- PCI DSS 4.0
- HIPAA
- GDPR/CCPA

---

## Security Configuration Benchmarks

- **CIS AWS Foundations Benchmark v1.5:** Mapped to 15+ canonical controls (IAM, Logging, Encryption, Network)
- **CIS Kubernetes Benchmark v1.8:** Mapped to 10+ canonical controls (RBAC, Network Policies, etcd encryption)
- **CIS Azure Benchmark v2.0:** Planned for Phase 5
- **CIS GCP Benchmark v3.0:** Planned for Phase 5

---

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

---

## Aerospace and Defense Focus

This library is designed for organizations handling Controlled Unclassified Information (CUI) and export-controlled technical data:

- **NIST 800-171:** CUI protection requirements for DoD contractors
- **ITAR/EAR:** Export control patterns for technical data segregation
- **CMMC 2.0 Level 2:** Cybersecurity maturity for Defense Industrial Base
- **Data Residency Tagging:** Controls tagged `Global`/`US`/`Restricted` for boundary enforcement

### ITAR Compliance Architecture
ITAR-Controlled Data
↓
Restricted Zone (us-east-1 FedRAMP region)
↓
VPC Isolation + IAM Attribute Checks + Audit Logging
↓
Evidence tagged residency_tag="Restricted" → stored in CUI-approved storage only
↓
Escalation path: Security Architect → Legal → CISO → Board


---

## AI Governance Extension

- **NIST AI RMF (2023):** Mapped via GOVERN, MAP, MEASURE, MANAGE functions
- **ISO/IEC 42001:2023:** AI Management System controls aligned with ISO 27001 structure
- **Data Residency for AI:** Training vs. inference boundary tagging for cross-border deployment

### AI Controls Included

| Control | Focus | Evidence Source |
|---------|-------|----------------|
| `CC-AI-01` | Training Data Lineage | Data catalog API + bias metrics |
| `CC-AI-02` | Model Risk Assessment | Red team results + risk workshop output |
| `CC-AI-03` | Human Oversight & Appeal | Appeal event logs + override actions |
| `CC-AI-04` | Model Transparency | Model card documentation + stakeholder access logs |

---

## Architecture Overview
External Frameworks (FedRAMP, NIST, ITAR, CMMC)
↓
Crosswalk Engine (framework_crosswalk.csv)
↓
Canonical Control Layer (21 controls, one definition)
↓
┌─────────────────┬─────────────────┬─────────────────┐
│ Evidence Layer │ Monitoring Layer│ Risk Layer │
│ (evidence-dict) │ (detectors/) │ (risk-register) │
└────────┬────────┴────────┬────────┴────────┬────────┘
│ │ │
└───────┬─────────┴────────┬────────┘
▼ ▼
Compliance Output Engineering Systems
(checksummed JSON) (AWS, K8s, RF, Satellite)

Getting Started
Prerequisites
Python 3.8+
AWS CLI configured (for real mode; mock mode works without credentials)
kubectl configured (for Kubernetes detectors)
Terraform 1.0+ (for IaC deployment)
Run Detectors (Mock Mode)
bash
123
Validate Terraform (No Apply)
bash
1234
Explore the Evidence Schema
bash
12
Contributing
This is an open-source reference architecture. Contributions welcome:
Fork the repo
Create a feature branch (git checkout -b feature/amazing-control)
Add your control mapping or detector
Submit a pull request
Guidelines:
Keep controls canonical (one definition, multiple framework mappings)
Include residency_tag, control_owner, escalation_path in evidence schema
Detectors should output standardized JSON with checksums
Author
Victor Adeleke
FedRAMP Certification Manager | Cloud Compliance Engineer | HSM & PKI Governance
Portfolio: grcsecuritycontrols.com
GitHub: github.com/vibosphere360/grc-control-systems-lab
LinkedIn: linkedin.com/in/victor-adeleke-214083177
Email: victorsreops@gmail.com
Note: This is a portfolio project demonstrating system design capabilities for regulated environments. It is not affiliated with any regulatory body, certification organization, or government agency. Specific implementations for organizations would be customized under NDA.
