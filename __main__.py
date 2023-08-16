from azure import Azure
import logging

logger = logging.getLogger('Charts')
logging.basicConfig(level=logging.INFO)

logger.info('Initializing')
az = Azure()

logger.info('Listing work items')
items = az.getWorkItems()

for item in items:
    logger.info(item.id)