### Sorting Algorithms

Sorting is the process of arranging data in a particular order. Sorting algorithms are used to sort data in a specific way. Here are some of the commonly used sorting algorithms:

#### 1. Insertion Sort
- It is a simple sorting algorithm that works by sorting an array one element at a time.
- It is efficient for small data sets or nearly sorted data sets.
- It has a time complexity of O(n^2).

#### 2. Selection Sort
- It is a simple sorting algorithm that works by selecting the smallest element from the unsorted portion of the array and placing it at the beginning of the array.
- It has a time complexity of O(n^2).

#### 3. Bubble Sort
- It is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- It has a time complexity of O(n^2).

#### 4. Quick Sort
- It is a divide and conquer algorithm that works by partitioning the array into two parts, then sorting the parts independently.
- It has a time complexity of O(n log n) on average, but worst case time complexity can be O(n^2).

#### 5. Merge Sort
- It is a divide and conquer algorithm that works by dividing the array into two parts, sorting the parts independently, and then merging the sorted parts.
- It has a time complexity of O(n log n).

#### 6. Heap Sort
- It is a comparison-based sorting algorithm that works by first building a heap, then repeatedly extracting the largest element and placing it at the end of the array.
- It has a time complexity of O(n log n).

#### 7. Radix Sort
- It is a non-comparison sorting algorithm that works by grouping elements by their digit values and sorting them digit by digit.
- It has a time complexity of O(d(n+k)), where d is the number of digits in the largest number and k is the number of possible digit values.

### Searching Algorithms

Searching is the process of finding a specific element in a collection of data. Here are some of the commonly used searching algorithms:

#### 1. Sequential Search
- It is a simple searching algorithm that works by sequentially checking each element in the collection until a match is found or the end of the collection is reached.
- It has a time complexity of O(n).

#### 2. Index Sequential Search
- It is a searching algorithm that works by dividing the collection into blocks of fixed size and creating an index for each block.
- It has a time complexity of O(log n).

#### 3. Binary Search
- It is a searching algorithm that works by dividing the collection in half at each step and comparing the search element with the middle element of the current sub-collection.
- It has a time complexity of O(log n).

### Hashing and Collision Resolution Techniques

Hashing is a technique used to map data of arbitrary size to data of fixed size. A hash function is used to generate the hash value. Collision resolution techniques are used to handle cases where multiple keys map to the same hash value. Here are some of the commonly used collision resolution techniques:

#### 1. Chaining
- It is a collision resolution technique that works by storing multiple elements with the same hash value in a linked list.
- It has a time complexity of O(1) for average case and O(n) for worst case.

#### 2. Open Addressing
- It is a collision resolution technique that works by finding an empty slot in the hash table to store the element.
- It has a time complexity of O(1) for average case and O(n) for worst case.

#### 3. Double Hashing
- It is a collision resolution technique that works by using a second hash function to find an alternative slot to store the element.
- It has a time complexity of O(1) for average case and O(n) for worst case.