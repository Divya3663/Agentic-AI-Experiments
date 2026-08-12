import ollama
import json

MODEL = "llama3.2:latest"

print("=" * 60)
print("FINE-TUNING / DOMAIN ADAPTATION EXPERIMENT")
print("=" * 60)

# Load domain dataset
with open("dataset.jsonl", "r", encoding="utf-8") as file:
    data = [json.loads(line) for line in file]

print("\nDomain Dataset Loaded")
print("Number of examples:", len(data))

# Show training examples
print("\nTraining Examples:")
for item in data:
    print("\nQuestion:", item["instruction"])
    print("Answer:", item["response"])


# Create domain context from dataset
domain_knowledge = ""

for item in data:
    domain_knowledge += (
        "Question: " + item["instruction"] + "\n"
        "Answer: " + item["response"] + "\n\n"
    )


# Ask user a question
question = input("\nEnter a domain-related question: ")


print("\nGenerating domain-adapted response...")


response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": f"""
You are a specialized college and student information assistant.

Use the following domain knowledge to answer questions:

{domain_knowledge}

Give a clear and accurate answer.
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]
)


answer = response["message"]["content"]


print("\n" + "=" * 60)
print("DOMAIN-ADAPTED MODEL RESPONSE")
print("=" * 60)

print(answer)

print("\n" + "=" * 60)
print("EXPERIMENT COMPLETED")
print("=" * 60)
