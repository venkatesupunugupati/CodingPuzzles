using System.Text.RegularExpressions;

namespace ConferenceEventPlanner
{
    public class ConferenceEvent
    {
        public string Topic;
        public int Duration;

        public ConferenceEvent(string eventData)
        {
            string eventDuration = Regex.Match(eventData, @"\d+").Value;
            if (!string.IsNullOrEmpty(eventDuration))
            {
                Duration = int.Parse(eventDuration);
                Topic = eventData;
            }
            else
            {
                if ((eventData.ToLower().Contains("vignette") || eventData.ToUpper().Contains("VIGNETTE")))
                    Topic = eventData;
                Duration = 5;
            }
        }
       
    }
}
