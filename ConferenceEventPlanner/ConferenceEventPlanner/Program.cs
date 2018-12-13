using System;

namespace ConferenceEventPlanner
{
    class Program
    {
        static void Main(string[] args)
        {
            //ConferencePlanner conferencePlanner = new ConferencePlanner(new FileInputReader(), new FirstFitDecreasingScheduler(), new FileOutputWriter());
            ConferencePlanner conferencePlanner = new ConferencePlanner(new FileInputReader(),new BestFitDecreasingScheduler(), new FileOutputWriter());
            conferencePlanner.GenerateConferencePlan();
            Console.ReadLine();

        }
    }
}
