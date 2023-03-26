 Here are the notes in markdown format without any emojis or external links and in a formal tone:

### Counting Distinct Elements in a Stream

1.  Maintaining exact counts of distinct elements in a data stream is challenging due to the unbounded nature of streams.
2.  Approximate distinct counting algorithms provide bounded space and time guarantees while providing an estimate of the number of distinct elements seen so far in a stream.
3.  Flajolet-Martin algorithm: Provides a probabilistic estimate of distinct count using hash functions and logarithmic space. It uses a hash table with a small, fixed number of buckets to map string to integers. Collisions are accounted for using stochastic averaging.
4.  HyperLogLog: Improves upon Flajolet-Martin algorithm using a more sophisticated stochastic averaging technique providing better accuracy with smaller space requirements. It is suitable for counting distinct elements in massive data streams.
5.  Count-min sketch: Provides a way to estimate frequency counts of objects in a stream using hash functions and fixed-size arrays. It can be used to estimate distinct counts, but may produce large errors for skewed data.

These algorithms provide useful approximations of distinct counts using small, fixed space, enabling analytics on massive data streams. The trade-off is losing exactness for space and time efficiency. The choice of algorithm depends on the use case and accuracy requirements.

Does this help? Let me know if you would like me to modify or expand the notes in any way.