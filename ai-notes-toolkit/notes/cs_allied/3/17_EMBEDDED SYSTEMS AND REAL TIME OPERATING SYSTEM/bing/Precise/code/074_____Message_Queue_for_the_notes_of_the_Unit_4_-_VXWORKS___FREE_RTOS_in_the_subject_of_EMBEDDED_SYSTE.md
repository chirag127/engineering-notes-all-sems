### Message Queue

A message queue is a data structure used for inter-process communication (IPC) in real-time operating systems such as VxWorks and FreeRTOS. It allows multiple tasks to exchange data in the form of messages.

- A message queue is created by the operating system and is identified by a unique name or ID.
- Tasks can send messages to the queue, which are stored in the queue until they are retrieved by another task.
- The operating system ensures that messages are delivered in the order they were sent and that no messages are lost.
- Message queues can be used for both point-to-point and publish-subscribe communication patterns.
- In point-to-point communication, messages are sent from one task to another specific task.
- In publish-subscribe communication, messages are sent to multiple tasks that have subscribed to the queue.
- Message queues provide a way to decouple the sender and receiver tasks, allowing them to operate independently.
- This can improve the modularity and scalability of the system, as well as simplify the design and implementation of the tasks.