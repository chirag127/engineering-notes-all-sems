### Counting Oneness in a Window

- Counting oneness in a window is a problem of estimating the number of 1's in the last k bits of a data stream, where k is a parameter that can vary.
- This problem is useful for applications such as network monitoring, where we want to measure the traffic volume or the number of packets in a given time interval.
- A naive solution is to store all the k bits in memory and count the 1's, but this is not feasible when k is large or the stream is unbounded.
- A better solution is to use a sketching technique that compresses the stream into a smaller representation that allows approximate counting with a bounded error.
- One such technique is the DGIM algorithm, which uses O(log N) bits to represent a window of N bits, and allows us to estimate the number of 1's in the window with an error of no more than 50% .
- The DGIM algorithm works as follows:
  - Each bit of the stream has a timestamp, the position in which it arrives. The first bit has timestamp 1, the second has timestamp 2, and so on.
  - The algorithm divides the window into buckets, each consisting of the timestamp of its right (most recent) end and the number of 1's in the bucket.
  - The buckets are maintained in a queue, with the most recent bucket at the head and the oldest bucket at the tail.
  - The algorithm ensures that there are at most two buckets of the same size, and that the sizes of the buckets are powers of two. This is done by merging two buckets of the same size into one larger bucket whenever a new bucket is created or an old bucket is dropped.
  - A new bucket is created whenever a 1 arrives in the stream. The new bucket has size 1 and the timestamp of the 1.
  - An old bucket is dropped whenever the timestamp of its right end is more than N positions away from the current position. This means that the bucket is no longer in the window of N bits.
  - To estimate the number of 1's in the last k bits, the algorithm sums up the sizes of all the buckets that are entirely within the last k bits, and adds half of the size of the bucket that straddles the k-th position from the right. This gives an upper bound on the number of 1's, since the bucket that straddles the k-th position may contain some 0's.
  - The algorithm can also provide a lower bound on the number of 1's by subtracting half of the size of the bucket that straddles the k-th position from the sum of the sizes of all the buckets that are entirely within the last k bits. This gives a lower bound on the number of 1's, since the bucket that straddles the k-th position may contain some 1's.
  - The algorithm can also provide a point estimate by taking the average of the upper and lower bounds, or by using a random coin toss to decide whether to add or subtract half of the size of the bucket that straddles the k-th position from the sum of the sizes of all the buckets that are entirely within the last k bits.

- Here is an example of how the DGIM algorithm works on a stream of bits:

  - Suppose the stream is 001011001101 and the window size is N = 8. The current position is 12 and the oldest position in the window is 5.
  - The queue of buckets is as follows:

    | Timestamp | Size |
    | --------- | ---- |
    | 12        | 1    |
    | 11        | 1    |
    | 10        | 1    |
    | 9         | 1    |
    | 8         | 2    |
    | 6         | 2    |

  - To estimate the number of 1's in the last k = 4 bits, the algorithm sums up the sizes of the buckets that are entirely within the last 4 bits, which are 1, 1, and 1, and adds half of the size of the bucket that straddles the 4-th position from the right, which is 2. The upper bound is 1 + 1 + 1 + 1 = 4.
  - The lower bound is 1 + 1 + 1 - 1 = 2.
  - The point estimate is (4 + 2) / 2 =