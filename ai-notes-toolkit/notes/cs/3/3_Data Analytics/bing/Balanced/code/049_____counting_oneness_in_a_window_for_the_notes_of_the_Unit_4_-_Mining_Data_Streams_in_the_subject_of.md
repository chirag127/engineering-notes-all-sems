### Counting oneness in a window

- Counting oneness in a window is a problem of estimating the number of 1's in the last k bits of a data stream, where k is a large number that cannot be stored in memory.
- One possible solution is to use the DGIM algorithm, which uses a compact representation of the stream and allows an approximate count with a bounded error.
- The DGIM algorithm works as follows :
  - Each bit of the stream has a timestamp, the position in which it arrives. The first bit has timestamp 1, the second has timestamp 2, and so on.
  - The algorithm divides the stream into buckets, each consisting of the timestamp of its rightmost bit and the number of 1's in the bucket.
  - The buckets are stored in a circular buffer of size N, where N is the length of the window. The buffer also stores the total number of bits ever seen in the stream modulo N, which helps to locate the bits in the current window.
  - The algorithm maintains the following invariants for the buckets:
    - There are at most two buckets with the same number of 1's.
    - The buckets are ordered by their timestamps, from oldest to newest.
    - The rightmost bit of each bucket is a 1.
  - Whenever a new bit arrives, the algorithm updates the buffer as follows:
    - If the new bit is a 0, it is ignored.
    - If the new bit is a 1, it forms a new bucket with timestamp and count equal to 1, and is added to the buffer.
    - If the buffer is full, the oldest bucket is dropped.
    - If there are three buckets with the same count, the two oldest buckets are merged into one, with the timestamp of the newer one and the count of the sum of the two.
  - To estimate the number of 1's in the last k bits, the algorithm does the following:
    - Find the oldest bucket that is completely within the last k bits, by using the modulo operation and the timestamps.
    - Sum the counts of all the buckets that are newer than this bucket.
    - Subtract half of the count of this bucket, to account for the possible overestimation due to merging.
    - The result is an estimate that is within 50% of the true count.

- Here is an example of the DGIM algorithm in action, with N = 16 and k = 10:

```
Stream: 1001101100
Buffer: [1,1], [2,1], [3,1], [5,1], [6,1], [8,1], [9,1], [10,1]
Estimate: 6 - 0.5 = 5.5

Stream: 10011011001
Buffer: [1,1], [2,1], [3,1], [5,1], [6,1], [8,2], [10,1], [11,1]
Estimate: 6 - 1 = 5

Stream: 100110110011
Buffer: [1,1], [2,1], [3,1], [5,1], [6,1], [8,2], [11,2]
Estimate: 6 - 1 = 5

Stream: 1001101100110
Buffer: [1,1], [2,1], [3,1], [5,1], [6,1], [8,2], [11,2]
Estimate: 6 - 1 = 5

Stream: 10011011001101
Buffer: [1,1], [2,1], [3,1], [5,1], [6,1], [8,2], [11,2], [13,1]
Estimate: 7 - 1 = 6

Stream: 100110110011010
Buffer: [1,1], [2,1], [3,1], [5,1], [6,1], [8,2], [11,2], [13,1]
Estimate: 7 - 1 = 6

Stream: 1001101100110100
Buffer: [2,1], [3,1], [5,1], [6,1], [8,2], [11,2], [13,1]
Estimate: 6 - 0.5 =

```
