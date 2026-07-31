### Message Queue

- A message queue is a form of intertask communication that allows tasks and interrupts to send and receive data by copy.
- A message queue can store multiple messages of the same size, which can be a pointer to larger buffers.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and unblock any task that is waiting to receive from the queue.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and unblock any task that is waiting to send to the queue.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.
- A message queue can be used to implement various communication patterns, such as producer-consumer, event-driven, or publish-subscribe.
- A message queue can be used to replace some of the functionality of signals, such as notifying a task when a message is available.
- A message queue can be used in both VxWorks and FreeRTOS, as they both support the POSIX message queue API.