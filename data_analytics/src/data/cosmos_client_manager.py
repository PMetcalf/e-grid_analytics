'''
cosmos_client_manager

This file connection and CRUD operations with the Cosmos DB storing data.

'''

# Module Importations
import azure.cosmos.cosmos_client as client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

# Project Modules
import config

# Constants
HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']
