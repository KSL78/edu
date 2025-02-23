using System;
using System.Collections.Generic;

public class G1011
{
    public static void Main(string[] args)
    {
        int T = int.Parse(Console.ReadLine());
        List<int> results = new List<int>();

        for (int i = 0; i < T; i++)
        {
            string[] inputs = Console.ReadLine().Split();
            int x = int.Parse(inputs[0]);
            int y = int.Parse(inputs[1]);
            results.Add(CalculateMinJumps(x, y));
        }

        foreach (var result in results)
        {
            Console.WriteLine(result);
        }
    }

    public static int CalculateMinJumps(int x, int y)
    {
        int distance = y - x;
        int steps = 0;
        int total = 0;

        while (total < distance)
        {
            steps++;
            total += steps / 2;
            if (total >= distance) break;
        }

        return steps-1;
    }
}
