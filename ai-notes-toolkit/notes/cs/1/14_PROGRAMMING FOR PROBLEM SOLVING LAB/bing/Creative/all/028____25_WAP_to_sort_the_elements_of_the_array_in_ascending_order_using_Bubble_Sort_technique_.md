## 25.WAP to sort the elements of the array in ascending order using Bubble Sort technique.

- Bubble sort is a simple sorting algorithm that compares adjacent elements of an array and swaps them if they are in the wrong order.
- The algorithm repeats this process until the array is sorted.
- The algorithm gets its name from the way smaller or larger elements "bubble" to the top of the array.
- The pseudocode for bubble sort is:

```
procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped := false
        for i := 1 to n-1 inclusive do
            /* if this pair is out of order */
            if A[i-1] > A[i] then
                /* swap them and remember something changed */
                swap(A[i-1], A[i])
                swapped := true
            end if
        end for
    until not swapped
end procedure
```

- The time complexity of bubble sort is O(n^2) in the worst case, when the array is in reverse order.
- The space complexity of bubble sort is O(1), as it only requires a constant amount of auxiliary space.
- Bubble sort is stable, meaning that it preserves the relative order of equal elements in the array.
- Bubble sort is adaptive, meaning that it can perform better if the array is already partially sorted.