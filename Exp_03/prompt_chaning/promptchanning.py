import ollama

print("=" * 50)
print("PROMPT CHAINING FOR SUMMARIZATION")
print("=" * 50)

# Get topic from user
topic = input("\nEnter a topic: ")


# ==========================================
# STEP 1: GENERATE SUMMARY
# ==========================================

print("\nGenerating summary...")

summary = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": f"""
Write a short and simple summary about {topic}
in around 100 words.
"""
        }
    ]
)

summary_text = summary["message"]["content"]

print("\nSUMMARY:")
print(summary_text)


# ==========================================
# STEP 2: EXTRACT KEY POINTS
# ==========================================

print("\nExtracting key points...")

keypoints = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": f"""
Extract exactly 5 important key points
from the following summary:

{summary_text}
"""
        }
    ]
)

keypoints_text = keypoints["message"]["content"]

print("\nKEY POINTS:")
print(keypoints_text)


# ==========================================
# STEP 3: GENERATE QUESTIONS
# ==========================================

print("\nGenerating questions...")

questions = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": f"""
Generate exactly 3 important questions
using the following key points:

{keypoints_text}
"""
        }
    ]
)

questions_text = questions["message"]["content"]

print("\nQUESTIONS:")
print(questions_text)


# ==========================================
# COMPLETED
# ==========================================

print("\n" + "=" * 50)
print("PROMPT CHAINING COMPLETED")
print("=" * 50)
