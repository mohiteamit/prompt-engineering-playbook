import csv
from datetime import datetime
from utils.openai_client import OpenAIClient

# Initialize OpenAI client
client = OpenAIClient().get_client()

# Define test prompts and expected outputs
test_cases = [
    # Zero-Shot Summarization
    {
        "strategy": "Zero-Shot",
        "prompt": "Summarize the following text: 'The market saw a rise in tech stocks last week.'",
        "expected": "Summary of tech stock market trends."
    },
    # Chain-of-Thought Reasoning
    {
        "strategy": "Chain-of-Thought",
        "prompt": "Solve the following math problem step by step: A shop sells 3 books for $5 each. What is the total cost?",
        "expected": "Step-by-step calculation leading to $15."
    },
    # Role-Based Customer Support
    {
        "strategy": "Role-Based",
        "prompt": "You are a helpful customer support agent. A customer asks: 'How do I reset my password?'",
        "expected": "Instructions for password reset."
    },
    # Few-Shot Prompting
    {
        "strategy": "Few-Shot",
        "prompt": "Translate the following sentence to French: 'Good morning!'",
        "expected": "Bonjour!"
    },
    # Self-Consistency Prompting
    {
        "strategy": "Self-Consistency",
        "prompt": "Provide three ways to improve workplace productivity.",
        "expected": "Common suggestions like time management, setting goals, reducing distractions."
    },
    # Creative Story Generation
    {
        "strategy": "Creativity",
        "prompt": "Write a short story about a robot that learns to play guitar.",
        "expected": "A creative story with a beginning, middle, and end."
    },
    # Code Generation
    {
        "strategy": "Code Generation",
        "prompt": "Write a Python function to calculate the factorial of a number.",
        "expected": "A Python function using recursion or iteration."
    },
    # Business Email Drafting
    {
        "strategy": "Role-Based",
        "prompt": "You are a professional HR manager. Draft an email to welcome a new employee.",
        "expected": "A warm, professional welcome email with key information."
    },
    # Data Extraction
    {
        "strategy": "Data Extraction",
        "prompt": "Extract all phone numbers from the following text: 'Contact us at 123-456-7890 or 987-654-3210.'",
        "expected": "List of phone numbers."
    },
    # Conditional Reasoning
    {
        "strategy": "Conditional Extraction",
        "prompt": "Extract all numbers greater than 100 from: '45, 120, 300, 80, 150.'",
        "expected": "120, 300, 150."
    },
    # Product Description Writing
    {
        "strategy": "Creativity",
        "prompt": "Write a compelling product description for a smartwatch.",
        "expected": "Features, benefits, and a call to action."
    },
    # Translation
    {
        "strategy": "Few-Shot",
        "prompt": "Translate 'Thank you' to Spanish.",
        "expected": "Gracias."
    },
    # Meeting Summary
    {
        "strategy": "Summarization",
        "prompt": "Summarize the meeting notes: 'Discussed project timeline, assigned tasks, and reviewed budget.'",
        "expected": "Summary of meeting outcomes."
    },
    # Legal Explanation
    {
        "strategy": "Role-Based",
        "prompt": "You are a legal advisor. Explain the term 'Force Majeure' in simple terms.",
        "expected": "Clear and simple explanation of legal concept."
    },
    # Educational Content Creation
    {
        "strategy": "Creativity",
        "prompt": "Create a short quiz on world history for high school students.",
        "expected": "A list of relevant questions with or without answers."
    },
    # Persuasive Writing
    {
        "strategy": "Role-Based",
        "prompt": "You are a marketing expert. Write a persuasive ad copy for an eco-friendly water bottle.",
        "expected": "A persuasive, eco-conscious ad message."
    },
    # Workflow Automation Script
    {
        "strategy": "Code Generation",
        "prompt": "Generate a Python script to rename all files in a folder to lowercase.",
        "expected": "A script using os or pathlib modules."
    },
    # Step-by-Step Instruction
    {
        "strategy": "Chain-of-Thought",
        "prompt": "Explain step by step how to change a flat tire on a car.",
        "expected": "Clear, step-by-step instructions."
    },
    # Health Advice
    {
        "strategy": "Role-Based",
        "prompt": "You are a nutritionist. Provide healthy snack ideas for someone on a low-carb diet.",
        "expected": "List of low-carb snack options."
    },
    # Troubleshooting
    {
        "strategy": "Chain-of-Thought",
        "prompt": "Troubleshoot why a computer might not be connecting to the internet step by step.",
        "expected": "Systematic troubleshooting steps."
    }
]

# Function to test prompts and save results
def evaluate_prompt(prompt, strategy, expected_output, model="gpt-4"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    output = response.choices[0].message.content
    return {
        "strategy": strategy,
        "prompt": prompt,
        "expected": expected_output,
        "actual": output,
        "timestamp": datetime.now().isoformat()
    }

# Evaluate all test cases and save to CSV
def run_evaluations(output_file="evaluations/benchmark_results.csv"):
    results = []
    for case in test_cases:
        result = evaluate_prompt(case["prompt"], case["strategy"], case["expected"])
        results.append(result)

    # Write results to CSV
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    run_evaluations()