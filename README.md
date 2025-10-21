# LLM
## reference 
- [teddylee](https://github.com/teddylee777/langchain-kr/)


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
uv venv --python 3.15 --seed .venv
.venv/bin/python --version

source .venv/bin/activate # deactivate

echo $VIRTUAL_ENV
python --version
which python
which pip
```