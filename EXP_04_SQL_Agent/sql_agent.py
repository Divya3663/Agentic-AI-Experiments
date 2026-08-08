import sqlite3
import ollama


# ==================================================
# 1. CREATE DATABASE
# ==================================================

def create_database():

    conn = sqlite3.connect("college.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT,
            marks INTEGER
        )
    """)

    # Check whether data already exists
    cursor.execute("SELECT COUNT(*) FROM students")

    count = cursor.fetchone()[0]

    if count == 0:

        students = [
            (1, "Rahul", 21, "CSE", 85),
            (2, "Priya", 22, "Cyber Security", 90),
            (3, "Arjun", 20, "CSE", 78),
            (4, "Sneha", 21, "AI", 88),
            (5, "Kiran", 22, "Data Science", 92)
        ]

        cursor.executemany("""
            INSERT INTO students
            VALUES (?, ?, ?, ?, ?)
        """, students)

    conn.commit()
    conn.close()


# ==================================================
# 2. DATABASE TOOL
# ==================================================

def database_tool(sql):

    conn = sqlite3.connect("college.db")

    cursor = conn.cursor()

    try:

        cursor.execute(sql)

        result = cursor.fetchall()

        conn.close()

        return result

    except Exception as e:

        conn.close()

        return f"Database Error: {e}"


# ==================================================
# 3. SQL AGENT
# ==================================================

def sql_agent(question):

    schema = """
    Database: college.db

    Table: students

    Columns:
    id
    name
    age
    course
    marks
    """

    prompt = f"""
You are a SQL agent.

Your job is to answer the user's question
using the database.

Database schema:

{schema}

Available database tool:

database_tool(SQL)

The tool executes SQL on the database.

User question:

{question}

Generate ONLY a valid SQLite SQL query.

Do not explain.
Do not use markdown.
"""

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    sql = response["message"]["content"].strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()


# ==================================================
# 4. MAIN AGENT
# ==================================================

def main():

    print("=" * 60)
    print("SQL AGENT WITH TOOL USE")
    print("=" * 60)

    # Create database
    create_database()

    # Get question
    question = input("\nEnter your question: ")

    # ReAct - Thought
    print("\nTHOUGHT:")
    print("I need to query the database to answer the question.")

    # ReAct - Action
    print("\nACTION:")
    print("Generating SQL query...")

    sql = sql_agent(question)

    print("\nSQL:")
    print(sql)

    # Tool use
    print("\nACTION:")
    print("Calling database_tool...")

    result = database_tool(sql)

    # ReAct - Observation
    print("\nOBSERVATION:")
    print(result)

    # Final answer
    print("\nFINAL ANSWER:")
    print("Database result:", result)

    print("\n" + "=" * 60)
    print("SQL AGENT COMPLETED")
    print("=" * 60)


# ==================================================
# 5. START
# ==================================================

if __name__ == "__main__":
    main()
