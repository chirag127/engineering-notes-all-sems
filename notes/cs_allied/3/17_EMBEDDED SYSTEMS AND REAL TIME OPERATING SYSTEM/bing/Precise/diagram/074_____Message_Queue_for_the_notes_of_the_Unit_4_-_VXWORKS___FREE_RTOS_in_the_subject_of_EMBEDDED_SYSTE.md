### Message Queue

A message queue is a data structure used in inter-process communication (IPC) and for inter-thread communication within the same process. It is used for exchanging messages between processes or threads. Message queues provide an asynchronous communication mechanism, meaning that the sender and receiver of the message do not need to interact with the message queue at the same time.

In the context of VXWORKS / FREE RTOS, message queues are used for communication between tasks. A task can send a message to a message queue, and another task can receive the message from the message queue. The message queue can hold multiple messages, and the messages are retrieved in the order in which they were sent.

Some key points to remember about message queues in VXWORKS / FREE RTOS are:

- Message queues provide an asynchronous communication mechanism between tasks.
- A message queue can hold multiple messages, and the messages are retrieved in the order in which they were sent.
- Message queues can be used for both inter-process and inter-thread communication.
- In VXWORKS / FREE RTOS, message queues are used for communication between tasks.