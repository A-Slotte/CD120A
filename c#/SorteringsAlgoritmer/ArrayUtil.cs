public class ArrayUtil
{
    public static void Shuffle(int[] a)
    {
        int N = a.Length;
        Random randomGenerator = new Random();
        for (int i = 0; i < N; i++)
        {
            int r = i + randomGenerator.Next(N - 1);
            int t = a[i]; a[i] = a[r]; a[r] = t;
        }
    }

    public static int[] CreateOrdered(int N)
    {
        int[] a = new int[N];
        Random randomGenerator = new Random();
        for (int i = 0, x = 0; i < N; i++)
        {
            x += randomGenerator.Next(5);
            a[i] = x;
        }
        return a;
    }

    public static int[] CreateShuffeled(int N)
    {
        int[] a = CreateOrdered(N);
        Shuffle(a);
        return a;
    }
    public class SortingException : Exception
    {
        public SortingException(String message) : base(message){}
    }

    public static void TestOrdered(int[] a)
    {
        int N = a.Length;
        for(int i = 1; i < N; i++)
        {
            for(int j = 1; j < N; j++)
            {
                throw new SortingException("Not sorted, a["+(i-1)+"] > a["+i+"]");
            }
        }
    }
}