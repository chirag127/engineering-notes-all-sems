### Counting Oneness in a Window

- Counting oneness in a window is a problem of estimating the number of 1's in the last k bits of a data stream, where k is a parameter and the stream is too large to store in memory.
- One possible solution is to use the DGIM algorithm, which is based on the following ideas :
  - Divide the stream into buckets of consecutive 1's, each with a timestamp of its rightmost bit and a count of 1's in the bucket.
  - Maintain the invariant that there are at most two buckets of the same size, and merge the oldest two buckets of the same size whenever a new bucket is created.
  - Use a sliding window of size N to keep track of the most recent bits in the stream, and discard the buckets that fall out of the window.
  - To estimate the number of 1's in the last k bits, sum up the counts of all the buckets that are entirely within the window, and add half of the count of the bucket that spans the boundary of the window.
  - The error of the estimate is at most 50%, and the space complexity is O(log2 N) bits.
- An example of the DGIM algorithm is shown below:

![DGIM example](https://phdinds-aim.github.io/alis/_images/dgim.png)

- The stream has 11 bits, and the window size is N = 8. The buckets are shown as rectangles with their timestamps and counts. The last k = 6 bits have 4 1's, and the estimate is 3.5, which is within 50% error.