from client import InstantAgentSandboxContainerProvisionerClient

def main():
    client = InstantAgentSandboxContainerProvisionerClient()
    cfg = {"agent_image": "node22-puppeteer-runner", "memory_mb": 1024}
    res = client.provision_agent_sandbox(cfg)
    print(f"Status: {res['sandbox_status']}")
    print(f"Provisioned in: {res['provisioning_duration_seconds']}s")
    print(f"Endpoint: {res['endpoint_url']}")

if __name__ == "__main__":
    main()
