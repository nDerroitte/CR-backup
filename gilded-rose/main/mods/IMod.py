from abc import ABC, abstractmethod

class IMod(ABC):

    @abstractmethod
    def update_value(val):
        ...