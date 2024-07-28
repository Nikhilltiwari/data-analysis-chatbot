from typing import List
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_openai import ChatOpenAI

class CAMELAgent:
    def __init__(
        self,
        role_name: str,
        task: str,
        system_message: SystemMessage = None,
        model: ChatOpenAI = None,
    ) -> None:
        self.role_name = role_name
        self.task = task
        self.system_message = system_message
        self.model = model if model else ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.0)
        self.init_messages()

    def reset(self) -> None:
        self.init_messages()
        return self.stored_messages

    def init_messages(self) -> None:
        self.stored_messages = [self.system_message]

    def update_messages(self, message: BaseMessage) -> List[BaseMessage]:
        self.stored_messages.append(message)
        return self.stored_messages

    def step(
        self,
        input_message: HumanMessage,
    ) -> AIMessage:
        messages = self.update_messages(input_message)

        output_message = self.model.invoke(messages)
        self.update_messages(output_message)

        return output_message
