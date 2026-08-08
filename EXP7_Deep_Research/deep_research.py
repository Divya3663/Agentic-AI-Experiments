import ollama


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
# STEP 1: PLANNING AGENT
# ==========================================================

def planning_agent(topic):

    print("\n[STEP 1] PLANNING")
    print("-" * 60)

    prompt = f"""
You are a research planning agent.

Create a detailed research plan for the topic:

{topic}

The plan must contain:

1. Introduction
2. Main concepts
3. Important facts
4. Advantages
5. Challenges
6. Real-world applications
7. Future scope
8. Conclusion

Create a clear list of research points that should
be covered in the final content.
"""

    plan = ask_ollama(prompt)

    print(plan)

    return plan


# ==========================================================
# STEP 2: CONTENT GENERATION
# ==========================================================

def content_generation_agent(topic, plan):

    print("\n[STEP 2] CONTENT GENERATION")
    print("-" * 60)

    prompt = f"""
You are a content research agent.

Topic:
{topic}

Research plan:
{plan}

Using the research plan, write a detailed and
well-structured article.

Requirements:

- Use clear headings.
- Explain concepts simply.
- Cover all points from the plan.
- Avoid unnecessary repetition.
- Write approximately 500 words.
- Do not invent specific statistics.
"""

    draft = ask_ollama(prompt)

    print("\nDRAFT CONTENT:")
    print(draft)

    return draft


# ==========================================================
# STEP 3: REFLECTION AGENT
# ==========================================================

def reflection_agent(topic, draft):

    print("\n[STEP 3] REFLECTION")
    print("-" * 60)

    prompt = f"""
You are a reflection and quality-checking agent.

Topic:
{topic}

Draft content:
{draft}

Review the draft carefully.

Check:

1. Is the content relevant to the topic?
2. Is the structure clear?
3. Are important points missing?
4. Is there unnecessary repetition?
5. Is the explanation easy to understand?
6. Are there unsupported or overly specific claims?
7. What should be improved?

Give a list of specific improvements.
"""

    reflection = ask_ollama(prompt)

    print(reflection)

    return reflection


# ==========================================================
# STEP 4: FINAL REVISION
# ==========================================================

def revision_agent(topic, draft, reflection):

    print("\n[STEP 4] FINAL REVISION")
    print("-" * 60)

    prompt = f"""
You are a final content editor.

Topic:
{topic}

Original draft:
{draft}

Reflection and suggested improvements:
{reflection}

Rewrite the article using the reflection.

Requirements:

- Keep the content relevant.
- Improve clarity and structure.
- Remove unnecessary repetition.
- Include important missing points.
- Keep the language simple and professional.
- Do not invent statistics or fake references.
- Produce the final improved article.
"""

    final_content = ask_ollama(prompt)

    return final_content


# ==========================================================
# MAIN PROGRAM
# ==========================================================

def main():

    print("=" * 60)
    print("DEEP RESEARCH AGENT WORKFLOW")
    print("=" * 60)

    topic = input("\nEnter research topic: ")

    # ------------------------------------------------------
    # STEP 1: PLAN
    # ------------------------------------------------------

    plan = planning_agent(topic)

    # ------------------------------------------------------
    # STEP 2: GENERATE
    # ------------------------------------------------------

    draft = content_generation_agent(topic, plan)

    # ------------------------------------------------------
    # STEP 3: REFLECT
    # ------------------------------------------------------

    reflection = reflection_agent(topic, draft)

    # ------------------------------------------------------
    # STEP 4: REVISE
    # ------------------------------------------------------

    final_content = revision_agent(
        topic,
        draft,
        reflection
    )

    # ------------------------------------------------------
    # FINAL RESULT
    # ------------------------------------------------------

    print("\n" + "=" * 60)
    print("FINAL RESEARCH CONTENT")
    print("=" * 60)

    print(final_content)

    print("\n" + "=" * 60)
    print("DEEP RESEARCH WORKFLOW COMPLETED")
    print("=" * 60)


# ==========================================================
# START
# ==========================================================

if __name__ == "__main__":
    main()
