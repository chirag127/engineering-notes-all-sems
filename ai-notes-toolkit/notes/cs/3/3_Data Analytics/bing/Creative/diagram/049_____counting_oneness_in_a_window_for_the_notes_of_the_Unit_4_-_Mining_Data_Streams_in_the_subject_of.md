### Counting oneness in a window

- Counting oneness in a window is a problem of estimating the number of 1's in the last k bits of a data stream, where k is a large number that cannot be stored in memory.
- One possible solution is to use the DGIM algorithm, which uses a compact representation of the stream using buckets of 1's with timestamps and sizes.
- The DGIM algorithm works as follows :
  - Each bit of the stream has a timestamp, the position in which it arrives. The first bit has timestamp 1, the second has timestamp 2, and so on.
  - The algorithm maintains a set of buckets, each consisting of the timestamp of its rightmost bit and the number of 1's in the bucket.
  - The buckets are stored in a circular array of size N, where N is the length of the window. The algorithm also stores the total number of bits ever seen in the stream modulo N, which allows to determine the position of any bit in the current window.
  - The buckets are subject to two constraints:
    - The buckets are ordered by their timestamps, from oldest to newest.
    - There can be at most two buckets of the same size, and they must be adjacent.
  - Whenever a new bit arrives, the algorithm performs the following steps:
    - If the bit is 0, it is ignored.
    - If the bit is 1, it creates a new bucket with timestamp equal to the current bit position and size equal to 1.
    - If the new bucket violates the second constraint, it is merged with the next bucket of the same size, and the resulting bucket inherits the timestamp of the newer bucket.
    - If the merge causes another violation of the second constraint, the process is repeated until no violation occurs.
    - If the oldest bucket falls out of the window, it is discarded.
  - To estimate the number of 1's in the last k bits, the algorithm sums up the sizes of all the buckets that are fully contained in the window, and adds half of the size of the oldest bucket that is partially contained in the window. This gives an approximation with an error of no more than 50%.
- An example of the DGIM algorithm is shown below, where N = 16 and k = 10:

| Bit stream | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Timestamp  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16|
| Buckets    |   |(2,1)|(2,1)|(4,1)|(4,1)|(4,1)|(7,1)|(8,1)|(9,1)|(10,1)|(11,1)|(12,1)|(13,1)|(14,2)|(15,1)|(16,2)|
|            |   |     |     |     |     |     |     |     |     |     |     |     |     |(8,2)|(15,1)|(16,2)|
|            |   |     |     |     |     |     |     |     |     |     |     |     |     |     |(15,3)|(16,2)|
|            |   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |(16,5)|

- The estimate for the number of 1's in the last 10 bits is 5 + 0.5 * 3 = 6.5, which is close to the actual number of 7.