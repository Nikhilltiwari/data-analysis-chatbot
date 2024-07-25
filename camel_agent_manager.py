from camel_agents import CamelAgent

class CamelAgentManager:
    def __init__(self):
        self.agents = {
            'preprocess': CamelAgent(task='preprocess'),
            'analyze': CamelAgent(task='analyze'),
            'visualize': CamelAgent(task='visualize')
        }
        self.dataframes = {}

    def initialize_agents(self):
        for agent in self.agents.values():
            agent.initialize()

    def store_dataframe(self, filename, dataframe):
        self.dataframes[filename] = dataframe

    def retrieve_dataframe(self, filename):
        return self.dataframes.get(filename)

    def get_agent(self, task):
        return self.agents.get(task)
