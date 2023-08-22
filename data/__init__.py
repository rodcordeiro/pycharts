import pandas as pd
from pandas import DataFrame
import seaborn as sns
import plotly.express as px

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
        values = [
            len(self.data[self.data["workItemType"] == wiType].index.tolist())
            for wiType in types
        ]
        fig = px.pie(
            names=types,
            values=values,
            title="Comparação tipo x total de itens",
            labels={"x": "Tipo", "y": "Total"},
            hole=0.6,
        )
        fig.show()

    def dashboardClientRankingPerType(self):
        types = self.data.groupby(["workItemType"]).describe().index.tolist()
        clients = self.data.groupby(["client"]).describe().index.tolist()
        print(types, clients)

    def perClient(self, client: str):
        data = self.data
        print(data)
