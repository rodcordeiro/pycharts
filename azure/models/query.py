
class QueryColumns:
    def __init__(self,referenceName:str,name:str,url:str):
        self.referenceName = referenceName
        self.name = name
        self.url = url
class QueryWorkItems:
    def __init__(self,id:int,url:str):
        self.id = id
        self.url = url

class QUERY:
    def __init__(self,queryType:str,queryResultType:str,asOf:str,columns:list[QueryColumns],workItems:list[QueryWorkItems]):
        self.queryType=queryType
        self.queryResultType=queryResultType
        self.asOf=asOf
        self.columns=[QueryColumns(dict(column).get('referenceName'),dict(column).get('name'),dict(column).get('url')) for column in columns]
        self.workItems=[QueryWorkItems(dict(wi).get('id'),dict(wi).get('url')) for wi in workItems]
