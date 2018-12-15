namespace FizzBuzzLibrary
{
    /// <summary>
    /// A way to print to a particular target
    /// </summary>
    public interface IPrinter
    {
        /// <summary>
        /// Prints the message in some local way
        /// </summary>
        /// <param name="message">The string that should be printed</param>
        void Print(string message);
    }
}
