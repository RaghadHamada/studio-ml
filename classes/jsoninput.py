import pandas as pd
import json
from classes.input import Input
class JSONInput(Input):
    """ Class for the JSONInput step """
    def __init__(self, path: str):
        """ Instantiate the JSONInput class """
        super().__init__()
        self.path = path

    def process(self) -> pd.DataFrame:
        """ Process the data of the step so that it can be used by the next step """
        with open(self.path, "r") as f:
            data = json.load(f)['historicalStockList']
        df = pd.DataFrame(data[0]['data'])
        # set yhat_close_long and yhat_close_short to 'price' of that day in the dataframe
        data_of_apple = data[0]['data']
        # for each day in the dataframe set yhat_close_long of that row equal to the price of that day
        for day in data_of_apple:
            df.loc[df['date'] == day['date'], 'yhat_close_long'] = day['yhat_close_long']['price']
            # same for yhat_close_short
            df.loc[df['date'] == day['date'], 'yhat_close_short'] = day['yhat_close_short']['price']
            # get std in dataframe
            df.loc[df['date'] == day['date'], 'std_short'] = day['yhat_close_short']['std']
            # get std long in dataframe
            df.loc[df['date'] == day['date'], 'std_long'] = day['yhat_close_long']['std']
        # rename close to y and date to ds
        df = df.rename(columns={'close': 'y', 'date': 'ds'})
        return df 