 Here are the notes for the topic - Sorting and Order Statistics - Merge Sort:

### Merge Sort

- Merge sort is a recursive algorithm that uses the divide and conquer technique to solve the sorting problem.
- It divides the input array into two halves, calls itself for the two halves and then merges the two sorted halves.
- The merge() function is used for merging two halves.
- Time complexity: O(n log n) as the array is divided into halves in each recursive call. The merging of two sorted arrays takes O(n) time.
- Space complexity: O(n) as an additional array of size n is needed for merging the two halves.
- Stable: Yes, merge sort preserves the relative order of elements with equal keys.
- Online: No, merge sort requires additional space proportional to the input.
- Example:

    ```
    mergeSort(arr, l, r)
        if(l < r)
            mid = (l + r) / 2;
            mergeSort(arr, l, mid);
            mergeSort(arr, mid + 1, r);
            merge(arr, l, mid, r);
    ```

    void merge(int arr[], int l, int m, int r)
    {
        int i, j, k;
        int n1 = m - l + 1;
        int n2 = r - m;
        int L[n1], R[n2];

        /* Copy data to temporary arrays L[] and R[] */
        for (i = 0; i < n1; i++)
            L[i] = arr[l + i];
        for (j = 0; j < n2; j++)
            R[j] = arr[m + 1 + j];

        /* Merge the temporary arrays back into arr[l..r]*/
        i = 0;
        j = 0;
        k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        /* Copy the remaining elements of L[], if there
        are any */
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        /* Copy the remaining elements of R[], if there
        are any */
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
    ```