using System;
using System.Collections.Generic;

class Balance {
    public static void Main() { 
        string s = Console.ReadLine();          
        if(!checkBalance(s))
            Console.WriteLine(0);
        else
            Console.WriteLine(1);
    }
    public static bool checkBalance(String s)
    {
        Stack<char> stack = new Stack<char>();
        int leftCount = 0;
        int rightCount = 0;

        foreach (var c in s)
        {
            if(c == '(' || c == '[')
            {   
                leftCount +=  1;
                stack.Push(c);
            }
            else if(c == ')' || c == ']')
            {
                rightCount += 1;
                if (stack.Count == 0)
                    return false;
                char left = stack.Pop();
                if (!matches(left, c))
                    return false;
            }
        }
        if(rightCount != leftCount)
            return false;
        return true;
    }
    public static bool matches(char left, char right)
    {
        if(left == '(' && right == ')' || left == '[' && right == ']')
            return true;
        else
            return false;
    }


}