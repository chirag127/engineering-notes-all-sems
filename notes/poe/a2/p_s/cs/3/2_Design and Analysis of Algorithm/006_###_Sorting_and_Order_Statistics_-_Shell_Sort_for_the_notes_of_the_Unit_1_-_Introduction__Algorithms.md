 Here are the notes for ### Sorting and Order Statistics - Shell Sort for the Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time. in the subject of Design and Analysis of Algorithm:

### Shell Sort
- Shellsort is a generalization of insertion sort. It is also known as diminishing increment sort.
- In shellsort, we make the array h-sorted for a large value of h. Then we reduce the value of h and then the array is h-sorted again. This repeats until h becomes 1, at which point the array is sorted.
- The array is h-sorted means that all sublists of every hth element is sorted.
- This allows shellsort to work efficiently even for larger increments, and the efficiency improves as h decreases.
- The time complexity of shellsort is O(nlogn) in the best case and O(n2) in the worst case.

**Algorithm:**

sort(arr[], n)
{
   // Start with a bigger gap, then reduce the gap
   for (gap = n/2; gap > 0; gap /= 2)
   {
       // Do a gapped insertion sort for this gap size. 
       // The first gap elements a[0..gap-1] are already in gapped order keep adding one more element until the entire array is gap sorted
       for (i = gap; i < n; i++)
       {
           // add a[i] to the elements that have been gap sorted save a[i] in temp and make a hole at position i
           temp = arr[i]
 
           // shift earlier gap-sorted elements up until the correct location for a[i] is found
           for (j = i - gap; j >= 0 && arr[j] > temp; j -= gap)
               arr[j + gap] = arr[j]
 
           //put temp (the original a[i]) in its correct location
           arr[j + gap] = temp
       }
   }
}

- The time complexity can be brought down to O(nlogn) by choosing the gaps in a clever manner. One popular sequence is: n/2, n/4, n/8, ...
- The code can be optimized by stopping the inner loop as soon as a[j + gap] becomes greater than temp.
- Shellsort is not a stable sort. The relative order of elements with equal values may change.
- The main advantage of shellsort is that it is faster than other simple sorting algorithms for larger input sizes.