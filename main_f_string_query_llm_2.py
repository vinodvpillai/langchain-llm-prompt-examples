from langchain_openai import ChatOpenAI

import os
from os.path import join, dirname
from dotenv import load_dotenv

# Loading the environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# LLM
llm = ChatOpenAI(temperature=0, model=os.environ.get('OPENAI_MODEL'), api_key=os.environ.get('OPENAI_API_KEY'))  # type: ignore

# Completion Method 
"""
Passing the query directly to the LLM
"""
def get_completion(prompt):
    ai_msg = llm.invoke(prompt)
    return ai_msg.content

# Main Method
if __name__ == "__main__":
    
    # Simple prompt using Direct F-String:
    style = "Hindi in a calm and respectful tone"
    customer_msg = "Hello how are you? I am too much tired working in such an environment unable to grow as per the expectation"
    
    prompt = f"""Translate the text that is delimited by triple backticks into a style that is {style}. text: ```{customer_msg}```"""
    print(prompt)
    print(get_completion(prompt))