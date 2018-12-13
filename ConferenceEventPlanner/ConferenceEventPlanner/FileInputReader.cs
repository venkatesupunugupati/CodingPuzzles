using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;

namespace ConferenceEventPlanner
{
    public class FileInputReader : IInputReader
    {
        public List<string> GetEventsData()
        {
            List<string> eventsData = new List<string>();
            try
            {               
                if (File.Exists(Constants.inputFileName))
                {                    
                    eventsData = File.ReadAllLines(Constants.inputFileName).ToList();
                    Console.WriteLine("\nTest Input:\n");
                    Console.WriteLine(File.ReadAllText(Constants.inputFileName));                    
                }
                else
                {
                    Console.WriteLine("Input File Doesn't exist");
                }
                
            }            
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            return eventsData;
        }
    }
}
