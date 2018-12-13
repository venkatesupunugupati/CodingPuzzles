namespace ConferenceEventPlanner
{
    class Constants
    {
        //All times in minutes
        public const int MorningBeforeBreakSessionDuration = 165;
        public const int MorningAfterBreakSessionDuration = 60;
        public const int EveningBeforeBreakSessionDuration = 90;
        public const int EveningAfterBreakSessionDuration = 75;
        public const int NetworkEventDuration = 120;
        public const int BreakDuration = 15;
        public const int LunchDuration = 60;

        public const string MorningBeforeBreakSessionStartTime = "8:0:0";
        public const string MorningAfterBreakSessionStartTime = "11:0:0";
        public const string EveningBeforeBreakSessionStartTime = "1:0:0";
        public const string EveningAfterBreakSessionStartTime = "2:45:0";

        public const string MorningBreak = "10:45AM Break(15 min)";
        public const string EveningBreak = "02:30PM Break (15 min)";
        public const string LunchBreak = "12:00PM Noon Lunch (60 min)";
        public const string Network = "04:00PM Poster Session and Networking Event (120 min)";
        public const string inputFileName = "Input.txt";
        public const string outputFileName = "ConferencePlan.txt";


    }
}
