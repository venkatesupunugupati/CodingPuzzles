using System.Collections.Generic;

namespace ConferenceEventPlanner
{
    public class ConferenceTrack
    {
        public int TrackNumber;
        public Dictionary<int, ConferenceSessionTrack> conferenceSessions;

        public ConferenceTrack(int trackNumber)
        {
            TrackNumber = trackNumber;
            conferenceSessions = new Dictionary<int, ConferenceSessionTrack>() {
                { 1, new ConferenceSessionTrack(Constants.MorningBeforeBreakSessionDuration) },
                { 2, new ConferenceSessionTrack(Constants.MorningAfterBreakSessionDuration) },
                { 3, new ConferenceSessionTrack(Constants.EveningBeforeBreakSessionDuration) },
                { 4, new ConferenceSessionTrack(Constants.EveningAfterBreakSessionDuration) }
            };
        }

    }
}
