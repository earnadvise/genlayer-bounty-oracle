"""
AutonomousBountyOracle Interaction Script
Demonstrates programmatic interaction with the AutonomousBountyOracle Intelligent Contract.
"""

def main():
    print("==================================================")
    print("🚀 GenLayer AutonomousBountyOracle Interaction")
    print("==================================================")
    print("Supported Methods:")
    print("  - create_bounty_pool(project_name, codebase_url, scope_desc, ...)")
    print("  - top_up_pool(pool_id) [payable]")
    print("  - submit_vulnerability(pool_id, title, poc_url, claimed_severity) [payable stake]")
    print("  - triage_and_settle(report_id) -> Consensus AI Triage (gl.eq_principle.strict_eq)")
    print("  - get_pool(pool_id) -> BountyPool")
    print("  - get_report(report_id) -> VulnerabilityReport")
    print("==================================================")

if __name__ == "__main__":
    main()
