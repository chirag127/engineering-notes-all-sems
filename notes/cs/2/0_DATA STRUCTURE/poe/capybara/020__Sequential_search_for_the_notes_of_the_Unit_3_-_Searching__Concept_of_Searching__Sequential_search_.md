### Sequential Search

Sequential search is a simple searching algorithm that examines each element in a list or an array in order until the desired element is found. It is also known as linear search. The algorithm starts at the beginning of the list and compares each element with the desired value until a match is found. Sequential search is easy to implement but it is not efficient for large data sets.

#### Steps for Sequential Search

1. Start at the beginning of the list.
2. Compare the first element with the desired element.
3. If they match, return the index of the element.
4. If they do not match, move to the next element and repeat step 2 and 3 until the end of the list is reached.
5. If the end of the list is reached and the desired element is not found, return -1.

#### Time Complexity

The time complexity of sequential search is O(n), where n is the number of elements in the list. This means that the worst-case scenario is when the desired element is at the end of the list, and the algorithm has to compare each element before finding it.

#### Advantages

- Easy to implement
- Works for unsorted lists

#### Disadvantages

- Not efficient for large data sets
- Time complexity is O(n)

#### Applications

Sequential search is often used in small data sets or when the data is not sorted. It is also used as a subroutine in other algorithms.

### Hashing & Collision Resolution Techniques

Hashing is a technique used to map data of arbitrary size to a fixed size. A hash function is used to generate a unique key for each data element. Collision resolution techniques are used to handle collisions that occur when two elements have the same hash value.

#### Hash Function

A hash function takes an input value and generates a fixed-size output value. The output value is used as the key for the data element. A good hash function should distribute the keys uniformly across the hash table to minimize collisions.

#### Collision Resolution Techniques

There are several collision resolution techniques that can be used to handle collisions:

1. **Chaining**: In chaining, each slot in the hash table contains a linked list of the data elements that hash to that slot. When a collision occurs, the new element is added to the end of the linked list.
2. **Open Addressing**: In open addressing, when a collision occurs, the algorithm searches for the next available slot in the hash table until an empty slot is found. There are several techniques for finding the next available slot, such as linear probing, quadratic probing, and double hashing.

#### Advantages

- Efficient for large data sets
- Time complexity is O(1) in the average case

#### Disadvantages

- Requires a good hash function
- Collision resolution can be complex

#### Applications

Hashing is used in many applications, such as databases, compilers, and cryptography.

### Sorting Algorithms

Sorting is the process of arranging data in a specific order. There are many sorting algorithms, each with its own strengths and weaknesses. Here are some of the most commonly used sorting algorithms:

#### Insertion Sort

Insertion sort is a simple sorting algorithm that works by comparing each element with the elements before it and inserting it in the correct position. It is efficient for small data sets but becomes slow for large data sets.

#### Selection Sort

Selection sort is a sorting algorithm that works by selecting the smallest element in the unsorted portion of the list and swapping it with the first element in the unsorted portion. It is simple to implement but not efficient for large data sets.

#### Bubble Sort

Bubble sort is a sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order. It is simple to implement but not efficient for large data sets.

#### Quick Sort

Quick sort is a sorting algorithm that works by partitioning the list into two sublists, one with elements less than a pivot element and one with elements greater than the pivot element. The algorithm then recursively sorts the sublists. It is efficient for large data sets but can be slow in the worst-case scenario.

#### Merge Sort

Merge sort is a sorting algorithm that works by dividing the list into two halves, recursively sorting the halves, and then merging the sorted halves. It is efficient for large data sets but requires additional memory.

#### Heap Sort

Heap sort is a sorting algorithm that works by building a binary heap from the list and repeatedly extracting the maximum element from the heap and placing it at the end of the list. It is efficient for large data sets but requires additional memory.

#### Radix Sort

Radix sort is a sorting algorithm that works by sorting the elements based on their digits. It is efficient for large data sets with small digits but requires additional memory.

#### Time Complexity

The time complexity of sorting algorithms varies depending on the algorithm and the data set. Some algorithms have a time complexity of O(n^2) in the worst-case scenario, while others have a time complexity of O(n log n) in the average case.

#### Advantages

-