
# import iterable class
from classes.step import Step
import pandas as pd
from collections.abc import Iterable
from classes.input import Input
class Pipeline:
    # What is a Pipeline?
    # A Pipeline is a set of instructions
    def __init__(self, steps: Iterable[Step]):
        """ Instantiate the Pipeline class by recieving a list of steps """
        if steps == ():
            raise ValueError("Pipeline steps are not specified")

        # OPTIONAL
        # if first step is not a input step (possible that inputstep is abstract, raise error)
        # if not isinstance(steps[0], Input):
        #     raise ValueError(f"First step in pipeline must be an input step it is now {type(steps[0])}")
        self.steps = steps

    # process -> take some data, modify it, output some data
    def process(self) -> pd.DataFrame:  # nog onzeker over format van data
        """ Process the data of the pipeline so that it can be used by the next step """
        for step in self.steps:
            print(f"Processing step: {step.name}")
            # step.config = self.settings
            # TODO: file aanmaken na elke stap zodat het niet opnieuw gedaan hoeft te worden indien er een fout optreedt
            if isinstance(step, Input):
                self.data = step.process()
            else:
                self.data = step.process(data=self.data)
        return self.data