namespace FizzBuzzLibrary
{
    /// <summary>
    /// A rule used to determine whether to print or not and the message to show if it should print
    /// </summary>
    public interface IRule
    {
        /// <summary>
        /// Determines whether a number passed the rule
        /// </summary>
        /// <param name="num">The number to evaluate</param>
        /// <returns>pass or not</returns>
        bool IsPass(int num);

        /// <summary>
        /// The string used instead of number if the rule passes
        /// </summary>
        string Message { get; }
    }
}
