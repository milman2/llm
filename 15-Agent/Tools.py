# pip install langchain-experimental
from langchain_experimental.tools import PythonREPLTool

# Python REPL tool
python_tool = PythonREPLTool()
print(python_tool.invoke("print(100 + 200)"))

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

def print_and_execute(code, debug=False):
    if debug:
        print("CODE:")
        print(code)
    return python_tool.invoke(code)

# 파이썬 코드를 작성하도록 요청하는 프롬프트
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are Raymond Hetting, an expert python programmer, well versed in meta-programming and elegant, concise and short but well documented code. You follow the PEP8 style guide. "
            "Return only the code, no intro, no explanation, no chatty, no markdown, no code block, no nothing. Just the code.",
        ),
        ("human", "{input}"),
    ]
)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, max_tokens=2048).bind(logprobs=True)
if False:
    chain = prompt | llm | StrOutputParser() | RunnableLambda(lambda code: print_and_execute(code, debug=True))
    print(chain.invoke("로또 번호 생성기를 출력하는 코드를 작성하세요."))

# Tavily Search API tool
# pip install langchain-tavily
from langchain_tavily import TavilySearch
if False:
    tool = TavilySearch(
        max_results=6,
        include_answer=True,
        include_raw_content=True,
        # include_images=True,
        # search_depth="advanced", # or "basic"
        include_domains=["github.io", "wikidocs.net"],
        # exclude_domains = []
    )
    print(tool.invoke({"query": "LangChain Tools에 대해서 알려주세요."}))

# DALL-E
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

# Custom Tool
from langchain.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b
print(add_numbers.invoke({"a": 3, "b": 4}))    
print(multiply_numbers.invoke({"a": 3, "b": 4}))


# Google news (RSS)
# https://github.com/teddylee777/langchain-teddynote/blob/01ce78268a184fd19ec81f444810446b289e076d/langchain_teddynote/tools/news.py

# 대안 1: DuckDuckGo Search (API key 불필요)
# pip install ddgs
from langchain_community.tools import DuckDuckGoSearchResults
if False:
    ddg_tool = DuckDuckGoSearchResults()
    print(ddg_tool.invoke({"query": "LangChain news"}))

# 대안 2: Wikipedia
# pip install wikipedia
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
if False:
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    print(wikipedia.invoke({"query": "LangChain"}))