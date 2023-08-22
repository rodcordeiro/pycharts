import json
import logging

from azure import Azure
from data import Data

logger = logging.getLogger("Charts")
logging.basicConfig(level=logging.INFO)

logger.info("Initializing")
az = Azure()

logger.info("Listing work items")
items = az.getWorkItems()

df = Data(items)
df.dashboardClientRankingPerType()
