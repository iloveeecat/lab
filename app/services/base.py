from abc import ABC, abstractmethod

class IPService(ABC):
    @abstractmethod
    async def get_ip(self):
        pass
