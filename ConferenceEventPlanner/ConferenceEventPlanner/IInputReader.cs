using System.Collections.Generic;

namespace ConferenceEventPlanner
{
    public interface IInputReader
    {
        List<string> GetEventsData();
    }
}
