#!/bin/bash

NIFI_API="http://localhost:8080/nifi-api"
FLOW_FILE="/opt/nifi/scripts/job_data_pipeline.json"

echo "Waiting for NiFi to start..."
until curl -s "$NIFI_API/flow/status" > /dev/null; do
  sleep 5
done

echo "NiFi started. Deploying flow definition..."

# Deploy the flow definition
curl -X POST -H "Content-Type: application/json" \
  -d @"$FLOW_FILE" \
  "$NIFI_API/process-groups/root/process-groups"

echo "Flow deployed successfully."
