### Counting Oneness in a Window

- A common problem in data stream mining is to count the number of 1's in a sliding window of N bits over a binary stream.
- This problem has applications in network monitoring, anomaly detection, and trend analysis.
- An exact solution would require storing all N bits in memory, which may not be feasible for large N or high-speed streams.
- Therefore, approximate algorithms are needed that can trade off accuracy for space and time efficiency.
- One such algorithm is the DGIM algorithm, proposed by Datar et al. in 2002.
- The DGIM algorithm uses O(log N) bits to represent a window of N bits, and allows us to estimate the number of 1's in the window with an error of no more than 50%.
- The main idea of the DGIM algorithm is to divide the window into buckets of consecutive 1's, and store only the timestamp of the rightmost bit and the size of each bucket.
- The buckets are subject to two constraints:
  - There can be at most two buckets of the same size.
  - The size of each bucket is a power of two.
- These constraints ensure that the number of buckets is at most 2 log N, and that the size of each bucket can be encoded with log log N bits.
- The algorithm works as follows:
  - For each incoming bit, increment a global counter that keeps track of the total number of bits seen so far (modulo N).
  - If the bit is 0, do nothing.
  - If the bit is 1, create a new bucket of size 1 with the current counter value as the timestamp.
  - If there are now three buckets of size 1, merge the two oldest buckets into a bucket of size 2.
  - Repeat this merging process for any other bucket size that has three buckets, until there are at most two buckets of any size.
  - If the oldest bucket's timestamp is more than N bits away from the current counter value, drop it from the window.
- To estimate the number of 1's in the last k bits, where k <= N, the algorithm does the following:
  - Find the oldest bucket that is completely within the last k bits, and call it B.
  - Sum up the sizes of all the buckets that are newer than B, and call it S.
  - Add half of the size of B to S, and call it E.
  - Return E as the estimate.
- The estimate E is guaranteed to be within 50% of the true count, because the error comes from two sources:
  - Dropping the oldest bucket that is partially within the last k bits, which can cause an underestimation of at most N/2 bits.
  - Adding half of the size of B to S, which can cause an overestimation of at most B/2 bits.
- Since the size of B is at most N/4, the total error is at most N/4 + N/8 = 3N/8 bits, which is less than 50% of N.
- The DGIM algorithm can be extended to handle multiple windows of different sizes, or to estimate the number of 1's in any subinterval of the window, by using more sophisticated data structures and techniques.
- For more details, please refer to the original paper or the lecture notes.

: Counting Ones in a Window — ALIS: Algorithmic Library for Scalability. https://phdinds-aim.github.io/alis/stream-mining/counting-ones.html
: Datar, M., Gionis, A., Indyk, P., & Motwani, R. (2002, January). Maintaining stream statistics over sliding windows. In Proceedings of the thirteenth annual ACM-SIAM symposium on Discrete algorithms (pp. 635-644). Society for Industrial and Applied Mathematics.