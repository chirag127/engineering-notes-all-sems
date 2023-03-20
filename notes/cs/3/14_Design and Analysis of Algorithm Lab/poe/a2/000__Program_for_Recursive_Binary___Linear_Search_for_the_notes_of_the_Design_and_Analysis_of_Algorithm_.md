 Here is the content in markdown format without any emojis or external links and in a formal tone:

## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System:

1. Binary Search:
- Binary search is a searching algorithm that works on sorted arrays.
- It compares the middle element with the key. If the middle element matches with the key, it returns the mid index.
- If the middle element is greater than the key, it searches the left half. Else it searches the right half.
- This process continues on the subarray containing the key till the key is found.
- If the subarray length reduces to 0 then the key is not present.

Algorithm:
binarySearch(arr, l, r, x) {
    if (r >= l) {
        mid = l + (r - l) / 2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}

2. Linear Search:
- Linear search simply iterates over the list and checks if each element matches the key.
- If a match is found, the index of that element is returned.
- If the list is traversed without a match, -1 is returned.

Algorithm:
linearSearch(arr, n, x) {
    for (i = 0; i < n; i++)
        if (arr[i] == x)
            return i;
    return -1;
}