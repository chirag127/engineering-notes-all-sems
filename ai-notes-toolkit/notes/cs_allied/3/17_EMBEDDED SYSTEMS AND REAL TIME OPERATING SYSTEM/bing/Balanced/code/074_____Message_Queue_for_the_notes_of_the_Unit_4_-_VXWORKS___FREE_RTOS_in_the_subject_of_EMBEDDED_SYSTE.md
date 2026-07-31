### Message Queue

- A message queue is a form of inter-task communication that allows tasks and interrupts to send and receive data by copy.
- A message queue can store multiple messages of the same size, which can be a pointer to larger buffers or structures.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and unblock any task waiting to receive from the queue.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and unblock any task waiting to send to the queue.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it or unblocking any task.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.

### VXWORKS

- VXWORKS is a real-time operating system (RTOS) that supports message queues as a kernel object.
- A message queue can be created using the `msgQCreate()` function, which returns an ID to the queue.
- A message can be sent to a queue using the `msgQSend()` function, which copies the message into the queue and wakes up any task pending on the queue.
- A message can be received from a queue using the `msgQReceive()` function, which copies the message from the queue and wakes up any task pending on the queue.
- A message can be peeked from a queue using the `msgQShow()` function, which copies the message from the queue without removing it or waking up any task.
- A message queue can be deleted using the `msgQDelete()` function, which frees the memory allocated for the queue.

### FREE RTOS

- FREE RTOS is a portable, open source, mini RTOS that supports message queues as a core feature.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and unblock any task waiting to receive from the queue.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and unblock any task waiting to send to the queue.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it or unblocking any task.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.
- FREE RTOS also supports POSIX message queues through the FREE RTOS+POSIX library, which provides a subset of the POSIX API for message queues.