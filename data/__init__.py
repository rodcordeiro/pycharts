import pandas as pd
from pandas import DataFrame

from azure.models.workItem import WorkItem

class Data:
    def __init__(self,payload: list[WorkItem]):
        self.__init__ = self
        self.data:DataFrame = self.__convertToList(payload)
    
    def __convertToList(self,objs: list[WorkItem]) -> DataFrame:
        dicts = []
        for item in objs:
            dicts.append(item.__dict__)
        return pd.json_normalize(dicts)
    
    def perClient(self):
        data = self.data
        print(data)
    