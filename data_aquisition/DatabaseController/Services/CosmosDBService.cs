﻿using Microsoft.Azure.Cosmos;
using DatabaseController.Models;
using System.Threading.Tasks;

namespace DatabaseController.Services
{
    /// <summary>
    /// Connect and use Azure Cosmos DB, including CRUD operations.
    /// </summary>

    public class CosmosDBService : ICosmosDbService
    {
        private Container container;

        /// <summary>
        /// Use client to connect database connection in container.
        /// </summary>
        /// <param name="dbClient"></param>
        /// <param name="dbName"></param>
        /// <param name="containerName"></param>
        public CosmosDBService(CosmosClient dbClient, string dbName, string containerName)
        {
            this.container = dbClient.GetContainer(dbName, containerName);
        }

        /// <summary>
        /// Add data item to container.
        /// </summary>
        /// <returns></returns>
        public async Task AddDataAsync(B1620_data_model data)
        {
            await this.container.CreateItemAsync<B1620_data_model>(data, new PartitionKey(data.Id));
        }

        /// <summary>
        /// Retreives data item from container.
        /// </summary>
        /// <returns></returns>
        public async Task<B1620_data_model> GetDataAsync(string id)
        {
            try
            {
                ItemResponse<B1620_data_model> response = await this.container.ReadItemAsync<B1620_data_model>(id, new PartitionKey(id));

                return response.Resource;
            }
            catch
            {
                return null;
            }
        }

        /// <summary>
        /// Retreives earliest data item from container.
        /// </summary>
        /// <returns></returns>
        public async Task<B1620_data_model> GetEarliestDataAsync()
        {
            // sql query for returning top value
            //string sqlquery = "SELECT TOP 1 * FROM c ORDER BY c.id";

            try
            {
                // Create iterator using sql query
                QueryDefinition queryDefinition = new QueryDefinition("SELECT TOP 1 * FROM c ORDER BY c.id");

                using FeedIterator<B1620_data_model> feedIterator = this.container.GetItemQueryIterator<B1620_data_model>(
                    queryDefinition,
                    null,
                    null);

                while (feedIterator.HasMoreResults)
                {
                    foreach (var item in await feedIterator.ReadNextAsync())
                    {
                        B1620_data_model data = item;

                        return data;
                    }
                }
            }
            catch
            {
                return null;
            }
        }
    }
}
