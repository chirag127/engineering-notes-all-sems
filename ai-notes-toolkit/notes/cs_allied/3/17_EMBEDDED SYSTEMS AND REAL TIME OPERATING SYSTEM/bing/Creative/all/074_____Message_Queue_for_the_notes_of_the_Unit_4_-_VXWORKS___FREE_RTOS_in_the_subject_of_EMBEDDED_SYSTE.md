# Message Queue for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A message queue is a data structure that stores messages between tasks or interrupts in a real-time operating system (RTOS).
- A message queue can be used to send data, signals, events, or commands from one task or interrupt to another, or to multiple recipients.
- A message queue can also be used to synchronize tasks or interrupts by blocking them until a message is available or a timeout occurs.
- A message queue has a fixed size and capacity, and can store messages of a fixed or variable length.
- A message queue can be created, deleted, sent to, received from, or peeked at using the RTOS API functions.
- A message queue can be accessed by tasks or interrupts with different priorities, and the RTOS scheduler can use the queue state to determine which task or interrupt to run next.
- A message queue can be configured to use different queueing policies, such as FIFO (first in, first out), LIFO (last in, first out), or priority-based.
- A message queue can be configured to use different notification mechanisms, such as callbacks, signals, semaphores, or events, to inform the sender or receiver of the queue status.

## VXWORKS Message Queue

- VXWORKS is a commercial RTOS that supports message queues as one of its intertask communication mechanisms.
- VXWORKS message queues are created using the msgQCreate function, which takes the following parameters:
  - maxMsgs: the maximum number of messages that can be stored in the queue
  - maxMsgLength: the maximum length of each message in bytes
  - options: a bitmask of options that control the queue behavior, such as queueing policy, notification mechanism, and message length mode
- VXWORKS message queues are deleted using the msgQDelete function, which takes the queue ID as a parameter and frees the memory allocated for the queue.
- VXWORKS message queues are sent to using the msgQSend function, which takes the following parameters:
  - msgQId: the queue ID returned by msgQCreate
  - buffer: a pointer to the message data to be sent
  - nBytes: the length of the message data in bytes
  - timeout: the maximum time to wait for the queue to have enough space, in ticks
  - priority: the priority of the message, used for priority-based queueing
- VXWORKS message queues are received from using the msgQReceive function, which takes the following parameters:
  - msgQId: the queue ID returned by msgQCreate
  - buffer: a pointer to the buffer where the message data will be copied
  - maxNBytes: the maximum length of the buffer in bytes
  - timeout: the maximum time to wait for the queue to have a message, in ticks
- VXWORKS message queues can be peeked at using the msgQNumMsgs function, which takes the queue ID as a parameter and returns the number of messages currently in the queue.
- VXWORKS message queues can be configured to use different notification mechanisms, such as callbacks, signals, semaphores, or events, to inform the sender or receiver of the queue status. For example, the MSG_Q_EVENT_SEND and MSG_Q_EVENT_RECEIVE options can be used to enable event-based notification, and the msgQEvRegister and msgQEvUnregister functions can be used to register and unregister event handlers for the queue.

## FREE RTOS Message Queue

- FREE RTOS is an open source RTOS that supports message queues as one of its intertask communication mechanisms.
- FREE RTOS message queues are created using the xQueueCreate function, which takes the following parameters:
  - uxQueueLength: the maximum number of messages that can be stored in the queue
  - uxItemSize: the size of each message in bytes
- FREE RTOS message queues are deleted using the vQueueDelete function, which takes the queue handle as a parameter and frees the memory allocated for the queue.
- FREE RTOS message queues are sent to using the xQueueSend or xQueueSendFromISR functions, which take the following parameters:
  - xQueue: the queue handle returned by xQueueCreate
  - pvItemToQueue: a pointer to the message data to be sent
  - xTicksToWait: the maximum time to wait for the queue to have enough space, in ticks
- FREE RTOS message queues are received from using the xQueue