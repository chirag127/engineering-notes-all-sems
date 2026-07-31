 Here is the formal content in Markdown format without any emojis or external links:

### Message Queue for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

1. Message queues are used for inter-task communication in real-time operating systems like VxWorks and FreeRTOS.
2. A message queue is a buffer area in kernel memory which is accessed by multiple tasks.
3. Tasks can send and receive messages through the message queue.
4. The sender task creates a message and sends it to the queue. The receiver task receives the message from the queue.
5. Message queues have a fixed maximum size which specifies the maximum number of messages that can be queued at a time.
6. If the queue is full, the sending task is suspended until the queue has space available.
7. The receiving task can suspend itself if the queue is empty and wait for messages to arrive.
8. Message queues allow asynchronous communication between tasks. The sender and receiver tasks do not have to be synchronized. They can operate independently at their own pace.
9. Message queues provide a bounded buffer between tasks, ensuring that the recipients receive messages in the same order as they were sent.

The above points cover the key aspects of message queues in real-time operating systems. Let me know if you would like me to elaborate on any of the points or add more details to the content.