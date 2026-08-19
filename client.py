class InstantAgentSandboxContainerProvisionerClient:
    def provision_agent_sandbox(self, agent_runtime_config: dict, target_region: str = "us-east-1") -> dict:
        return {
            "endpoint_url": "https://sandbox-agent-9921.genpark.ai",
            "provisioning_duration_seconds": 18,
            "sandbox_status": "READY_FOR_AUTONOMOUS_INVOCATION"
        }
