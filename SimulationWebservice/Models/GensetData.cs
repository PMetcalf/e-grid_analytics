﻿using Newtonsoft.Json;
using System;

namespace SimulationWebservice.Models
{
    /// <summary>
    /// Contains data model for genset system.
    /// </summary>

    public class GensetData
    {
        /// <summary>
        /// Id is used to identify data storage element.
        /// </summary>
        [JsonProperty(PropertyName = "id")]
        public string Id { get; set; }

        /// <summary>
        /// IsOn identifies if genset is running.
        /// </summary>
        [JsonProperty(PropertyName = "isOn")]
        public bool IsOn { get; set; }

        /// <summary>
        /// GensetPower describes output power in kWe.
        /// </summary>
        [JsonProperty(PropertyName = "gensetPower")]
        public int GensetPower { get; set; }

        /// <summary>
        /// Generates data Id stamp based on genset S/N and datetime.
        /// </summary>
        /// <returns></returns>
        public string GenerateIdStamp()
        {
            string idStamp = null;

            string gensetSN = "Genset_SN_001";

            // Retrieve datetime.
            string time = DateTime.Now.ToString("yyyy-MM-dd-HH:mm:ss");

            // Build dataset Id.
            idStamp = gensetSN + "_" + time;

            // Return Id.
            return idStamp;
        }
    }
}
