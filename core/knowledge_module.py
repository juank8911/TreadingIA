from abc import ABC, abstractmethod


class Knowedge_model(ABC):
    @abstractmethod
    def get_knowledge(self,symbol):
        pass
    
    @abstractmethod
    def update_knowledge(self,symbol,knowledge):
        pass