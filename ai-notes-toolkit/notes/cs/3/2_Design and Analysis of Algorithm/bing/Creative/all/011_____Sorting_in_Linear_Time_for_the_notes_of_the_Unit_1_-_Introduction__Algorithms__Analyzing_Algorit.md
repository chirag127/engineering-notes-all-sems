# Sorting in Linear Time

- Sorting in linear time means arranging a sequence of elements in a specific order in O(n) time, where n is the number of elements.
- Sorting in linear time is possible only when some special assumptions are made about the input sequence, such as the range of values, the distribution of elements, or the representation of data.
- Some examples of sorting algorithms that run in linear time are counting sort, radix sort, and bucket sort.

## Counting Sort

- Counting sort assumes that the input sequence consists of n integers in the range [0, k], where k is a small constant.
- Counting sort works by counting the number of occurrences of each integer in the input sequence, and then using those counts to determine the positions of each element in the sorted output sequence.
- Counting sort runs in O(n + k) time and O(n + k) space, where n is the number of elements and k is the range of values .

## Radix Sort

- Radix sort assumes that the input sequence consists of n d-digit numbers, where each digit is in the range [0, b-1], where b is the base of the number system.
- Radix sort works by sorting the input sequence by each digit, starting from the least significant digit to the most significant digit, using a stable sorting algorithm such as counting sort.
- Radix sort runs in O(d(n + b)) time and O(n + b) space, where n is the number of elements, d is the number of digits, and b is the base .

## Bucket Sort

- Bucket sort assumes that the input sequence consists of n real numbers that are uniformly distributed over the interval [0, 1).
- Bucket sort works by dividing the interval [0, 1) into n equal-sized buckets, and then distributing the input elements into the buckets according to their values. Then, each bucket is sorted individually using any comparison-based sorting algorithm, and the buckets are concatenated to form the sorted output sequence.
- Bucket sort runs in O(n) time on average and O(n) space, where n is the number of elements, but it can be as bad as O(n^2) in the worst case if all the elements fall into the same bucket .

: http://personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Sorting/linearTimeIntro.htm
: https://www.javatpoint.com/daa-linear-time-sorting
: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/bf7d79105762bf79bbc0925438e1468a_MIT6_006F11_lec07.pdf