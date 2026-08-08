import ollama
import json


MODEL = "llama3.2:latest"


# ==========================================================
# OLLAMA HELPER
# ==========================================================

def ask_ollama(prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()


# ==========================================================
# AGENT 1: LEAD GENERATION
# ==========================================================

def lead_generation_agent(industry):

    print("\n[AGENT 1] Lead Generation Agent")
    print("-" * 50)

    prompt = f"""
You are a Lead Generation Agent.

Find 5 example business leads in the following industry:

Industry: {industry}

Create realistic DEMO leads for a student project.

Do not use real personal email addresses.

Return exactly 5 leads in this format:

1. Company:
   Industry:
   Company Size:
   Location:
   Website:

2. Company:
   Industry:
   Company Size:
   Location:
   Website:

Continue until there are 5 leads.
"""

    result = ask_ollama(prompt)

    print(result)

    return result


# ==========================================================
# AGENT 2: LEAD QUALIFICATION
# ==========================================================

def lead_qualification_agent(leads):

    print("\n[AGENT 2] Lead Qualification Agent")
    print("-" * 50)

    prompt = f"""
You are a Lead Qualification Agent.

Analyze the following leads:

{leads}

Score each lead from 1 to 10 based on:

- Industry relevance
- Company size
- Potential business need
- Likelihood of being interested

Classify each lead as:

HOT
WARM
COLD

Return:

Company:
Score:
Category:
Reason:
"""

    result = ask_ollama(prompt)

    print(result)

    return result


# ==========================================================
# AGENT 3: EMAIL GENERATION
# ==========================================================

def email_generation_agent(qualified_leads):

    print("\n[AGENT 3] Email Generation Agent")
    print("-" * 50)

    prompt = f"""
You are an SDR Email Generation Agent.

Using the qualified leads below:

{qualified_leads}

Create a short professional outreach email
for the HOT leads.

Rules:

- Do not invent personal information.
- Do not use fake personal email addresses.
- Keep the email under 120 words.
- Make the email professional.
- Include a clear subject.
- Include a simple call to action.

Format:

Company:
Subject:
Email:
"""

    result = ask_ollama(prompt)

    print(result)

    return result


# ==========================================================
# MAIN MULTI-AGENT SYSTEM
# ==========================================================

def main():

    print("=" * 60)
    print("MULTI-AGENT SDR SYSTEM")
    print("=" * 60)

    industry = input("\nEnter target industry: ")

    # ------------------------------------------------------
    # AGENT 1
    # ------------------------------------------------------

    leads = lead_generation_agent(industry)

    # ------------------------------------------------------
    # AGENT 2
    # ------------------------------------------------------

    qualified_leads = lead_qualification_agent(leads)

    # ------------------------------------------------------
    # AGENT 3
    # ------------------------------------------------------

    emails = email_generation_agent(qualified_leads)

    # ------------------------------------------------------
    # FINAL OUTPUT
    # ------------------------------------------------------

    print("\n" + "=" * 60)
    print("FINAL EMAIL DRAFTS")
    print("=" * 60)

    print(emails)

    print("\n" + "=" * 60)
    print("MULTI-AGENT SDR SYSTEM COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
