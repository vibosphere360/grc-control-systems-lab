#!/bin/bash

# create_evidence_files.sh
# Creates empty evidence dictionary CSV files for GRC Control Systems Lab
# Run this script from the evidence-dictionary directory

echo "Creating evidence dictionary CSV files..."

# Create evidence_schema.csv with headers only
cat > evidence_schema.csv << 'EOF'
evidence_id,control_id,evidence_name,description,source_type,data_format,collection_method,freshness,owner,automation_possible,retention_period,residency_tag
EOF

# Create evidence_aws.csv with headers
cat > evidence_aws.csv << 'EOF'
evidence_id,control_id,evidence_name,aws_service,aws_resource_type,collection_method,aws_cli_example,terraform_example
EOF

# Create evidence_azure.csv with headers
cat > evidence_azure.csv << 'EOF'
evidence_id,control_id,evidence_name,azure_service,azure_resource_type,collection_method,azure_cli_example
EOF

# Create evidence_gcp.csv with headers
cat > evidence_gcp.csv << 'EOF'
evidence_id,control_id,evidence_name,gcp_service,gcp_resource_type,collection_method,gcloud_example
EOF

# Create evidence_alibaba.csv with headers
cat > evidence_alibaba.csv << 'EOF'
evidence_id,control_id,evidence_name,alibaba_service,alibaba_resource_type,collection_method,aliyun_cli_example
EOF

# Create evidence_kubernetes.csv with headers
cat > evidence_kubernetes.csv << 'EOF'
evidence_id,control_id,evidence_name,k8s_api_group,k8s_resource_type,collection_method,kubectl_example
EOF

# Create evidence_saas.csv with headers
cat > evidence_saas.csv << 'EOF'
evidence_id,control_id,evidence_name,saas_platform,data_source,collection_method,api_example
EOF

echo "✅ All evidence dictionary files created successfully!"
echo ""
echo "Files created:"
ls -la *.csv
echo ""
echo "Next step: Populate each file with the content from our conversation."
