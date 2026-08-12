import ollama
import sqlite3
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


MODEL = "llama3.2:latest"


# ============================================================
# LOAD KNOWLEDGE BASE
# ============================================================

with open("knowledge.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = [
    line.strip()
    for line in text.split("\n")
    if line.strip()
]


# ============================================================
# CREATE RAG VECTORS
# ============================================================

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(chunks)


# ============================================================
# RAG AGENT
# ============================================================

def rag_agent(question):

    question_vector = vectorizer.transform([question])

    similarity = cosine_similarity(
        question_vector,
        vectors
    )[0]

    best_index = similarity.argmax()

    context = chunks[best_index]

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a college information assistant. Answer using the provided college knowledge."
            },
            {
                "role": "user",
                "content": f"""
College Knowledge:
{context}

Question:
{question}
"""
            }
        ]
    )

    return response["message"]["content"]


# ============================================================
# SQL TOOL
# ============================================================

def sql_tool():

    connection = sqlite3.connect("college.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            marks INTEGER
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM students")

    count = cursor.fetchone()[0]

    if count == 0:

        students = [
            (1, "Rahul", "CSE", 85),
            (2, "Anita", "ECE", 90),
            (3, "Kiran", "CSE", 78),
            (4, "Priya", "ECE", 88),
            (5, "Arjun", "CSE", 92)
        ]

        cursor.executemany(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            students
        )

        connection.commit()

    cursor.execute(
        "SELECT id, name, department, marks FROM students"
    )

    results = cursor.fetchall()

    connection.close()

    return results


# ============================================================
# GENERAL LLM AGENT
# ============================================================

def general_agent(question):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful college assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]


# ============================================================
# MAIN ROUTER AGENT
# ============================================================

def main_agent(question):

    question_lower = question.lower()

    database_words = [
        "student",
        "students",
        "marks",
        "database",
        "department",
        "scores",
        "records"
    ]

    knowledge_words = [
        "college",
        "course",
        "courses",
        "library",
        "hostel",
        "semester",
        "computer science",
        "admission"
    ]

    # SQL Agent
    if any(word in question_lower for word in database_words):

        results = sql_tool()

        answer = "Student Database Results:\n\n"

        for row in results:
            answer += (
                f"ID: {row[0]} | "
                f"Name: {row[1]} | "
                f"Department: {row[2]} | "
                f"Marks: {row[3]}\n"
            )

        return answer

    # RAG Agent
    elif any(word in question_lower for word in knowledge_words):

        return rag_agent(question)

    # General Agent
    else:

        return general_agent(question)


# ============================================================
# STREAMLIT USER INTERFACE
# ============================================================

st.set_page_config(
    page_title="AI College Assistant",
    page_icon="🎓"
)

st.title("🎓 AI College Assistant")

st.write(
    "End-to-End Agentic AI System using "
    "RAG, SQL Tools, Multi-Agent Processing and Ollama."
)

st.divider()

question = st.text_input(
    "Ask your question:"
)


if st.button("Ask"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("AI Agent is processing your question..."):

            answer = main_agent(question)

        st.subheader("Answer")

        st.write(answer)


st.divider()

st.caption(
    "EXP12 - Agentic AI Capstone Project"
)
