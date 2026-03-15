#!/usr/bin/env python3
import re

files = ["check_cloudtrail.py", "check_mfa.py", "check_k8s_rbac.py"]

for filename in files:
    with open(filename, "r") as f:
        content = f.read()
    
    # Replace print statements that output file paths with stderr versions
    content = re.sub(
        r'print\(f"\\nEvidence saved to: \{output_file\}"\)',
        'print(f"\\nEvidence saved to: {output_file}", file=sys.stderr)',
        content
    )
    content = re.sub(
        r'print\(f"Checksum: \{result\.get\(\'checksum_sha256\', \'N/A\'\)\}"\)',
        'print(f"Checksum: {result.get(\'checksum_sha256\', \'N/A\')}", file=sys.stderr)',
        content
    )
    
    # Add import sys if not present
    if "import sys" not in content:
        content = content.replace("import json", "import json\nimport sys")
    
    with open(filename, "w") as f:
        f.write(content)
    
    print(f"Fixed {filename}")

print("All files fixed!")
