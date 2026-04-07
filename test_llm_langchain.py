import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import httpx

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL")
model_id = os.getenv("MODEL_ID")

print("Testing LangChain ChatOpenAI...")
try:
    llm = ChatOpenAI(
        model=model_id,
        openai_api_key=api_key,
        openai_api_base=base_url,
        temperature=0.7,
        max_tokens=512,
        http_client=httpx.Client(verify=False)
    )
    result = llm.invoke([HumanMessage(content="Hi")])
    print("ChatOpenAI complete:", result.content)
except Exception as e:
    print("ChatOpenAI error:", e)
