# Counting oneness in a window

- Counting oneness in a window is a problem of estimating the number of 1's in the last k bits of a data stream, where k is a large number that cannot be stored in memory.
- One possible solution is to use the DGIM algorithm, which uses a compact representation of the stream using buckets of 1's with timestamps and sizes.
- The DGIM algorithm works as follows :
  - Each bit of the stream has a timestamp, the position in which it arrives. The first bit has timestamp 1, the second has timestamp 2, and so on.
  - The algorithm maintains a set of buckets, each consisting of the timestamp of its rightmost bit and the number of 1's in the bucket.
  - The buckets are stored in a circular array of size N, where N is the length of the window. The algorithm also stores the total number of bits ever seen in the stream modulo N, which allows to determine the position of any bit in the current window.
  - The buckets are subject to two invariants:
    - There are at most two buckets of the same size.
    - The buckets are ordered by their timestamps, from oldest to newest.
  - Whenever a new bit arrives, the algorithm performs the following steps:
    - If the bit is 0, it is ignored.
    - If the bit is 1, it creates a new bucket of size 1 with the current timestamp and appends it to the end of the array.
    - If there are now three buckets of the same size, the algorithm merges the two oldest buckets into one bucket of twice the size and half the timestamp (rounded down).
    - The algorithm repeats the merging step until there are no more than two buckets of the same size.
  - To estimate the number of 1's in the last k bits, the algorithm performs the following steps:
    - It finds the oldest bucket that is entirely within the last k bits, by subtracting the bucket's timestamp from the current timestamp modulo N and comparing it with k.
    - It sums up the sizes of all the buckets that are newer than the oldest bucket, and adds half the size of the oldest bucket to the sum.
    - It returns the sum as the estimate, which is guaranteed to be within 50% of the true count.

: Counting Ones in a Window — ALIS: Algorithmic Library for Scalability. https://phdinds-aim.github.io/alis/stream-mining/counting-ones.html
: Explain DGIM algorithm for counting ones in a window - Ques10. https://www.ques10.com/p/2870/explain-dgim-algorithm-for-counting-ones-in-a-wi-1/