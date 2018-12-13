using System;
using System.Collections.Generic;

namespace ConferenceEventPlanner
{
    public class ConferenceSessionTrack
    {
        public TimeSpan SessionDuration;
        public List<ConferenceEvent> ConferenceEvents;

        public ConferenceSessionTrack(int minutes)
        {
            SessionDuration = new TimeSpan(minutes / 60, minutes % 60, 0);
            ConferenceEvents = new List<ConferenceEvent>();
        }
        
    }
}
