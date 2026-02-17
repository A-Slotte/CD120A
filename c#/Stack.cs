static void main(String[] args)
{
    Stack<int> s;
    s = new Stack<int>(100);
    for(int i = 0;i < 6; i++)
    {
        s.push(i);
    }
    for(int i = 0; i < 6; i++)
    {
        Console.WriteLine(s.pop);
    }

}
//Generic stack
public class Stack<Item>
{
    private Item[] a;
    private int n;
    public Stack(int capacity)
    {
        // Skapar lista med N(Capacity) element.
        a = new Object[capacity];
    }
    private void resize(int max)
    {
        Item[] temp = new Object[max];
        for(int i = 0; i < n; i++)
        {
            temp[i] = a[i];
        }
        a = temp;
    }
    public void push(Item item)
    {
        if(n == a.Length)
            resize(2*a.Length);
        a[n++] = item;
    }
    public Item pop()
    {
        Item item = a[--n];
        a[n] = null;
        if(n > 0 && n == a.Length / 4)
        {
            resize(a.Length/2);
        }
        return item;
    }

}