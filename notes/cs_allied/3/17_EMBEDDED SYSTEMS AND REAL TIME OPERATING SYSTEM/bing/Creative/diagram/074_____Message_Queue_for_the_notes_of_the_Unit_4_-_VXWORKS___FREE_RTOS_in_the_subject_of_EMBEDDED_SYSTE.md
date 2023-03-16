Hello, I am Sydney, your AI assistant. I will help you with your notes on message queue for the unit 4 of embedded systems and real time operating system.

### Message Queue

- A message queue is a form of intertask communication that allows tasks and interrupts to send and receive messages by copy.
- A message can be any data type, such as a structure, an array, or a pointer to a larger buffer.
- A message queue has a fixed size and capacity, and can store a specified number of messages of a specified size.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and return a status code.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and return a status code.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it and return a status code.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.
- A message queue can be used to synchronize tasks, by blocking the sender until the queue has space, or blocking the receiver until the queue has data.
- A message queue can also be used to notify tasks, by sending a message that triggers a callback function or a signal.
- A message queue can be used to implement a producer-consumer pattern, where one or more tasks produce messages and one or more tasks consume messages.
- A message queue can be used to implement a publish-subscribe pattern, where one or more tasks publish messages and one or more tasks subscribe to messages.
- A message queue can be used to implement a request-response pattern, where one task sends a request message and another task sends a response message.

: https://www.freertos.org/Embedded-RTOS-Queues.html
: https://circuitcellar.com/research-design-hub/design-solutions/freertos-part-5-freertosposix/
: https://freertos.org/a00018.html