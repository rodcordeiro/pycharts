import pandas as pd
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

from azure.models.workItem import WorkItem


class Data:
    """
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

        graph = sns.barplot(x=types, y=values, color="blue")
        graph.set_title("Work item x Tipo")
        return plt.show(graph)

    def perClient(self, client: str):
        data = self.data
        print(data)
"""
    def __init__(self, payload: list[WorkItem]):
        self.data = self.__convertToList(payload)

    def __convertToList(self, objs: list[WorkItem]) -> pd.DataFrame:
        dicts = []
        for item in objs:
            dicts.append({**item.__dict__, "quantity": 1})
        return pd.DataFrame(dicts)

    def dashboardTotalItems(self):
        # Agrupar por tipo de trabalho e contar a quantidade de ocorrências
        type_counts = self.data["workItemType"].value_counts()

        # Criar o gráfico de barras
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 6))
        graph = sns.barplot(x=type_counts.index, y=type_counts.values, color="blue")
        graph.set_title("Work item x Tipo")
        graph.set_xlabel("Types of Work")
        graph.set_ylabel("Frequency")
        # Ajustar a margem inferior para dar espaço ao título
        plt.subplots_adjust(bottom=0.2)
        # Alinhar os rótulos no eixo x
        plt.xticks(rotation=45, ha="right")
        for i, v in enumerate(type_counts.values):
            # Adicionar os valores no topo das barras // MEU LINDÃO
            graph.text(i, v + 1, str(v), color='black', ha='center')
        return plt.show()


    def perClient(self, client: str):
        data = self.data
        print(data)
