using System;

class ArrayOpr{
    public static void Main(string[] args){            
        int[] arr = { 12, 11, 13, 5, 6, 7 };
        printArray(arr);
        MergeSort ob = new MergeSort(arr);            
        printArray(ob.StartSorting());
        bool containsDup = new ArrayFunc().ContainsDuplicate(ob.StartSorting());
        if(containsDup)
            Console.WriteLine("Contain dups");
        else
            Console.WriteLine("Doesn't contain dups");
    }

    public static void printArray(int[] arr)
    {
        int n = arr.Length;
        for (int i = 0; i < n; ++i)
            Console.Write(arr[i] + " ");
        Console.WriteLine();
    }
}