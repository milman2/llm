# LLM
## reference 
- [teddylee langchain-kr](https://github.com/teddylee777/langchain-kr/)
- [teddylee langchain-teddynote python package](https://github.com/teddylee777/langchain-teddynote/)

# VS Code extension
- ms-python.python
- .vscode/settings.json
```json
{
  "python.pythonPath": "${workspaceFolder}/.venv/bin/python"
}
```

# Python virtual enviroment
```shell
uv venv --python 3.12 --seed .venv
.venv/bin/python --version

source .venv/bin/activate # deactivate

echo $VIRTUAL_ENV
python --version
which python
which pip

pip install dotenv langchain-openai
pip install langchain-google-genai
```