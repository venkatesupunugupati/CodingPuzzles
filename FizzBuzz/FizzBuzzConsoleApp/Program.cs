using FizzBuzzLibrary;
using System;
using System.Collections.Generic;

namespace FizzBuzzConsoleApp
{
    internal class ConsolePrinter : IPrinter
    {
        public void Print(string message)
        {
            Console.WriteLine(message);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {            
            var rules = new List<IRule>
            {
                FizzBuzzRules.FizzRule,
                FizzBuzzRules.BuzzRule
            };
            FizzBuzz fizzBuzz = new FizzBuzz();
            fizzBuzz.ExecuteFizzBuzz(1, 100, rules, new ConsolePrinter());
            Console.ReadKey();
        }
    }
}
