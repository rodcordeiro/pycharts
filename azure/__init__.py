import base64
import requests
import json
import logging
from decouple import config

from .constants import QUERY_WIQL
from .itemDetails import concurrentRequests
from .models.query import QUERY
from .models.workItem import WorkItem

logger = logging.getLogger(__name__)

class Azure:
    def __init__(self):
        self.__init__ = self

        _personal_access_token = config("AZURE_PAT")
        _organization_url = 'https://dev.azure.com/' + config('AZURE_ORG')
        _encoded = str(base64.b64encode(bytes(':'+_personal_access_token, 'ascii')), 'ascii')
        self.__headers = {
            "Content-Type": "application/json",
            "Accept":"application/json",
            "Authorization": f"Basic {_encoded}"
        }
        self.baseUrl = f"{_organization_url}/Projetos/_apis"
        logger.debug(self.baseUrl)
        logger.debug(self.__headers)
        logger.info('Azure client instance created')
        
    def getQueryResult(self) -> QUERY:
        """
        Retrieves information about the work item provided id.
        """
        logger.debug('Retrieving query result')
        url = f"{self.baseUrl}/wit/wiql?api-version=7.1-preview.2"
        payload={"query": QUERY_WIQL}
        req = requests.post(url,headers=self.__headers,data=json.dumps(payload))
        data = req.json()
        response = QUERY(
            data.get('queryType'),
            data.get('queryResultType'),
            data.get('asOf'),
            data.get('columns'),
            data.get('workItems')
        )
        logger.debug('Retrieved query result')
        return response

    def getWorkItemDetails(self,item:int) -> WorkItem:
        """
        Retrieves information about the work item provided id.
        :param item: The work item id to retrieve information about
        """
        logger.debug('Retrieving work item details')
        url = f"{self.baseUrl}/wit/workitems/{item}?api-version=7.1-preview.2"
        req = requests.get(url,headers=self.__headers)
        payload = dict(req.json())
        payloadFields = dict(payload.get('fields'))
        logger.debug(f"Retrieved {item} work item details")
        return WorkItem(
            payload.get('id'),
            payloadFields.get('System.Title'),
            payloadFields.get('System.BoardColumn'),
            payloadFields.get('System.AssignedTo'),
            payloadFields.get('System.IterationPath'),
            payloadFields.get('System.WorkItemType'),
            payloadFields.get('Microsoft.VSTS.Common.ClosedDate'),
            payloadFields.get('Microsoft.VSTS.Common.ClosedBy'),
            payloadFields.get('Microsoft.VSTS.Common.Priority'),
            payloadFields.get('Custom.Client'),
            payloadFields.get('Custom.Project'),
            payloadFields.get('Custom.AnalystFunctional'),
            payloadFields.get('Custom.Description'),
            )
        
    
    def getWorkItems(self) -> list[WorkItem]:
        try:
            query = self.getQueryResult()
            urls = [f"{self.baseUrl}/wit/workitems/{wi.id}?api-version=7.1-preview.2" for wi in query.workItems]
            workItems = []
            logger.info(f"{len(urls)} work items identified. Retrieving details")
            def parse(item):
                payload = dict(item)
                payloadFields = dict(payload.get('fields'))
                workItems.append(WorkItem(
                    payload.get('id'),
                    payloadFields.get('System.Title'),
                    payloadFields.get('System.BoardColumn'),
                    payloadFields.get('System.AssignedTo'),
                    payloadFields.get('System.IterationPath'),
                    payloadFields.get('System.WorkItemType'),
                    payloadFields.get('Microsoft.VSTS.Common.ClosedDate'),
                    payloadFields.get('Microsoft.VSTS.Common.ClosedBy'),
                    payloadFields.get('Microsoft.VSTS.Common.Priority'),
                    payloadFields.get('Custom.Client'),
                    payloadFields.get('Custom.Project'),
                    payloadFields.get('Custom.AnalystFunctional'),
                    payloadFields.get('Custom.Description'),
                    ))
            concurrentRequests(self.__headers,urls,parse)
            logger.debug('Work items details retrieved.')
            return workItems
        except Exception:
            logger.error('Failed to list work items')
            
