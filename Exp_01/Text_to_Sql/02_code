import sqlite3
import ollama


# ==========================================
# 1. CREATE DATABASE
# ==========================================

def create_database():

    conn = sqlite3.connect("students.db")
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

    # Insert sample data only if table is empty
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

    return conn


# ==========================================
# 2. RETRIEVAL / RAG
# ==========================================

def retrieve_schema(question):

    schema = """
    DATABASE SCHEMA:

    Table: students

    Columns:
    id       INTEGER
    name     TEXT
    age      INTEGER
    course   TEXT
    marks    INTEGER

    The students table contains student information.
    """

    return schema


# ==========================================
# 3. OLLAMA TEXT-TO-SQL
# ==========================================

def generate_sql(question, schema):

    prompt = f"""
You are an expert SQLite SQL generator.

{schema}

User question:
{question}

Rules:
1. Generate only valid SQLite SQL.
2. Use only the students table.
3. Use only these columns:
   id, name, age, course, marks
4. Do not invent tables.
5. Do not invent columns.
6. Return ONLY the SQL query.
7. Do not use markdown.
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

    sql_query = response["message"]["content"].strip()

    # Remove markdown if Ollama adds it
    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")

    return sql_query.strip()


# ==========================================
# 4. MAIN PROGRAM
# ==========================================

def main():

    print("\nTEXT-TO-SQL WORKFLOW USING OLLAMA")
    print("=" * 55)

    # Create database
    conn = create_database()

    cursor = conn.cursor()

    # User question
    question = input("\nEnter your question: ")

    # Retrieval
    print("\nRetrieving database schema...")

    schema = retrieve_schema(question)

    # Generate SQL
    print("\nGenerating SQL query...")

    sql_query = generate_sql(question, schema)

    print("\nGenerated SQL:")
    print(sql_query)

    # Execute SQL
    print("\nExecuting query...")

    try:

        cursor.execute(sql_query)

        results = cursor.fetchall()

        if results:

            print("\nResults:")
            print("-" * 55)

            for row in results:
                print(row)

            print("-" * 55)

        else:

            print("\nNo results found.")

    except Exception as e:

        print("\nSQL Error:", e)

    conn.close()

    print("\nProgram completed successfully!")


# ==========================================
# 5. START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
