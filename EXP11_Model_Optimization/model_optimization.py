import ollama
import time

print("=" * 60)
print("MODEL OPTIMIZATION EXPERIMENT")
print("=" * 60)

MODEL = "llama3.2:latest"

question = input("\nEnter a question: ")

print("\nRunning model...")
start_time = time.time()

response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

end_time = time.time()

answer = response["message"]["content"]

print("\n" + "=" * 60)
print("MODEL RESPONSE")
print("=" * 60)

print(answer)

print("\n" + "=" * 60)
print("PERFORMANCE")
print("=" * 60)

print("Model:", MODEL)
print("Response Time:", round(end_time - start_time, 2), "seconds")

print("\n" + "=" * 60)
print("MODEL OPTIMIZATION COMPLETED")
print("=" * 60)
