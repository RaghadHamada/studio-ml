import pandas as pd
from classes.step import Step
from prophet import Prophet
class Forecaster(Step):
    
    def __init__(self, model: str) -> None:        
        # custom logic for each model
        self._models = {'prophet': Prophet()}
        self.model = self._models[model]
    @property
    def df(self) -> pd.DataFrame:
        self._df = self._df.sort_values(by=['ds'])
        return self._df
    def process(self, data) -> pd.DataFrame:
        self._df = data
        self.model.fit(self.df)
        # create a dataframe with the dates for the next month
        future = self.model.make_future_dataframe(periods=30)
        forecast = self.model.predict(future)
        return forecast
        