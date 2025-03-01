# Data Extraction Prompting

## Overview
Data extraction prompting is used to retrieve structured information from unstructured text. It is commonly applied in document processing, web scraping, database population, and text analytics.

## Techniques for Data Extraction

### 1️⃣ Keyword-Based Extraction
- Extracts specific words or phrases from the input text.
- Example Prompt:
  ```
  Extract all company names mentioned in the following text:
  "TechCorp and DataWorks announced a merger, while InnovateX remains independent."
  ```

### 2️⃣ Pattern-Based Extraction (Regex + LLM)
- Extracts structured data (e.g., dates, email addresses, phone numbers) using patterns.
- Example Prompt:
  ```
  Extract all email addresses from the following text:
  "Contact support at help@company.com or sales@business.org for more information."
  ```

### 3️⃣ Entity Recognition (NER - Named Entity Recognition)
- Identifies entities such as people, locations, dates, and product names.
- Example Prompt:
  ```
  Identify and list all locations mentioned in the following text:
  "John traveled from New York to San Francisco, stopping in Chicago along the way."
  ```

### 4️⃣ Structured Table Extraction
- Converts unstructured data into a structured format like tables.
- Example Prompt:
  ```
  Extract and format the following information into a table:
  "Alice, Marketing, 5 years experience. Bob, Engineering, 8 years experience. Carol, Sales, 3 years experience."
  ```
  Expected Output:
  | Name  | Department  | Experience |
  |-------|------------|------------|
  | Alice | Marketing  | 5 years    |
  | Bob   | Engineering | 8 years   |
  | Carol | Sales      | 3 years   |

### 5️⃣ Conditional Extraction
- Extracts data based on conditions (e.g., only extract numbers greater than 100).
- Example Prompt:
  ```
  Extract all transactions above $100 from the following:
  "$45, $120, $300, $80, $150."
  ```

## Best Practices for Data Extraction
- Use specific instructions (e.g., “Extract only dates” instead of “Extract information”).  
- If extracting structured data, request output in a table or JSON format for easier processing.  
- For accuracy, use few-shot examples where possible.  
- Combine Regex + LLM for higher precision when extracting complex data formats.  

## Common Pitfalls
- Ambiguous instructions (e.g., “Find important words” without specifying what is important).  
- Incorrect entity recognition if the prompt lacks context.  
- Extraction hallucination, where the model generates data that doesn’t exist in the input.  

## Advanced Applications
- Multi-document extraction (Extract structured insights from multiple sources).  
- Domain-specific entity extraction (e.g., extracting legal clauses, medical terms, financial transactions).  
- Combining data extraction with reasoning (e.g., extracting key takeaways along with relevant context).
