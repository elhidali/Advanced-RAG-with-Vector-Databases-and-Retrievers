import os
from dotenv import load_dotenv
from llama_index.llms.openrouter import OpenRouter
from llama_index.llms.openai_like import OpenAILike
import httpx

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL")
model_id = os.getenv("MODEL_ID")

print("Testing OpenRouter...")
try:
    llm1 = OpenRouter(
        model=model_id,
        api_key=api_key,
        api_base=base_url,
        temperature=0.7,
        max_tokens=512,
        http_client=httpx.Client(verify=False)
    )
    response1 = llm1.complete("Hi")
    print("OpenRouter complete:", response1)
except Exception as e:
    print("OpenRouter error:", e)

print("Testing OpenAILike...")
try:
    llm2 = OpenAILike(
        model=model_id,
        api_key=api_key,
        api_base=base_url,
        is_chat_model=True,
        temperature=0.7,
        max_tokens=512,
        http_client=httpx.Client(verify=False)
    )
    response2 = llm2.complete("Hi")
    print("OpenAILike complete:", response2)
except Exception as e:
    print("OpenAILike error:", e)
