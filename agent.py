import requests

BASE_URL = "http://localhost:3000"

def query_knowledge(question):
    response = requests.post(f"{BASE_URL}/query_knowledge", json={"query": question})
    return response.json()

def get_case_studies(question):
    response = requests.post(f"{BASE_URL}/get_case_studies", json={"query": question})
    return response.json()

def main():
    user_input = input("Ask something: ")

    print("\nFetching knowledge...\n")
    knowledge = query_knowledge(user_input)

    print("Fetching case studies...\n")
    cases = get_case_studies(user_input)

    print("\n=== FINAL ANSWER ===\n")
    print("Knowledge:")
    print(knowledge)

    print("\nCase Studies:")
    print(cases)

    print("\nSources used:")
    print("- query_knowledge")
    print("- get_case_studies")

if __name__ == "__main__":
    main()
