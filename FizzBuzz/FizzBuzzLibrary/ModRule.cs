namespace FizzBuzzLibrary
{
    /// <summary>
    /// This is the Mod Rule, if pass respective message will be given
    /// </summary>
    public class ModRule : IRule
    {
        private readonly int modVal;
        private readonly string message;

        /// <summary>
        /// Constructs this type of rule
        /// </summary>
        /// <param name="modVal">The value to check evenly divisible</param>
        /// <param name="message">The message to display if the number is evenly divisible</param>
        public ModRule(int modVal, string message)
        {
            this.modVal = modVal;
            this.message = message;
        }

        public bool IsPass(int num)
        {
            return num % modVal == 0;
        }

        public string Message
        {
            get { return message; }
        }
    }
}
