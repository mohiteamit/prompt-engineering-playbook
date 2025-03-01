import os ; os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
from transformers import AutoModelForCausalLM, AutoTokenizer


# Load the Phi-2 model from Hugging Face
model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=500, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    response = generate_response(
        "What data is used to train microsoft/phi-1 and microsoft/phi-2 and how was it sourced?"
    )
    print("Response:\n", response)
