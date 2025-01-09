FROM apache/nifi:latest

COPY scripts/ /opt/nifi/scripts/

RUN chmod +x /opt/nifi/scripts/deploy_nifi_flow.sh

ENTRYPOINT ["/bin/bash", "/opt/nifi/scripts/deploy_nifi_flow.sh"]
