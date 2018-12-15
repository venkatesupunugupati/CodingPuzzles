
namespace FizzBuzzLibrary
{
    /// <summary>
    /// A set of pre-defined rules
    /// </summary>
    public static class FizzBuzzRules
    {
        /// <summary>
        /// if the number is divisible by 3 with out remainder then mesage is "FIZZ"
        /// </summary>
        public static readonly IRule FizzRule = new ModRule(3, "FIZZ");

        /// <summary>
        /// if the number is divisible by 5 with out remainder then message is "BUZZ"
        /// </summary>
        public static readonly IRule BuzzRule = new ModRule(5, "BUZZ");
       
    }
}
