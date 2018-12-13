using System.Collections.Generic;
using System.Linq;

namespace ConferenceEventPlanner
{
    public class FirstFitDecreasingScheduler : IConferenceScheduler
    {
        private List<ConferenceEvent> ScheduleConferenceSession(List<ConferenceEvent> conferenceEvents, double sessionTime)
        {
            List<ConferenceEvent> sessionEvents = new List<ConferenceEvent>();
            for (int i = conferenceEvents.Count - 1; i >= 0; i--)
            {
                if (sessionTime >= double.Parse(conferenceEvents[i].Duration.ToString()))
                {
                    sessionEvents.Add(conferenceEvents[i]);
                    sessionTime = sessionTime - double.Parse(conferenceEvents[i].Duration.ToString());
                    conferenceEvents.RemoveAt(i);
                    if (sessionTime == 0)
                    {
                        break;
                    }
                }
            }
            return sessionEvents;
        }

        public Conference ScheduleConference(List<ConferenceEvent> conferenceEvents)
        {
            //sort events
            conferenceEvents = conferenceEvents.OrderBy(o => o.Duration).ToList();

            Conference conference = new Conference();
            int conferenceTrackNum = 0;
            while (conferenceEvents.Count > 0)
            {
                ConferenceTrack conferenceTrack = new ConferenceTrack(++conferenceTrackNum);

                foreach (KeyValuePair<int, ConferenceSessionTrack> conferenceSession in conferenceTrack.conferenceSessions)
                {
                    List<ConferenceEvent> sessionEvents = ScheduleConferenceSession(conferenceEvents, conferenceSession.Value.SessionDuration.TotalMinutes);
                    conferenceSession.Value.ConferenceEvents.AddRange(sessionEvents);
                }

                conference.ConferenceTracks.Add(conferenceTrack);

            }

            return conference;
        }
    }
}
