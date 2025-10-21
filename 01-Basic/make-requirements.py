import requests

def get_latest_version(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["info"]["version"]
    else:
        return None

def generate_requirements(packages):
    requirements = []
    for pkg in packages:
        version = get_latest_version(pkg)
        if version:
            requirements.append(f"{pkg}=={version}")
        else:
            requirements.append(f"# {pkg} (패키지 정보를 찾을 수 없음)")
    return "\n".join(requirements)

package_list = [
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
    "langchain-text-splitters"
]

# requirements.txt 출력
requirements_txt = generate_requirements(package_list)
print(requirements_txt)
