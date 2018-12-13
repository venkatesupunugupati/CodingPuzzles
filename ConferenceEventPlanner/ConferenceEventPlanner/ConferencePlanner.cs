using System;
using System.Collections.Generic;
using System.Text;

namespace ConferenceEventPlanner
{
    /// <summary>
    /// This is for generating conference plan by reading input as per the given input reader 
    /// and scheduling events as per the given scheduling algorithem. It also generates output plan as per the given output writer. 
    /// </summary>
    public class ConferencePlanner
    {
        private readonly IInputReader _inputReader;
        private readonly IConferenceScheduler _conferenceScheduler;
        private readonly IOutputWriter _outputWriter;

        public ConferencePlanner(IInputReader inputReader, IConferenceScheduler conferenceScheduler, IOutputWriter outputWriter)
        {
            this._inputReader = inputReader;
            this._conferenceScheduler = conferenceScheduler;
            this._outputWriter = outputWriter;
        }

        private string BuildSessionPlan(List<ConferenceEvent> conferenceEvents, string sessionStartTime, bool isItMorning)
        {
            StringBuilder stringBuilder = new StringBuilder();
            TimeSpan startTime = TimeSpan.Parse(sessionStartTime);
            foreach (ConferenceEvent conferenceEvent in conferenceEvents)
            {
                string fromTime = startTime.ToString("hh':'mm");
                stringBuilder.AppendLine(fromTime + (isItMorning ? "AM " : "PM ") + conferenceEvent.Topic);
                startTime = TimeSpan.FromMinutes(startTime.TotalMinutes + conferenceEvent.Duration);
            }
            return stringBuilder.ToString();
        }

        private StringBuilder BuildConferencePlan(Conference conference)
        {
            StringBuilder stringBuilder = new StringBuilder();
            foreach (ConferenceTrack conferenceTrack in conference.ConferenceTracks)
            {
                stringBuilder.AppendLine("Track " + conferenceTrack.TrackNumber.ToString() + ":");
                stringBuilder.AppendLine();
                stringBuilder.Append(BuildSessionPlan(conferenceTrack.conferenceSessions[1].ConferenceEvents, Constants.MorningBeforeBreakSessionStartTime, true));
                stringBuilder.AppendLine(Constants.MorningBreak);
                stringBuilder.Append(BuildSessionPlan(conferenceTrack.conferenceSessions[2].ConferenceEvents, Constants.MorningAfterBreakSessionStartTime, true));
                stringBuilder.AppendLine(Constants.LunchBreak);
                stringBuilder.Append(BuildSessionPlan(conferenceTrack.conferenceSessions[3].ConferenceEvents, Constants.EveningBeforeBreakSessionStartTime, false));
                stringBuilder.AppendLine(Constants.EveningBreak);
                stringBuilder.Append(BuildSessionPlan(conferenceTrack.conferenceSessions[4].ConferenceEvents, Constants.EveningAfterBreakSessionStartTime, false));
                stringBuilder.AppendLine(Constants.Network);
                stringBuilder.AppendLine();
            }
            return stringBuilder;
        }

        private List<ConferenceEvent> BuildConferenceEvents(List<string> eventsData)
        {
            List<ConferenceEvent> conferenceEvents = new List<ConferenceEvent>();
            foreach (string eventData in eventsData)
            {
                conferenceEvents.Add(new ConferenceEvent(eventData));
            }
            return conferenceEvents;
        }

        public void GenerateConferencePlan()
        {
            IInputReader inputReader = new FileInputReader();
            List<string> eventsData = inputReader.GetEventsData();
            if (eventsData.Count > 0)
            {
                List<ConferenceEvent> conferenceEvents = BuildConferenceEvents(eventsData);

                //Schedule conference events for tracking sessions
                Conference conference = _conferenceScheduler.ScheduleConference(conferenceEvents);

                //Build Plan output including non tracking sessions
                StringBuilder stringBuilder = BuildConferencePlan(conference);

                _outputWriter.Write(stringBuilder.ToString());
            }
        }
    }
}
