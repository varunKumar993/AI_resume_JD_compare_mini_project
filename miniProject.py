import os
import time
from pathlib import Path
from urllib import response
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

JD="""
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIS
- 2+ years of experience
"""


RESUME="""
Name: Rahul Sharma

Experience:
3 years as a Software Developer.

Skills:
Python, FastAPI, MySQL, Docker,
REST APIs, Git I

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""


def ask_llm(system_prompt, user_prompt):
    sys_msg = {
        "role": "system",
        "content": system_prompt
    }

    user_msg = {
        "role": "user",
        "content": user_prompt
    }

    messages = [sys_msg, user_msg]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    answer = response.choices[0].message.content
    return answer


def step1_res_extract():
    system_prompt = "You are a professional HR assistant. Extract the skills from the candidates resume provided."
    user_prompt = f"Extract the relevant information from the following resume:\n{RESUME}"
    extracted_info = ask_llm(system_prompt, user_prompt)
    return extracted_info

def step2_jd_extract():
    system_prompt = "You are a professional HR assistant. Extract the required skills from the job description provided."
    user_prompt = f"Extract the relevant information from the following job description:\n{JD}"
    extracted_info = ask_llm(system_prompt, user_prompt)
    return extracted_info

def step3_match(resume_info, jd_info):
    system_prompt = "You are a helpful assistant that matches resumes with job descriptions."
    user_prompt = f"Match the following resume information with the job description information:\nResume Info:\n{resume_info}\n\nJob Description Info:\n{jd_info}"
    match_result = ask_llm(system_prompt, user_prompt)
    return match_result

if __name__ == "__main__":
    resume_info = step1_res_extract()
    jd_info = step2_jd_extract()
    match_result = step3_match(resume_info, jd_info)

    print("Resume Information:")
    print(resume_info)
    print("\nJob Description Information:")
    print(jd_info)
    print("\nMatch Result:")
    print(match_result)