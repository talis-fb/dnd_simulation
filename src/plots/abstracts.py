from abc import ABC, abstractmethod
from dataclasses import dataclass
from pandas import DataFrame

@dataclass
class Plot(ABC):
    df:DataFrame

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def show(self):
        pass
