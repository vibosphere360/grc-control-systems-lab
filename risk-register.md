# Unified Risk Register (Concept)

This document demonstrates how canonical controls map to business risks — enabling leadership to see compliance as risk reduction, not checkbox completion.

## Risk-to-Control Mapping

| Risk ID | Risk Description | Linked Controls | Business Impact | Likelihood | Residual Risk | Owner |
|---------|-----------------|----------------|----------------|------------|--------------|-------|
| RISK-ITAR-01 | Unauthorized export of controlled technical data | CC-SEG-01, CC-EXPORT-01, CC-PERSONNEL-01 | Criminal penalties, loss of DoD contracts, reputational harm | Medium | Low (with controls) | Legal + Security |
| RISK-AI-01 | AI model bias or data leakage leading to regulatory action | CC-AI-01, CC-AI-02, CC-AI-03 | Fines under EU AI Act, loss of customer trust, model recall | High | Medium | ML Lead + Compliance |
| RISK-CLOUD-01 | Cloud misconfiguration exposing CUI | CC-ENC-01, CC-LOG-01, CC-BACKUP-01 | FedRAMP authorization loss, data breach notification costs | Low | Low | Cloud Security |
| RISK-VENDOR-01 | Third-party vendor compromise impacting supply chain | CC-VENDOR-01, CC-SEG-01 | Contract termination, cascading compliance failures | Medium | Medium | Vendor Risk + Procurement |

## How This Integrates with Evidence Automation

1. **Risk identified** → Linked controls flagged in evidence schema
2. **Detector runs** → PASS/FAIL status updates risk exposure score
3. **Dashboard alert** → High-risk FAIL triggers escalation to owner
4. **Remediation tracked** → POA&M updated in ServiceNow GRC

## Interview Talking Point

> "Controls don't exist in isolation — they mitigate business risks. My unified risk register ties CC-SEG-01 to ITAR violation risk, CC-AI-02 to model bias risk, etc. This lets leadership see compliance as risk reduction, not checkbox completion. For AnySignal, I'd customize this register based on your actual RF systems, export classification, and contract obligations."
