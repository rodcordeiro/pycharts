import pandas as pd
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

from azure.models.workItem import WorkItem


class Data:
    def __init__(self, payload: list[WorkItem]):
        self.__init__ = self
        self.data: DataFrame = self.__convertToList(payload)

    def __convertToList(self, objs: list[WorkItem]) -> DataFrame:
        dicts = []
        for item in objs:
            dicts.append({**item.__dict__, "quantity": 1})
        return pd.json_normalize(dicts)

    def dashboardTotalItems(self):
        types = self.data.groupby(["workItemType"]).describe().index.tolist()
        values = self.data.query(f"workItemType == 'Bug'", inplace=True)
        print(types, values)

        # graph = sns.barplot(x="workItemType", y="quantity", color="blue")
        # graph.set_title("Work item x Tipo")
        # plt.show(graph)

    def perClient(self, client: str):
        data = self.data
        print(data)
