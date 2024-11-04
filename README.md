# LangChain LLM Prompting Examples

This repository contains examples of using the LangChain framework to interact with Large Language Models (LLMs) for different prompt construction and execution techniques. Each script demonstrates a different approach for creating and using prompts with LLMs in Python, leveraging LangChain’s utilities for managing prompts, output parsing, and chain execution.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Scripts](#scripts)
  - [main_query_to_llm_1.py](#main_query_to_llm_1py)
  - [main_f_string_query_llm_2.py](#main_f_string_query_llm_2py)
  - [main_chatprompttemplate_from_template_3.py](#main_chatprompttemplate_from_template_3py)
  - [main_chatprompttemplate_from_messages_4.py](#main_chatprompttemplate_from_messages_4py)
- [Running the Scripts](#running-the-scripts)
- [License](#license)

## Overview

This project demonstrates how to structure and manage queries for an LLM, using LangChain's prompt utilities. Each script explores a different way of constructing prompts, ranging from basic string interpolation to using LangChain’s advanced `ChatPromptTemplate` methods for more complex interactions.

## Prerequisites

- Python 3.7 or above
- OpenAI API key or other compatible LLM provider API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vinodvpillai/langchain-llm-prompt-examples.git
   cd langchain-llm-prompt-examples
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment with an API key for accessing LLMs:
   ```bash
   export OPENAI_API_KEY="your_api_key"
   ```

## Scripts

### 1. `main_query_to_llm_1.py`

This script demonstrates a simple interaction with an LLM where the query is passed directly to the model. It’s a basic example that shows how to structure a straightforward question-response interaction with an LLM using LangChain’s core LLM API.

- **Usage**: Run the script with a query to see the LLM's direct response.
  
### 2. `main_f_string_query_llm_2.py`

In this script, an f-string is used to embed variables into a prompt dynamically. This is a flexible way to format queries when there are parameters or contextual data you need to include in the prompt without using LangChain's more advanced templates.

- **Usage**: Run the script with a query that contains dynamic content, formatted through Python’s f-strings.

### 3. `main_chatprompttemplate_from_template_3.py`

This script uses the `ChatPromptTemplate.from_template` method from LangChain to create prompts. This approach enables structured templates, making it easier to maintain prompt consistency across multiple queries. `from_template` allows for more structured variable substitution than basic f-strings and is well-suited for reusability in complex workflows.

- **Usage**: Run the script with a structured prompt template. Variables in the template are automatically substituted by LangChain.

### 4. `main_chatprompttemplate_from_messages_4.py`

This example showcases using `ChatPromptTemplate.from_messages` to construct a chat-based prompt template. It enables multi-turn conversations by creating a sequence of messages, which can simulate more interactive LLM behavior, such as holding context over multiple exchanges.

- **Usage**: Run the script to initiate a conversation with the LLM, where the prompt contains multiple message components.

## Running the Scripts

To run any of the scripts:

```bash
python script_name.py
```

Replace `script_name.py` with the desired script (e.g., `main_query_to_llm_1.py`).

Each script will print the LLM response based on the prompt and template setup used in that script.

## License

This project is licensed under the MIT License.