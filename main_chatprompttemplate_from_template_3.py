from langchain_core.prompts import ChatPromptTemplate
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
    
    # Prompt using ChatPromptTemplate - from_template:
    customer_style = "American English in a calm and respectful tone"
    customer_msg = "Hello how are you? I am too much tired working in such an environment unable to grow as per the expectation"
    
    template_string = """Translate the text that is delimited by triple backticks into a style that is {style}. text: ```{text}```"""
    
    # Using the LangChain Prompt 
    chat_prompt = ChatPromptTemplate.from_template(template_string)
    print(chat_prompt.messages[0].prompt) # type: ignore

    text = "Hello how are you? I am too much tired working in such an environment unable to grow as per the expectation"
    customer_message = chat_prompt.format_messages(style=customer_style, text=customer_msg)
    print(customer_message) # type: ignore
    
    print(get_completion(customer_message))