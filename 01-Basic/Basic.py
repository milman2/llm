from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)
print(f"[API KEY]\n{os.environ['OPENAI_API_KEY'][:-15]}" + "*" * 15)

from importlib.metadata import version

print("[LangChain 관련 패키지 버전]")
for package_name in [
    "dotenv",
    "langchain",
    "langchain-core",
    "langchain-experimental",
    "langchain-community",
    "langchain-openai",
    "langchain-teddynote",
    "langchain-huggingface",
    "langchain-google-genai",
    "langchain-anthropic",
    "langchain-cohere",
    "langchain-chroma",
    "langchain-elasticsearch",
    "langchain-upstage",
    "langchain-cohere",
    "langchain-milvus",
    "langchain-text-splitters",
]:
    try:
        package_version = version(package_name)
        print(f"{package_name}: {package_version}")
    except ImportError:
        print(f"{package_name}: 설치되지 않음")