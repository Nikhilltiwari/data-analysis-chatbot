from langchain.llms import OpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from prompt import get_llm_prompt

class CamelAgentManager:
    def __init__(self):
        self.llm = OpenAI(model="text-davinci-003")
        self.llm_chain = LLMChain(llm=self.llm, prompt=ChatPromptTemplate.from_template(get_llm_prompt()))

    def call_openai_model(self, context):
        return self.llm_chain.run(context)
    
    # ... other methods to store and retrieve dataframes







