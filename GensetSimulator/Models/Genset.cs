﻿using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;
using System.Threading.Tasks;

namespace GensetSimulator.Models
{
    /// <summary>
    /// Genset class holds properties and methods for a genset.
    /// </summary>

    class Genset
    {
        /// <summary>
        /// Bool determines if genset is running.
        /// </summary>
        private bool isOn;
        public bool IsOn { get => isOn; set => isOn = value; }

        /// <summary>
        /// Property stores genset generated power.
        /// </summary>
        private int gensetPower;
        public int GensetPower { get => gensetPower; set => gensetPower = value; }

        /// <summary>
        /// Constructor alerts user and sets properties.
        /// </summary>
        public Genset()
        {
            Console.WriteLine("Genset Created.");

            // Initialise genset properties.
            IsOn = false;
            GensetPower = 0;
        }


        /// <summary>
        /// Generates random values for properties for a pescribed count.
        /// </summary>
        public void RunGenset(int runCycles)
        {
            IsOn = true;
            Console.WriteLine("Starting Genset.");

            // Run genset for prescribed count.
            for (int cycle = 0; cycle < runCycles; cycle++)
            {
                // Generate values for properties.
                GensetPower = GenerateRandomNumber(990, 1010);

                // Print values (Replace with data export).
                Console.WriteLine("Power Output: " + GensetPower.ToString() + "kW");

                // Wait (simulated) time.
                Task.Delay(2000).Wait();
            }
        }

        /// <summary>
        /// Stop generating values for properties.
        /// </summary>
        private void StopGenset()
        {

        }

        /// <summary>
        /// Generates random number of value greater than min / less than max.
        /// </summary>
        /// <param name="min"></param>
        /// <param name="max"></param>
        private int GenerateRandomNumber(int min, int max)
        {
            if (min < 0)
            {
                min = 0;
            }

            if (max < 0)
            {
                max = 0;
            }

            // Generate number.
            Random random = new Random();
            int number = random.Next(min, max);

            // Return number.
            return number;
        }
    }
}
