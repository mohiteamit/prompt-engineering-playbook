# Prompt Engineering Playbook

Author: Amit Mohite  
Email: [mohite.amit@gmail.com](mailto:mohite.amit@gmail.com)

## 📌 Overview
The **Prompt Engineering Playbook** is a comprehensive learning exercise and demonstration repository that showcases various techniques and strategies for crafting effective prompts for Large Language Models (LLMs). The repository is designed to explore different prompting methods, test them in practical scenarios, and document best practices for using prompts effectively with generative AI models.

## 🎯 Objectives
- Demonstrate practical prompting techniques, including Zero-Shot, Few-Shot, Chain-of-Thought, Role-Based, and Advanced Strategies.
- Provide reusable code snippets and structured examples to aid learning and experimentation.
- Showcase practical applications through Jupyter notebooks and well-documented `.md` files.
- Centralize resources and utilities for easier integration with OpenAI and local LLMs.

---

## 📂 Folder Structure

### 1️⃣ **notebooks/**
- Contains Jupyter notebooks demonstrating different prompting strategies.
- Each notebook covers a specific technique with real-world examples and scenarios.
- **Key Notebooks:**
  - `01_intro_prompting.ipynb`: Introduction to basic prompting techniques.
  - `02_few_shot_prompting.ipynb`: Demonstrates few-shot learning using structured examples.
  - `03_chain_of_thought.ipynb`: Explores step-by-step reasoning with Chain-of-Thought.
  - `04_role_based_prompting.ipynb`: Shows how role-based prompts can guide responses.
  - `05_advanced_strategies.ipynb`: Combines advanced techniques like self-consistency and hybrid prompting.

### 2️⃣ **prompts/**
- Houses `.md` files with detailed documentation of each prompting technique.
- Each file provides explanations, example prompts, best practices, and pitfalls.
- **Included Files:**
  - `summarization.md`: Techniques for generating concise and accurate summaries.
  - `data_extraction.md`: Approaches for extracting structured data from text.
  - `reasoning.md`: Methods to enhance logical reasoning and problem-solving.
  - `creativity.md`: Strategies for creative writing and idea generation.
  - `code_generation.md`: Prompts for generating and explaining code.

### 3️⃣ **api/**
- Contains Python scripts to test API connections and local model interactions.
- **Scripts:**
  - `openai_test.py`: Tests connectivity with the OpenAI API using a sample query.
  - `local_llm_test.py`: Demonstrates how to interact with a local LLM (e.g., Phi-2) using `transformers`.

### 4️⃣ **utils/**
- Holds utility functions and helper classes to simplify code reuse.
- Includes the `openai_client.py` class, which centralizes API initialization and authentication.

### 5️⃣ **models/**
- Placeholder for storing local models (e.g., `phi-2.Q4_K_M.gguf`) if using local LLMs.
- This folder is not populated in the repository but should be used if local models are required.

### 6️⃣ **docs/**
- Additional documentation and supporting files for understanding and extending the playbook.
- Could be expanded to include images, diagrams, or supplementary guides.

---

## 🚀 How to Run

### 1️⃣ **Install Dependencies**
Navigate to the root folder and run:
```bash
pip install -e .
```
This will install the **`utils`** module and any required dependencies.

### 2️⃣ **Set Up OpenAI API Key**
- Create a `.env` file in the **root directory** with your **OpenAI API Key**:
```
OPENAI_API_KEY=your_api_key_here
```
- You can obtain an API key from the [OpenAI API website](https://platform.openai.com/signup).

### 3️⃣ **Run Jupyter Notebooks**
- Launch Jupyter Notebook from the terminal:
```bash
jupyter notebook
```
- Open any notebook from the **notebooks/** folder to explore different prompting techniques.

### 4️⃣ **Test API and Local Models**
- Run `openai_test.py` to verify the OpenAI API connection.
- Run `local_llm_test.py` to test interactions with a local LLM using `transformers`.

---

## 🛠 Future Extensions
- Adding more advanced prompting techniques (e.g., ReAct, dynamic prompts).
- Integrating more local models and exploring lightweight LLMs.
- Expanding use cases for business, education, and research scenarios.

---

## 📧 Contact
For questions, suggestions, or collaboration opportunities, please reach out to:  
**Amit Mohite** - [mohite.amit@gmail.com](mailto:mohite.amit@gmail.com)
