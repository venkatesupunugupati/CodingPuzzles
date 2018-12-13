using System;

namespace ConferenceEventPlanner
{
    public class FileOutputWriter : IOutputWriter
    {
        public void Write(string conferencePlan)
        {
            using (System.IO.StreamWriter file = new System.IO.StreamWriter(Constants.outputFileName))
            {
                file.Write(conferencePlan);
                Console.WriteLine("\nTest Output:\n");
                Console.Write(conferencePlan);
            }
            Console.WriteLine("Conference Plan written to File Successfully");
        }
    }
}
