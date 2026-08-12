import ollama

MODEL = "llama3.2:latest"

print("=" * 60)
print("REASONING MODEL BENCHMARKING")
print("=" * 60)

problem = input("\nEnter a reasoning problem: ")


# --------------------------------------------------
# 1. DIRECT PROMPT
# --------------------------------------------------

print("\nGenerating Direct Prompt response...")

direct = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": problem
        }
    ]
)

direct_answer = direct["message"]["content"]

print("\n" + "=" * 60)
print("1. DIRECT PROMPT")
print("=" * 60)
print(direct_answer)


# --------------------------------------------------
# 2. STEP-BY-STEP PROMPT
# --------------------------------------------------

print("\nGenerating Step-by-Step response...")

step_by_step = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": f"""
Solve the following problem carefully.

Explain the reasoning step by step and then give the final answer.

Problem:
{problem}
"""
        }
    ]
)

step_answer = step_by_step["message"]["content"]

print("\n" + "=" * 60)
print("2. STEP-BY-STEP PROMPT")
print("=" * 60)
print(step_answer)


# --------------------------------------------------
# 3. STRUCTURED PROMPT
# --------------------------------------------------

print("\nGenerating Structured response...")

structured = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": f"""
Solve the following problem.

Use this format:

1. Understanding
2. Key Information
3. Solution
4. Final Answer

Problem:
{problem}
"""
        }
    ]
)

structured_answer = structured["message"]["content"]

print("\n" + "=" * 60)
print("3. STRUCTURED PROMPT")
print("=" * 60)
print(structured_answer)


# --------------------------------------------------
# FINAL COMPARISON
# --------------------------------------------------

print("\n" + "=" * 60)
print("BENCHMARK COMPLETED")
print("=" * 60)

print("""
The three prompting strategies were:

1. Direct Prompting
2. Step-by-Step Prompting
3. Structured Prompting

Compare the responses based on:

- Correctness
- Clarity
- Detail
- Reasoning quality
""")
