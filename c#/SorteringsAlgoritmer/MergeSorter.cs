using System.Runtime.InteropServices;

public class MergeSorter : IntSorter
{
    public void Sort(int[] a)
    {
        int[] b = new int[a.Length];
        CopyArray(a, b, 0, a.Length - 1);
        SplitArray(a, b, 0, a.Length - 1);
    }
    public void CopyArray(int[] a, int[] b, int lo, int hi )
    {
        for(int i = lo; i < hi; i++)
            b[i] = a[i];
    }
    
    public void SplitArray(int[] a, int[] b, int lo, int hi)
    {
        if(lo < hi)
        {
            int mid = (lo + hi) / 2;
            SplitArray(a, b, lo, mid); // vänster
            SplitArray(a, b, mid + 1, hi); // Höger

            Merge(a, b, lo, mid + 1, hi);
        }
    }
    public void Merge(int[] a, int[] b, int lo, int hi, int mid)
    {
        int i = lo;
        int j = hi;

        for(int k = lo; k <= hi; k++)
        {
            if (i > mid) a[k] = b[j++];
            else if(j > hi) a[k] = b[i++];
            else if(a[i] <= a[j]) a[k] = b[j++];
            else a[k] = b[i++]; 
        }
    }
}