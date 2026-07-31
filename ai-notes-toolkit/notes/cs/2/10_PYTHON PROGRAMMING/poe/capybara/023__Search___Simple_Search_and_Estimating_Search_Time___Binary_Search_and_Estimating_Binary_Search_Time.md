### Search: Simple Search and Estimating Search Time, Binary Search and Estimating Binary Search Time

In the unit 5 of Python Programming, we will learn about iterators and recursion. As a part of this unit, we will also cover two important searching algorithms - Simple Search and Binary Search.

#### Simple Search

Simple Search is also known as Linear Search. It is a basic searching algorithm that checks each element of the list until it finds the desired element. The steps involved in Simple Search are:

- Start from the first element of the list.
- Compare each element with the desired element.
- If the element is found, return its index.
- If the element is not found, return -1.

The time complexity of Simple Search algorithm is O(n), where n is the number of elements in the list. 

#### Estimating Simple Search Time

The time taken by Simple Search algorithm depends on the size of the list. If the list contains n elements, then the worst-case scenario is that the desired element is not present in the list, and we have to check all n elements. In this case, the time taken by Simple Search algorithm is n * T, where T is the time taken to compare two elements.

#### Binary Search

Binary Search is a more efficient searching algorithm than Simple Search. It works only on sorted lists. The steps involved in Binary Search are:

- Find the middle element of the list.
- Compare the middle element with the desired element.
- If the middle element is equal to the desired element, return its index.
- If the middle element is greater than the desired element, search in the left half of the list.
- If the middle element is less than the desired element, search in the right half of the list.
- Repeat steps 1 to 5 until the desired element is found or the list is exhausted.

The time complexity of Binary Search algorithm is O(log n), where n is the number of elements in the list.

#### Estimating Binary Search Time

The time taken by Binary Search algorithm depends on the size of the list. If the list contains n elements, then the worst-case scenario is that the desired element is not present in the list, and we have to search until we exhaust the list. In this case, the time taken by Binary Search algorithm is log2(n) * T, where T is the time taken to compare two elements.

In addition to Simple Search and Binary Search, we will also cover Recursive Fibonacci and Tower of Hanoi algorithms as a part of this unit. These algorithms use recursion to solve problems and are widely used in computer science.

By understanding these searching algorithms and their estimating search time, you will be able to choose the appropriate algorithm for your problem and optimize your code for better performance.