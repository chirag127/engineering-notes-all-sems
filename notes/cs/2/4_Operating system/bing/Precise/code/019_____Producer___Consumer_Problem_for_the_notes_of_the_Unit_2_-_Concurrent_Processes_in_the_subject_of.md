### Producer / Consumer Problem

The producer-consumer problem is a classic example of a multi-process synchronization problem. The problem describes two processes, the producer and the consumer, who share a common, fixed-size buffer used as a queue.

1. The producer's job is to generate data, put it into the buffer, and start again.
2. At the same time, the consumer is consuming the data (i.e., removing it from the buffer), one piece at a time.
3. The problem is to make sure that the producer won't try to add data into the buffer if it's full and that the consumer won't try to remove data from an empty buffer.
4. The solution can be reached by using semaphores which is an integer variable that, apart from initialization, is accessed only through two standard atomic operations: wait and signal.
5. The wait operation decrements the semaphore, and the signal operation increments it.
6. If the value of the semaphore is negative after the decrement, then the process executing the wait is blocked.
7. If the value of the semaphore is zero or positive after the increment, then one of the blocked processes is unblocked.
