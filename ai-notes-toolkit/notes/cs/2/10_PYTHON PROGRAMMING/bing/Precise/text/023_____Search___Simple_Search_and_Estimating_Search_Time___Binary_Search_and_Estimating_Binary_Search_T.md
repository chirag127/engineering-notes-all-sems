### Search: Simple Search and Estimating Search Time, Binary Search and Estimating Binary Search Time

#### Simple Search
- Simple search, also known as linear search, is a method for finding an element within a list.
- It sequentially checks each element of the list until a match is found or the whole list has been searched.
- The time complexity of simple search is O(n), where n is the number of elements in the list.

#### Estimating Search Time for Simple Search
- The time it takes to perform a simple search depends on the size of the list.
- If the list has n elements, in the worst case, the algorithm will have to check all n elements to find the target element.
- Therefore, the worst-case time complexity of simple search is O(n).

#### Binary Search
- Binary search is a search algorithm that finds the position of a target value within a sorted array.
- It compares the target value to the middle element of the array.
- If the target value is less than the middle element, the search continues in the lower half of the array.
- If the target value is greater than the middle element, the search continues in the upper half of the array.
- The process is repeated until the target value is found or it is determined that the target value is not in the array.
- The time complexity of binary search is O(log n), where n is the number of elements in the array.

#### Estimating Binary Search Time
- The time it takes to perform a binary search depends on the size of the list.
- If the list has n elements, in the worst case, the algorithm will have to perform log2(n) comparisons to find the target element.
- Therefore, the worst-case time complexity of binary search is O(log n).

### Unit 5 - Iterators & Recursion: Recursive Fibonacci, Tower Of Hanoi

#### Recursive Fibonacci
- The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding numbers.
- The first two numbers in the sequence are 0 and 1.
- The Fibonacci sequence can be defined recursively as follows:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1
- A recursive function to compute the nth Fibonacci number can be written as follows:
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

#### Tower Of Hanoi
- The Tower of Hanoi is a mathematical puzzle consisting of three rods and a number of disks of different sizes, which can slide onto any rod.
- The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top.
- The objective of the puzzle is to move the entire stack to another rod, obeying the following rules:
    - Only one disk can be moved at a time.
    - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
    - No disk may be placed on top of a smaller disk.
- A recursive solution to the Tower of Hanoi puzzle can be written as follows:
```python
def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n-1, source, auxiliary, target)
        print(f'Move disk {n} from {source} to {target}')
        hanoi(n-1, auxiliary, target, source)
```