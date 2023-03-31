
### Message Queue for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM 

1. Message queues are a form of inter-process communication (IPC) that allow processes to communicate with each other by exchanging messages. 
2. Message queues are used in VxWorks and FreeRTOS to facilitate communication between tasks, interrupts, and other processes. 
3. In VxWorks, message queues are created using the `msgQCreate()` API, while in FreeRTOS they are created using the `xQueueCreate()` API. 
4. Messages can be sent to and received from message queues using the `msgQSend()` and `msgQReceive()` APIs in VxWorks, and the `xQueueSend()` and `xQueueReceive()` APIs in FreeRTOS. 
5. Messages can be sent to a message queue with a priority, which allows for prioritization of messages. 
6. Message queues can be used to send data between tasks, interrupts, and other processes. 
7. Message queues are used in embedded systems and real-time operating systems to facilitate communication between tasks, interrupts, and other processes.