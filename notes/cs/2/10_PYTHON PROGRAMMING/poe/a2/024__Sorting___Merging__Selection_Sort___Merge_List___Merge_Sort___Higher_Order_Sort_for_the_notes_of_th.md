 Here is the content in markdown format without any feeling or friendliness, being formal and without any emojis or external links:

### Sorting & Merging:

Selection Sort:

- Repeatedly finds the minimum element from unsorted part and puts it at the beginning.
- Inefficient for large data sets as it makes maximum number of comparisons in the worst and average cases.

Merge List:

- Divide the input list into halves until you have lists of size 1.
- Merge the smaller lists into successively larger lists.
- Efficient for sorting linked lists in O(n log n) time.

Merge Sort:

- Divide the unsorted list into n sublists, each containing 1 element.
- Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.
- Efficient for sorting large data sets in O(n log n) time.

Higher Order Sort:

- A sort that takes a comparator function as an argument to define the sort order.
- The comparator function takes two elements and returns a negative, zero or positive integer depending on whether the first element is less than, equal to or greater than the second element.
- Enables sorting objects of user-defined types and flexible sort orders.

### Iterators & Recursion:

Recursive Fibonacci:

- A recursive function that returns the nth Fibonacci number.
- The base cases are fib(0) = 0 and fib(1) = 1.
- For n > 1, fib(n) = fib(n-1) + fib(n-2).
- Efficient iterative solutions also exist to avoid repeated subproblems.

Tower Of Hanoi:

- A mathematical puzzle consisting of 3 rods and n disks of different sizes.
- The goal is to move the disks from the first rod to the third rod while following the rules: only one disk can be moved at a time and a larger disk cannot sit on top of a smaller disk.
- Solved using recursion with 3 parameters: starting rod, destination rod and spare rod.
- The minimum number of moves required is 2n - 1 where n is the number of disks.