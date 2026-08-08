import ollama


# ==========================================================
# POLICY COMPLIANCE AGENT
# ==========================================================

MODEL = "llama3.2:latest"


# ==========================================================
# SYNTHETIC DATA
# ==========================================================

employees = [
    {
        "name": "Employee A",
        "department": "IT",
        "password_length": 12,
        "mfa_enabled": True,
        "training_completed": True,
        "data_shared_externally": False
    },
    {
        "name": "Employee B",
        "department": "Finance",
        "password_length": 7,
        "mfa_enabled": False,
        "training_completed": True,
        "data_shared_externally": True
    },
    {
        "name": "Employee C",
        "department": "HR",
        "password_length": 10,
        "mfa_enabled": True,
        "training_completed": False,
        "data_shared_externally": False
    },
    {
        "name": "Employee D",
        "department": "Marketing",
        "password_length": 14,
        "mfa_enabled": True,
        "training_completed": True,
        "data_shared_externally": False
    }
]


# ==========================================================
# POLICY RULES
# ==========================================================

def check_policy(employee):

    violations = []

    # Rule 1: Password must be at least 8 characters
    if employee["password_length"] < 8:
        violations.append(
            "Password length is less than 8 characters"
        )

    # Rule 2: MFA must be enabled
    if not employee["mfa_enabled"]:
        violations.append(
            "Multi-factor authentication is not enabled"
        )

    # Rule 3: Security training must be completed
    if not employee["training_completed"]:
        violations.append(
            "Security awareness training is incomplete"
        )

    # Rule 4: External data sharing is not allowed
    if employee["data_shared_externally"]:
        violations.append(
            "Data was shared externally"
        )

    return violations


# ==========================================================
# AI AGENT
# ==========================================================

def generate_report(employee, violations):

    if violations:
        status = "NON-COMPLIANT"
    else:
        status = "COMPLIANT"

    prompt = f"""
You are a Policy Compliance Agent.

Employee:
{employee["name"]}

Department:
{employee["department"]}

Compliance status:
{status}

Violations:
{violations}

Create a short compliance report.

Include:

1. Employee
2. Status
3. Violations
4. Recommended action

Keep the report concise.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# ==========================================================
# MAIN PROGRAM
# ==========================================================

def main():

    print("=" * 60)
    print("POLICY COMPLIANCE AGENT")
    print("=" * 60)

    print("\nChecking synthetic employee data...")

    for employee in employees:

        print("\n" + "-" * 60)

        print("Employee:", employee["name"])

        # Rule-based evaluation
        violations = check_policy(employee)

        # Determine status
        if violations:
            status = "NON-COMPLIANT"
        else:
            status = "COMPLIANT"

        print("Status:", status)

        if violations:

            print("\nViolations:")

            for violation in violations:
                print("-", violation)

        else:

            print("No policy violations found.")

        # AI-generated report
        print("\nAI COMPLIANCE REPORT:")

        report = generate_report(
            employee,
            violations
        )

        print(report)

    print("\n" + "=" * 60)
    print("POLICY COMPLIANCE CHECK COMPLETED")
    print("=" * 60)


# ==========================================================
# START PROGRAM
# ==========================================================

if __name__ == "__main__":
    main()
