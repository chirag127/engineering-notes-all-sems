### Message Queue

- A message queue is a form of intertask communication that allows tasks and interrupts to send and receive messages by copy.
- A message queue can store multiple messages of the same size, which can be a pointer to larger buffers.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and unblock any task that is waiting to receive a message.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and unblock any task that is waiting to send a message.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.

#### VXWORKS

- VXWORKS is a real-time operating system (RTOS) that supports message queues as a kernel object.
- A message queue can be created using the `msgQCreate()` function, which returns an identifier for the queue.
- A message can be sent to a queue using the `msgQSend()` function, which copies the message into the queue and wakes up any task that is waiting to receive a message.
- A message can be received from a queue using the `msgQReceive()` function, which copies the message from the queue and wakes up any task that is waiting to send a message.
- A message can be peeked from a queue using the `msgQShow()` function, which copies the message from the queue without removing it.
- A message queue can be deleted using the `msgQDelete()` function, which frees the memory allocated for the queue.

#### FREE RTOS

- FREE RTOS is a portable, open source, mini RTOS that supports message queues as a primary form of intertask communication.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and unblock any task that is waiting to receive a message.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and unblock any task that is waiting to send a message.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.
- FREE RTOS also supports POSIX message queues through the FREE RTOS+POSIX library, which provides a subset of the POSIX API for message queues.
- A POSIX message queue can be created using the `mq_open()` function, which returns a descriptor for the queue.
- A message can be sent to a queue using the `mq_send()` function, which copies the message into the queue and notifies any task that is waiting to receive a message.
- A message can be received from a queue using the `mq_receive()` function, which copies the message from the queue and notifies any task that is waiting to send a message.
- A message can be peeked from a queue using the `mq_timedreceive()` function, which copies the message from the queue without removing it and returns the remaining time until the message expires.
- A message queue can be deleted using the `mq_close()` and `mq_unlink()` functions, which close the descriptor and remove the queue from the system.

: https://www.freertos.org/Embedded-RTOS-Queues.html
: https://circuitcellar.com/research-design-hub/design-solutions/freertos-part-5-fre