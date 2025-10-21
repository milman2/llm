# PromptTemplate
from langchain_core.prompts import PromptTemplate
# - template, input_variables, partial_variables
# - from_template
# - format
# - partial

# loading template from file
from langchain_core.prompts import load_prompt

# ChatPromptTemplate
# - message tuple (role, message)
# - role
#   - "system"
#   - "human"
#   - "ai"

# MessagePlaceholder
from langchain_core.prompts import MessagesPlaceholder

# FewShotPromptTemplate
from langchain_core.prompts import FewShotPromptTemplate