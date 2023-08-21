import pandas as pd
from pandas import DataFrame

from azure.models.workItem import WorkItem


class Data:
    def __init__(self, payload: list[WorkItem]):
        self.__init__ = self
        self.data: DataFrame = self.__convertToList(payload)

    def __convertToList(self, objs: list[WorkItem]) -> DataFrame:
        dicts = []
        for item in objs:
            dicts.append(item.__dict__)
        return pd.json_normalize(dicts)

    def dashboardTotalItems(self):
        data = self.data[["workItemType"]].groupby(["workItemType"]).value_counts()
        print(data)
        # data.set_index("workItemType", inplace=True)
        # plot = data.plot.pie(y="workItemType", figsize=(7, 7))
        # print(plot)

    def perClient(self, client: str):
        data = self.data
        print(data)
