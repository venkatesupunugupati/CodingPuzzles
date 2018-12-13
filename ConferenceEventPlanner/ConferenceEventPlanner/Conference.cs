using System.Collections.Generic;

namespace ConferenceEventPlanner
{
    public class Conference
    {
        public List<ConferenceTrack> ConferenceTracks;

        public Conference()
        {
            ConferenceTracks = new List<ConferenceTrack>();
        }
    }
}
