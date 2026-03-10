namespace algoritm_analys;

class Algo_1
{
    public static void Main()
    {
        int[] arr = { 1,1,1,1,1};
        int a = Countpairs(arr);
        Console.WriteLine(a);
        
    }

    public static int Countpairs(int[] sortedarr) {
        int N = sortedarr.Length;
        int pairs = 0;
        int m = 1;
        for (int i = 1; i < N; i++)
        {
            if(sortedarr[i] == sortedarr[i - 1] )
            {
                m++;
                if(i == N - 1)
                {
                    pairs += m * (m-1)/2;
                }
            }
            else
            {
                pairs += m * (m-1)/2;
                m = 1;
            }
        }
        return pairs;
    }
}