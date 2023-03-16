### Counting oneness in a window

- Counting oneness in a window is a problem of estimating the number of 1's in the last k bits of a data stream, where k is a large number that cannot be stored in memory.
- One possible solution is to use the DGIM algorithm, which uses a compact representation of the stream using buckets of 1's with timestamps and sizes.
- The DGIM algorithm works as follows:
  - Each bit of the stream has a timestamp, the position in which it arrives. The first bit has timestamp 1, the second has timestamp 2, and so on.
  - The algorithm maintains a set of buckets, each consisting of the timestamp of its rightmost bit and the number of 1's in the bucket.
  - The buckets are stored in a circular array of size N, where N is the length of the window. The algorithm also keeps track of the total number of bits seen in the stream modulo N, which can be used to determine the position of a bucket in the current window.
  - The buckets are subject to two rules:
    - Rule 1: There can be at most two buckets of the same size.
    - Rule 2: The buckets are ordered by their timestamps, from oldest to newest.
  - Whenever a new bit arrives, the algorithm performs the following steps:
    - Step 1: If the bit is 0, do nothing. If the bit is 1, create a new bucket of size 1 with the current timestamp and append it to the end of the array.
    - Step 2: If there are more than two buckets of the same size, merge the two oldest buckets of that size into a new bucket of twice the size and half the timestamp. Repeat this step until Rule 1 is satisfied.
    - Step 3: If the oldest bucket in the array is no longer in the current window, remove it from the array.
  - To estimate the number of 1's in the last k bits, the algorithm uses the following formula:
    - Estimate = Sum of the sizes of all buckets except the oldest one + Half the size of the oldest bucket
  - The estimate is guaranteed to be within 50% of the true count, and the algorithm uses O(log2 N) bits of space.