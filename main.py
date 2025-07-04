import os
import sys
from dotenv import load_dotenv

def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    
    verbose = False
    if "--verbose" in sys.argv:
        verbose = True

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    from google import genai

    client = genai.Client(api_key=api_key)

    from google.genai import types

    model = "gemini-2.0-flash-001"
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(model=model, contents=messages)

    if verbose:
        print(f"User prompt: {user_prompt}")
    print(response.text)
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def usage():
    print("uv run main.py <AI prompt>")

if __name__ == "__main__":
    main()
