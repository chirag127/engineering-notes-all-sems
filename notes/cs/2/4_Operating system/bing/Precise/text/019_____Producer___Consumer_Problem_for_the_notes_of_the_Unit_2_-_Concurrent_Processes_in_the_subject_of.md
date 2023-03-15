### Producer / Consumer Problem

The Producer / Consumer Problem is a classical example of a multi-process synchronization problem. It is also known as the bounded-buffer problem. The problem describes two processes, the producer and the consumer, who share a common, fixed-size buffer used as a queue.

1. The producer's job is to generate data, put it into the buffer, and start again.
2. At the same time, the consumer is consuming the data (i.e., removing it from the buffer), one piece at a time.
3. The problem is to make sure that the producer won't try to add data into the buffer if it's full and that the consumer won't try to remove data from an empty buffer.
4. The solution can be reached by using semaphores which is an abstract data type for controlling access to a common resource by multiple processes in a concurrent system such as a multitasking operating system.

This problem is commonly used to illustrate the power of synchronization between threads and the use of semaphores. It is a fundamental concept in the study of concurrent processes in an operating system.