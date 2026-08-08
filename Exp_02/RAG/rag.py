import ollama
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("=" * 50)
print("RAG-Based Question Answering System")
print("=" * 50)

# Load knowledge base
with open("knowledge.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split knowledge into chunks
chunks = [line.strip() for line in text.split("\n") if line.strip()]

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(chunks)

# Get user question
question = input("\nAsk your question: ")

# Convert question into vector
question_vector = vectorizer.transform([question])

# Calculate similarity
similarity = cosine_similarity(question_vector, vectors)[0]

# Get most relevant chunks
top_indices = similarity.argsort()[-3:][::-1]

context = "\n".join(chunks[i] for i in top_indices)

# Generate answer using Ollama
response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"""Answer the question using only the following context.

Context:
{context}

Question:
{question}

Give a clear and simple answer."""
        }
    ]
)

print("\n" + "=" * 50)
print("ANSWER")
print("=" * 50)
print(response["message"]["content"])
