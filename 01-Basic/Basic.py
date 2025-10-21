# pip install dotenv
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

# pip install langchain-openai
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_tokens=2048).bind(logprobs=True)
# prompt = ChatPromptTemplate.from_template("What is the capital of {country}?")
# chain = prompt | llm | StrOutputParser()
# print(chain.invoke({"country": "France"}))

# pip install langchain-google-genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, max_tokens=2048).bind(logprobs=True)

# prompt = ChatPromptTemplate.from_template("What is the capital of {country}?")
# chain = prompt | llm | StrOutputParser()
# print(chain.invoke({"country": "France"})) # chain.stream(input)

# answer = llm.stream("대한민국의 아름다운 관광지 10곳과 주소를 알려주세요!")
# for token in answer:
#     print(token.content, end="", flush=True)


# Prompt Caching

# Multi-modal model
from langchain_core.messages import HumanMessage
image_url = "https://raw.githubusercontent.com/teddylee777/langchain-kr/main/01-Basic/images/sample-image2.jpeg"
message = HumanMessage(content=[
    {
        "type": "image_url",
        "image_url": {"url": image_url}
    },
    {
        "type": "text",
        "text": "What is this image about?"
    }
])
print(llm.invoke([message]).content)

# LCEL interface : Runnable
# stream, invoke, batch : 동기
# astream, ainvoke, abatch, astream_log

from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda