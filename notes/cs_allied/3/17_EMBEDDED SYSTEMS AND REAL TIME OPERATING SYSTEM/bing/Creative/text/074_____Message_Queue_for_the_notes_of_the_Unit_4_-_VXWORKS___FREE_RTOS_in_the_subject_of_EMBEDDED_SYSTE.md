### Message Queue

- A message queue is a form of inter-task communication that allows tasks and interrupts to send and receive data by copy.
- A message queue can store multiple messages of the same size, which can be either fixed or variable depending on the configuration.
- A message queue can be created using the `xQueueCreate()` or `xQueueCreateStatic()` API functions.
- A message queue can be deleted using the `vQueueDelete()` API function.
- A message can be sent to a queue using the `xQueueSend()`, `xQueueSendToFront()`, `xQueueSendToBack()`, or `xQueueOverwrite()` API functions.
- A message can be received from a queue using the `xQueueReceive()`, `xQueuePeek()`, or `xQueuePeekFromISR()` API functions.
- A message queue can be queried for its status using the `uxQueueMessagesWaiting()`, `uxQueueSpacesAvailable()`, `xQueueIsQueueEmptyFromISR()`, or `xQueueIsQueueFullFromISR()` API functions.
- A message queue can be used to synchronize tasks by blocking on a queue until a message is available or a timeout expires.
- A message queue can be used to notify tasks of events by sending a message with a specific value or a pointer to a larger buffer.
- A message queue can be used to implement a producer-consumer pattern, where one or more tasks produce data and one or more tasks consume data from the same queue.
- A message queue can be used to implement a priority inheritance mechanism, where a task that owns a resource inherits the priority of a higher-priority task that is blocked on the same queue.
- A message queue can be used to implement a deferred interrupt handler, where an interrupt service routine sends a message to a queue and a task handles the message at a later time.

: https://www.freertos.org/Embedded-RTOS-Queues.html
: https://circuitcellar.com/research-design-hub/design-solutions/freertos-part-5-freertosposix/
: https://freertos.org/a00018.html