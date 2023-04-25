from abc import ABC, abstractmethod
from langchain.memory import ConversationBufferWindowMemory
import openai
import os

class OpenAIChat(Chat):
    def __init__(self, model, api_key=None, chat_options):
        super().__init__()
        self.memory = ConversationBufferWindowMemory(k=2)
        self.prompt = PromptTemplate(
            input_variables=["user", "date"], 
            template=chat_options.get("start_system_message"))

        self.chatgpt_chain = LLMChain(
        llm=OpenAI(temperature=chat_options.get("temprature")), 
        prompt=self.prompt, 
        verbose=True, 
        memory=self.memory)
        
        self.chat_history = []
    
    def reply(self, message):
        reply = self.chatgpt_chain.predict(human_input=message)

        # Add history feature?
        # self.chat_history.append(f"User: {message}")

        return reply

    
    

    #def get_or_create(s)