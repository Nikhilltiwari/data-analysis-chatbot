
from camelagents.camel_agent import CAMELAgent
from langchain.prompts import ChatPromptTemplate
from services.nlp import call_openai_model
from prompt import get_llm_prompt
from camelagents.util import get_specified_task, task_specifier_prompts, inception_prompts, get_sys_msgs, camel_chat

class CamelAgentManager:
    def __init__(self):
        self.agents = {
            'preprocess': CAMELAgent(role_name='Preprocess Agent', task='preprocess'),
            'analyze': CAMELAgent(role_name='Analyze Agent', task='analyze'),
            'visualize': CAMELAgent(role_name='Visualize Agent', task='visualize')
        }
        self.dataframes = {}
        prompt = get_llm_prompt()
        self.runnable_chain = prompt | call_openai_model

    # Removed the initialize_agents method as it's not needed

    def store_dataframe(self, filename, dataframe):
        self.dataframes[filename] = dataframe

    def retrieve_dataframe(self, filename):
        return self.dataframes.get(filename)

    def get_agent(self, task):
        return self.agents.get(task)

    def process_query(self, task, query, df):
        agent = self.get_agent(task)
        context = {'dataframe': df.to_dict()}
        response = self.runnable_chain.invoke({"input": query, "context": context})
        return response







