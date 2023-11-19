from classes.forecaster import Forecaster
from classes.pipeline import Pipeline
import json 
from classes.jsoninput import JSONInput
import os

def main(): 
    jsoninput = JSONInput(path='data/data.json')
    forecaster = Forecaster(model='prophet')
    pipeline = Pipeline([jsoninput, forecaster])
    data = pipeline.process()
    print(data.tail())
    
    
if __name__ == "__main__":
    main()