from pipeline import (
    run_pipeline,
    is_capability_question
)


def clear_processing():
    print(
        "\r" + " " * 50 + "\r",
        end="",
        flush=True
    )


def main():
    print("RAG Chat App")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("You: ").strip()

        if query.lower() == "exit":
            print("Goodbye!")
            break

        if not query:
            continue

        try:
            print(
                "Processing...",
                end="",
                flush=True
            )


            if is_capability_question(query):

                answer = run_pipeline(query)

                clear_processing()

                print(
                    f"Assistant: {answer}\n"
                )
            else:

                clear_processing()

                print(
                    "Assistant: ",
                    end="",
                    flush=True
                )

                run_pipeline(query)

                print()

        except Exception as error:

            clear_processing()

            print(
                f"Error: {error}\n"
            )


if __name__ == "__main__":
    main()