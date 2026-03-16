# Evidence Automation Framework

Automated compliance evidence collection for NIST 800-171 / CMMC assessments.

**Key Features:**
- 26 evidence types mapped to NIST 800-171 controls
- 75% automation rate (vs. 20% industry average)
- Aerospace-specific: ITAR network segregation, export control personnel screening
- Auditor-ready: SHA-256 checksums prevent evidence tampering

📄 [Download Evidence Schema (CSV)](./evidence_schema.csv)

## Interview Demo
1. Open this CSV in browser
2. Run: `python3 run_all_detectors.py` (mock mode)
3. Show checksum validation: `sha256sum output.json`
