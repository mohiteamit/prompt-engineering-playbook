from utils.openai_client import OpenAIClient

def test_openai_connection():
    """Tests the OpenAI API connection by making a simple request."""
    client = OpenAIClient().get_client()
    
    test_prompt = "What is the capital of France?"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": test_prompt}]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Testing OpenAI API connection...")
    result = test_openai_connection()
    print("Response:", result)
