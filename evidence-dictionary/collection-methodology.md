# Evidence Collection Methods

## Automation Tiers

### Automated (automation_possible = yes)
- **API Export**: Lambda/Python script querying cloud provider APIs (AWS IAM, Config, KMS)
- **Config Rule**: Native cloud provider rule evaluating resource state (AWS Config, Azure Policy)
- **Event-Driven**: S3/CloudWatch event triggering evidence collection pipeline
- **Policy-as-Code**: OPA/Rego evaluating infrastructure state pre-deploy

### Partial (automation_possible = partial)
- **Hybrid Workflow**: Automated data collection + manual review/approval step
- **Scheduled Report**: Tool-generated report requiring human validation before submission
- **Sampling**: Automated query of subset + manual extrapolation for full population

### Manual (automation_possible = no)
- **Document Upload**: Policy approvals, training records, TCP signatures, audit reports
- **Attestation**: Manager sign-off, access review certifications, risk acceptance forms
- **Physical Evidence**: Badge logs, facility audit photos, SCIF inspection records

## Data Residency Tags

| Tag | Definition | Example Use |
|-----|-----------|-------------|
| `Global` | Evidence can be collected/stored in any approved region | SOC 2 logs, public-facing system configs |
| `US` | Evidence must remain in US-approved environments (FedRAMP, ITAR) | CloudTrail logs for CUI systems |
| `Restricted` | Evidence contains CUI/controlled data; requires encrypted storage + access logging + audit trail | KMS policies, vulnerability scans of classified systems, export control records |

## Freshness Guidelines

| Frequency | Use Case | Example |
|-----------|----------|---------|
| `hourly` | High-risk, rapidly changing controls | CloudTrail log integrity, MFA status |
| `daily` | Standard operational controls | IAM inventory, encryption configs, backup logs |
| `weekly` | Lower-frequency validation | Vulnerability scans, asset inventory exports |
| `monthly` | Governance/oversight controls | Appeal workflow logs, risk register updates |
| `quarterly` | Strategic risk reporting | Risk register exports, policy reviews |
| `annual` | Policy/training/attestation controls | TCP approvals, personnel screening, policy sign-offs |
| `per-model` / `per-release` | AI/ML-specific controls | Training data lineage, model cards, risk assessments |
