## 24. WAP to search an element in an array using Linear Search

### Introduction

Linear search is a simple searching algorithm that searches for an element in an array by sequentially checking each element of the array until it finds the target element. It is also known as a sequential search. This algorithm is easy to understand and implement, but it can be slow for large arrays.

### Algorithm

1. Start the linear search from the first element of the array.
2. Compare the target element with the current element of the array.
3. If the target element is found, return the index of the element.
4. If the target element is not found, move to the next element of the array.
5. Repeat steps 2 to 4 until the target element is found or the end of the array is reached.

### Pseudocode

```
function linearSearch(array, target) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === target) {
            return i;
        }
    }
    return -1;
}
```

### Time Complexity

The time complexity of linear search is O(n), where n is the number of elements in the array. This means that the time taken to search for an element in an array increases linearly with the size of the array.

### Example

Let's say we have an array of integers: [4, 6, 7, 2, 9, 1, 5]. We want to search for the element 9.

```
linearSearch([4, 6, 7, 2, 9, 1, 5], 9);
```

The linear search algorithm will start from the first element of the array, which is 4. It will compare 4 with 9 and move to the next element. It will continue this process until it finds the target element, which is 9. The function will return the index of the element, which is 4.

### Conclusion

Linear search is a simple algorithm that can be used to search for an element in an array. It is easy to understand and implement, but it can be slow for large arrays. There are other searching algorithms like binary search that have a better time complexity for large arrays, but they require the array to be sorted.