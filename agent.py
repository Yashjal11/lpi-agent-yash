import subprocess
import sys

def run_lpi():
    try:
        result = subprocess.run(
            "cd ../lpi-developer-kit && npm run test-client",
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise Exception(result.stderr)

        return result.stdout

    except Exception as e:
        return f"Error running LPI tools: {e}"

def explain(user_input):
    return f"""
This answer is based on LPI tools like:
- query_knowledge
- get_case_studies

These tools provide structured knowledge and real-world examples.
The recommendation is based on those outputs.
"""

def main():
    try:
        user_input = input("Ask something: ").strip()

        if not user_input:
            print("Please enter a valid question")
            return

        print("\nRunning LPI tools...\n")
        output = run_lpi()

        print("\n=== AGENT RESPONSE ===\n")
        print(f"User Question: {user_input}\n")

        print("Relevant Output:")
        print(output[:1500])

        print("\nExplainability:")
        print(explain(user_input))

        print("\nSources Used:")
        print("- query_knowledge")
        print("- get_case_studies")

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
