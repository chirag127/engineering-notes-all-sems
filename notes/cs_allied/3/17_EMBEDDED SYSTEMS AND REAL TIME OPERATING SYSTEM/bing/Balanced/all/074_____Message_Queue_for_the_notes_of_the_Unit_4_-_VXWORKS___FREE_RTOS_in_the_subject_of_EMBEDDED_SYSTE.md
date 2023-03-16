# Message Queue

- A message queue is a form of intertask communication that allows tasks and interrupts to send and receive messages by copy.
- A message queue can store multiple messages of the same size, which can be a pointer to larger buffers.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and unblock any task that is waiting to receive a message.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and unblock any task that is waiting to send a message.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.

## Message Queue in VxWorks

- VxWorks provides a message queue library that implements the POSIX message queue standard.
- A message queue can be created using the `mq_open()` function, which returns a descriptor to the queue.
- A message can be sent to a queue using the `mq_send()` function, which copies the message into the queue and notifies any thread that is waiting to receive a message.
- A message can be received from a queue using the `mq_receive()` function, which copies the message from the queue and notifies any thread that is waiting to send a message.
- A message queue can be deleted using the `mq_close()` and `mq_unlink()` functions, which close the descriptor and remove the queue from the system.

## Message Queue in FreeRTOS

- FreeRTOS provides a queue library that is similar to the VxWorks message queue library, but with some differences .
- FreeRTOS does not support the `mq_notify()` function, which notifies a thread when a message is available in the queue.
- FreeRTOS does not support the `mq_setattr()` and `mq_getattr()` functions, which set and get the attributes of the queue.
- FreeRTOS does not use descriptors to identify queues, but handles that are of type `QueueHandle_t`.
- FreeRTOS provides additional functions to query the status of the queue, such as `uxQueueMessagesWaiting()`, `uxQueueSpacesAvailable()`, and `xQueueIsQueueEmptyFromISR()`.