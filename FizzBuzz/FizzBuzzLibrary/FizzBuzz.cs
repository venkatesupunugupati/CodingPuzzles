using System.Collections.Generic;

namespace FizzBuzzLibrary
{
    /// <summary>
    /// Printing FizzBuzz logic
    /// </summary>
    public class FizzBuzz
    {
        /// <summary>
        /// Prints a message depending on a rule set going over a number range
        /// </summary>
        /// <param name="start">The beginning number</param>
        /// <param name="end">The ending number</param>
        /// <param name="rules">The rules that determine what gets printed</param>
        /// <param name="printer">The local way to print from the client</param>
        public void ExecuteFizzBuzz(int start, int end, IEnumerable<IRule> rules, IPrinter printer)
        {
            for (int i = start; i <= end; i++)
            {
                string result = string.Empty;
                if (rules != null)
                {
                    foreach (var rule in rules)
                    {                        
                        if (rule.IsPass(i))
                        {
                            result += rule.Message;                            
                        }
                    }
                }
                if(string.IsNullOrEmpty(result))
                {
                    result = i.ToString();
                }
                printer.Print(result);
            }
        }
    }
}
