#!/usr/bin/env python3
"""
Orchestrator: Run all compliance detectors and aggregate results
Addresses Titilayo's finding: Controls must be ongoing operational processes
"""

import subprocess
import json
from datetime import datetime
from pathlib import Path

def run_all_detectors():
    """Execute all detector scripts and aggregate results"""
    detectors = [
        "check_cloudtrail.py",
        "check_mfa.py",
        "check_k8s_rbac.py"
    ]
    
    results = []
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    print(f"Starting compliance check at {timestamp}")
    print("=" * 60)
    
    for detector in detectors:
        print(f"\nRunning {detector}...")
        try:
            result = subprocess.run(
                ["python3", detector],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                output = json.loads(result.stdout)
                results.append(output)
                print(f"  ✓ {output['control_id']}: {output['status']}")
                print(f"    CIS: {', '.join(output.get('cis_benchmarks', []))}")
            else:
                print(f"  ✗ {detector} failed: {result.stderr}")
                
        except Exception as e:
            print(f"  ✗ {detector} exception: {str(e)}")
    
    # Aggregate summary
    summary = {
        "timestamp": timestamp,
        "total_detectors": len(detectors),
        "passed": sum(1 for r in results if r.get("status") == "PASS"),
        "failed": sum(1 for r in results if r.get("status") == "FAIL"),
        "results": results
    }
    
    # Save summary
    output_dir = Path("../outputs/")
    output_dir.mkdir(exist_ok=True)
    summary_file = output_dir / f"compliance-summary-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.json"
    
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)
    
    print("\n" + "=" * 60)
    print(f"Summary: {summary['passed']} passed, {summary['failed']} failed")
    print(f"Results saved to: {summary_file}")
    
    return summary

if __name__ == "__main__":
    run_all_detectors()
