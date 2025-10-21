import os
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
os.chdir(current_dir)
#print("현재 디렉토리:", os.getcwd())

from dotenv import load_dotenv
load_dotenv()

# pip install pymupdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
#from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# Load Document
loader = PyMuPDFLoader("data/SPRI_AI_Brief_2023년12월호_F.pdf")
docs = loader.load()
#print(f"문서의 페이지수: {len(docs)}")
#print(docs[10].page_content)
#print(docs[10].__dict__)

# Split Document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(docs)
#print(f"분할된 청크의수: {len(chunks)}")

# Create Embeddings
# Google Gemini API 무료 할당량 소진 시 HuggingFace 임베딩 사용 (로컬 무료)
# pip install sentence-transformers
# pip install langchain-huggingface
from langchain_huggingface import HuggingFaceEmbeddings

# 한국어 지원이 우수한 모델 사용
embeddings = HuggingFaceEmbeddings(
    model_name="jhgan/ko-sroberta-multitask",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

# 대안 1: Google Gemini (무료 할당량 있을 때)
# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 대안 2: OpenAI (API 키 필요, 유료)
# from langchain_openai import OpenAIEmbeddings
# embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Create DB
# pip install faiss-gpu
# pip install faiss-cpu
vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)
#for doc in vectorstore.similarity_search("구글"):
#    print(doc.page_content)

# Create Retreiver
retriever = vectorstore.as_retriever()
#print(retriever.invoke("삼성전자가 자체 개발한 AI 의 이름은?"))

# Create Prompt
prompt = PromptTemplate.from_template(
    """You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Answer in Korean.

#Context: 
{context}

#Question:
{question}

#Answer:"""
)

# LLM model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, max_tokens=2048).bind(logprobs=True)

# CreateChain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Run Chain
question = "삼성전자가 자체 개발한 AI 의 이름은?"
response = chain.invoke(question)
print(response)