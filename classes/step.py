from abc import ABC, abstractmethod
import pandas as pd


"""
step sub-classes must implement method process
"""


class Step(ABC):

    def __init__(self, model=None, class_type=None):
        """ Instantiate the Step class """
        # NOTE: issubclass(self.__class__, type) werkt niet
        if self.__class__ == class_type:
            raise Exception("I am abstract!")
        self.model = model

    @property
    def name(self) -> str:
        """ Return the name of the step """
        print(self.__class__.__name__) # TODO debug
        return str(self.__class__.__name__)

    @abstractmethod
    def process(self, data) -> pd.DataFrame:
        """abstract method for using the data of the step."""
        pass
