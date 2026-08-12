import ollama
import os


MODEL = "llama3.2-vision:latest"


# ==========================================================
# IMAGE VISUAL QA
# ==========================================================

def visual_qa(image_path, question):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question,
                "images": [image_path]
            }
        ]
    )

    return response["message"]["content"]


# ==========================================================
# MAIN PROGRAM
# ==========================================================

def main():

    print("=" * 60)
    print("IMAGE RETRIEVAL / VISUAL QA SYSTEM")
    print("=" * 60)

    image_name = input("\nEnter image filename: ")

    image_path = os.path.join(
        "images",
        image_name
    )

    # Check whether image exists
    if not os.path.exists(image_path):

        print("\nERROR: Image not found.")

        print("\nMake sure the image is inside:")
        print("EXP8_Visual_QA/images/")

        return

    question = input(
        "\nAsk a question about the image: "
    )

    print("\nProcessing image...")
    print("Using Llama 3.2 Vision...")

    answer = visual_qa(
        image_path,
        question
    )

    print("\n" + "=" * 60)
    print("VISUAL QA ANSWER")
    print("=" * 60)

    print(answer)

    print("\n" + "=" * 60)
    print("VISUAL QA COMPLETED")
    print("=" * 60)


# ==========================================================
# START
# ==========================================================

if __name__ == "__main__":
    main()
