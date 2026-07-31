### Sorting and Order Statistics - Merge Sort

Merge Sort is a popular sorting algorithm that uses the divide-and-conquer approach to sort an array or a list of elements. It is a comparison-based algorithm that has a time complexity of O(n log n), where n is the number of elements to be sorted.

#### How does Merge Sort work?
1. Divide the array into two halves and recursively sort each half.
2. Merge the two sorted halves to get the final sorted array.

#### Algorithm
```
mergeSort(arr[], l, r)
if l < r
    middle = l + (r-l)/2
    mergeSort(arr, l, middle)
    mergeSort(arr, middle+1, r)
    merge(arr, l, middle, r)
    
merge(arr[], l, middle, r)
n1 = middle - l + 1
n2 = r - middle
left[] and right[] are temporary arrays
for i in range 0 to n1-1
    left[i] = arr[l+i]
for j in range 0 to n2-1
    right[j] = arr[middle+1+j]
i = 0, j = 0, k = l
while i < n1 and j < n2
    if left[i] <= right[j]
        arr[k] = left[i]
        i = i+1
    else
        arr[k] = right[j]
        j = j+1
    k = k+1
while i < n1
    arr[k] = left[i]
    i = i+1
    k = k+1
while j < n2
    arr[k] = right[j]
    j = j+1
    k = k+1
```

#### Advantages of Merge Sort
- Merge Sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the sorted array.
- It has a guaranteed worst-case time complexity of O(n log n).
- It is a good choice for sorting large data sets as it has a space complexity of O(n).

#### Disadvantages of Merge Sort
- Merge Sort has a higher space complexity than other sorting algorithms, as it requires additional memory to store the temporary arrays during the sorting process.
- It has a higher constant factor than other sorting algorithms, making it slower for small data sets.

#### Conclusion
Merge Sort is a popular and efficient sorting algorithm that uses the divide-and-conquer approach to sort an array or a list of elements. It has a worst-case time complexity of O(n log n), making it a good choice for sorting large data sets. However, it may not be the best choice for small data sets due to its higher constant factor and space complexity.