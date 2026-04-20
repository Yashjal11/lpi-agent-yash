import subprocess

def run_tool(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def main():
    user_input = input("Ask something: ")

    print("\nFetching knowledge...\n")
    knowledge = run_tool(f"npm run test-client")

    print("\n=== FINAL ANSWER ===\n")
    print("Based on LPI tools:\n")

    print(knowledge)

    print("\nSources used:")
    print("- query_knowledge")
    print("- get_case_studies")

if __name__ == "__main__":
    main()
