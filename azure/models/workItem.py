class WorkItem:
    def __init__(self, id:int, Title:str, BoardColumn:str, AssignedTo:str, IterationPath:str, WorkItemType:str, ClosedDate:str, ClosedBy:str, Priority:str, Client:str, Project:str, AnalystFunctional:str, Description:str):
        self.id = id
        self.title=Title
        self.boardColumn=BoardColumn
        self.assignedTo=AssignedTo
        self.iterationPath=IterationPath
        self.workItemType=WorkItemType
        self.closedDate=ClosedDate
        self.closedBy=ClosedBy
        self.priority=Priority
        self.client=Client
        self.project=Project
        self.analystFunctional=AnalystFunctional
        self.description=Description
    