import os
import numpy as np
import logging
from openai import OpenAI
from google import genai

from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.environ.get("PROJECT_ID")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class OpenAIModels:
    gpt4o = "gpt-4o"
    gpt4omini = "gpt-4o-mini"
    o1 = "o1"
    o1mini = "o1-mini"
    o3mini = "o3-mini"
    o1preview = "o1-preview"


class GeminiModels:
    gemini_2_0_flash = "gemini-2.0-flash"
    gemini_1_5_flash = "gemini-1.5-flash"
    gemini_1_5_pro = "gemini-1.5-pro"


class ClaudeModels:
    claude_3_7_sonnet = "claude-3-7-sonnet"



openai_model = OpenAIModels.gpt4o
gemini_model = GeminiModels.gemini_2_0_flash
claude_model = ClaudeModels.claude_3_7_sonnet

# genai.configure(api_key=GEMINI_API_KEY)
# gemini_client = genai.GenerativeModel(gemini_model)
# claude_client = genai.GenerativeModel(claude_model)
openai_client = OpenAI(api_key=OPENAI_API_KEY)
gemini_client = genai.Client(api_key=GEMINI_API_KEY)
claude_client = genai.Client(api_key=GEMINI_API_KEY)
# claude_client = genai.Client(project=PROJECT_ID, location="us-central1", vertexai=True)


def load_file(file_path):
    """Reads and returns the content of a file."""
    with open(file_path, "r") as f:
        return f.read()


def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, "w") as f:
        f.write(content)


def create_directory(path):
    """Creates a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)


def call_openai(prompt):
    """Calls the OpenAI API with the provided prompt."""
    messages = [{"role": "user", "content": prompt}]
    print(f"Running Query with OPENAI LLM {openai_model}")
    response = openai_client.chat.completions.create(
        model=openai_model,
        messages=messages,
    )
    return {
        "model_name": response.model,
        "usage": response.usage.total_tokens,
        "response": response.choices[0].message.content.strip(),
    }


def call_gemini(prompt):
    print(f"Running Query with GEMINI LLM {gemini_model}")
    response = gemini_client.models.generate_content(
        model=gemini_model, contents=[prompt]
    )
    return {
        "model_name": response.model_version,
        "usage": response.usage_metadata.total_token_count,
        "response": response.text,
    }


def call_claude(prompt):
    print(f"Running Query with Claude LLM {claude_model}")
    response = claude_client.models.generate_content(
        model=claude_model, contents=[prompt]
    )
    return {
        "model_name": response.model_version,
        "usage": response.usage_metadata.total_token_count,
        "response": response.text,
    }


def get_llm_output(context, user_prompt, llm="openai"):
    """Combines the context and user prompts, then gets output code from the chosen LLM."""
    full_prompt = context + "\n\n" + user_prompt
    if llm == "openai":
        return call_openai(full_prompt)
    elif llm == "gemini":
        return call_gemini(full_prompt)
    elif llm == "claude":
        return call_claude(full_prompt)
    else:
        raise ValueError("Unsupported LLM: choose 'openai', 'gemini' or 'claude' ")


def compare_snippets(snippet1, snippet2, llm="openai"):
    context = """
    You are given two snippets of code 
    You need to compare both of them in terms of similarity and functionality
    Give score between -1 and 1. -1 being totally different and 1 being most similar, keep the number precision upto 2 decimals
    return no additional text, just the result number
    """

    user_prompt = f"""
    #### SNIPPET 1 
    {snippet1}

    ### SNIPPET 2 
    {snippet2}
    """

    return get_llm_output(context, user_prompt, llm)


def get_embedding(text, provider="openai"):
    """Gets an embedding vector for the given text using the specified provider."""
    if provider == "openai":
        embedding_response = openai_client.embeddings.create(
            model="text-embedding-ada-002",
            input=text,
        )
        return embedding_response.data[0].embedding


def cosine_similarity(vec1, vec2):
    """Computes cosine similarity between two vectors."""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
