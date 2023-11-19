import json
from classes.step import Step
class Input(Step):
    """" Class for the input step"""
    """" should be the first step in the pipeline """

    def __init__(self):
        """ Instantiate the Input class """
        super().__init__()
        if self.__class__ == Input:
            raise Exception("I am abstract!")

    @property
    def name(self) -> str:
        """ Return the name of the step """
        return self.__class__.__name__

    def process(self) -> object:
        """ abstract method for using the data of the step """
        pass