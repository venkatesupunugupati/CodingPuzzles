using System.Collections.Generic;

namespace ConferenceEventPlanner
{
    public interface IConferenceScheduler
    {
        Conference ScheduleConference(List<ConferenceEvent> conferenceEvents);
    }
}