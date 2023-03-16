### Message Queue

A message queue is a data structure used in inter-process communication (IPC) and for inter-thread communication within the same process. It is used for exchanging messages between processes or threads. Message queues provide an asynchronous communication mechanism, meaning that the sender and receiver of the message do not need to interact with the message queue at the same time.

In the context of VXWORKS / FREE RTOS, message queues are used for communication between tasks. The following are some key points to remember about message queues in these real-time operating systems:

1. Message queues allow multiple tasks to send and receive messages to and from the same queue.
2. Messages are stored in the queue until they are retrieved by a receiving task.
3. The order in which messages are retrieved from the queue depends on the queue's scheduling policy.
4. Message queues can have a fixed size, meaning that the number of messages that can be stored in the queue is limited.
5. If a message queue is full, a sending task may be blocked until space becomes available in the queue.
6. Message queues can be used for both inter-task and intra-task communication.

In summary, message queues provide a flexible and powerful mechanism for communication between tasks in real-time operating systems such as VXWORKS and FREE RTOS. They allow for asynchronous communication and can be used to exchange messages between multiple tasks. It is important to carefully design the use of message queues in a system to ensure that they are used effectively and efficiently.