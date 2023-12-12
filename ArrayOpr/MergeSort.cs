using System;

class MergeSort{

    public int[] array_2b_sorted;

    public MergeSort(int[] array_2b_sorted){
        Console.WriteLine("MergeSort selected as the sorting algorithm.");
        this.array_2b_sorted = array_2b_sorted;
    }
    public void Sort(int left, int right){
        if (left < right){
            int middle = left + (right - left)/2;
            Sort(left, middle);
            Sort(middle + 1, right);

            Merge(left, middle, right);
        }
    }

    public void Merge(int left, int middle, int right){
        int left_len = middle - left + 1;
        int right_len = right - middle;

        int[] left_arr = new int[left_len];
        int[] right_arr = new int[right_len];

        int i, j;

        for(i = 0; i< left_len; ++i)
            left_arr[i] = array_2b_sorted[left+i];
        for(j = 0; j< right_len; ++j)
            right_arr[j] = array_2b_sorted[middle+1+j];

        i = 0;
        j = 0;

        int k = left;

        while (i < left_len && j < right_len) {
            if (left_arr[i] <= right_arr[j]) {
                array_2b_sorted[k] = left_arr[i];
                i++;
            }
            else {
                array_2b_sorted[k] = right_arr[j];
                j++;
            }
            k++;
        }
 
        while (i < left_len) {
            array_2b_sorted[k] = left_arr[i];
            i++;
            k++;
        }

        while (j < right_len) {
            array_2b_sorted[k] = right_arr[j];
            j++;
            k++;
        }
    }

    public int[] StartSorting(){
        Sort(0,array_2b_sorted.Length - 1);
        return array_2b_sorted;
    }
}