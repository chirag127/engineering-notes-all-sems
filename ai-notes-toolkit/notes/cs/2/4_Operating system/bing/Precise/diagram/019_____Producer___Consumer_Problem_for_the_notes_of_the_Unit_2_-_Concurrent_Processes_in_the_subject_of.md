### Producer / Consumer Problem

The Producer / Consumer Problem is a classical example of a multi-process synchronization problem. The problem describes two processes, the producer and the consumer, who share a common, fixed-size buffer used as a queue.

1. The producer's job is to generate data, put it into the buffer, and start again.
2. At the same time, the consumer is consuming the data (i.e., removing it from the buffer), one piece at a time.
3. The problem is to make sure that the producer won't try to add data into the buffer if it's full and that the consumer won't try to remove data from an empty buffer.
4. The solution can be reached by using semaphores which is an integer variable that, apart from initialization, is accessed only through two standard atomic operations: wait and signal.