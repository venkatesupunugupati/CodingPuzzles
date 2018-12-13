using System;
using System.Collections.Generic;
using System.Linq;

namespace ConferenceEventPlanner
{
    public class BestFitDecreasingScheduler : IConferenceScheduler
    {
        private int FindFitWithLeastDurationAvaliableSession(ConferenceTrack conferenceTrack, int eventDuration)
        {
            int sessionNumber = 0;
            double leastDuration = 0;
            foreach (KeyValuePair<int, ConferenceSessionTrack> conferenceSession in conferenceTrack.conferenceSessions)
            {
                if(conferenceSession.Value.SessionDuration.TotalMinutes >= eventDuration)
                {
                    if(leastDuration == 0)
                    {
                        leastDuration = conferenceSession.Value.SessionDuration.TotalMinutes;
                        sessionNumber = conferenceSession.Key;
                    }
                    else
                    {
                        if (leastDuration > conferenceSession.Value.SessionDuration.TotalMinutes)
                        {
                            leastDuration = conferenceSession.Value.SessionDuration.TotalMinutes;
                            sessionNumber = conferenceSession.Key;
                        }
                    }                    
                                      
                }
            }
            return sessionNumber;
        }

        public Conference ScheduleConference(List<ConferenceEvent> conferenceEvents)
        {
            //sorting conference events
            conferenceEvents = conferenceEvents.OrderBy(o => o.Duration).ToList();

            Conference conference = new Conference();
            int conferenceTrackNum = 0;
            while (conferenceEvents.Count > 0)
            {
                ConferenceTrack conferenceTrack = new ConferenceTrack(++conferenceTrackNum);

                for (int i = conferenceEvents.Count-1;i >= 0; i--)
                {
                    int sessonNumber = FindFitWithLeastDurationAvaliableSession(conferenceTrack, conferenceEvents[i].Duration);
                    if(sessonNumber != 0)
                    {
                        conferenceTrack.conferenceSessions[sessonNumber].ConferenceEvents.Add(conferenceEvents[i]);
                        conferenceTrack.conferenceSessions[sessonNumber].SessionDuration -= new TimeSpan(conferenceEvents[i].Duration/60, conferenceEvents[i].Duration%60,0);
                        conferenceEvents.RemoveAt(i);
                    }
                }
                conference.ConferenceTracks.Add(conferenceTrack);

            }
            return conference;
        }
    }
}
