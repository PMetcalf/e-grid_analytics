﻿using BmrsDataAcquisition.Services;
using Microsoft.Extensions.Hosting;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;

namespace BmrsDataAcquisition.Business_Logic
{
    public class bmrsWebCallHostedService : IHostedService
    {
        private Timer _timer;

        private AzureWebService azureWebService = new AzureWebService(); 

        public Task StartAsync(CancellationToken cancellationToken)
        {
            // Start webservices
            azureWebService.InitialiseAzureHttpClient();

            _timer = new Timer(BmrsWebCallAsync, null, 0, 86400000
                );   // Interval specified in milliseconds (24 hrs)
            return Task.CompletedTask;
        }

        // This is the routine called by the timer
        async void BmrsWebCallAsync(object state)
        {
            Debug.WriteLine("Making webcall ...");

            // Determine earliest entry in storage
            Tuple<string, string> result = await azureWebService.ReturnEarliestDate();
            
            Debug.WriteLine(result);

            // Calculate date to request data for

            // Iterate over periods for date

                // Request data from BMRS API

                // Convert data to storage format

                // Send converted data to storage
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
            //New Timer does not have a stop. 
            _timer?.Change(Timeout.Infinite, 0);
            return Task.CompletedTask;
        }
    }
}
