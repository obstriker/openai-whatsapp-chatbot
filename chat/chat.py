class Chat(ABC):
    def __init__(self):
        chat_history = []
        pass
    
    @abstractmethod
    def reply(self):
        pass
    
    @abstractmethod
    def end_chat(self):
        pass