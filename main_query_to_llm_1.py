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
def get_completion(prompt):
    ai_msg = llm.invoke(prompt)
    return ai_msg.content

# Main Method
if __name__ == "__main__":
    
    # Step 1: Query to LLM
    
    print(get_completion("What is 1+1?"))