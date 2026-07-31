 Here are the notes on Communication and Synchronization for Unit 3 - Real Time Kernel Basics:

### Communication

- Inter-process communication (IPC) is a key concept in real-time systems to enable communication between processes.
- Common IPC methods:
  - Shared memory: Processes share a region of memory to exchange data. Needs synchronization mechanisms to avoid conflicts.
  - Message passing: Processes exchange messages through send/receive operations. Can be synchronous ( sending process blocks until message is received) or asynchronous (sending process continues executing after sending message).
  - Remote procedure call (RPC): A process can call a function in another process and get a response. Needs a protocol to encode and decode parameters and results.

### Synchronization

- Synchronization is necessary to coordinate the execution of processes to avoid conflicts and ensure correct operation.
- Common synchronization methods:
  - Semaphores: Allow restricting the number of processes that can access a shared resource. Binary semaphores can only have value 0 or 1.
  - Monitors: Allow restricting access to shared data to one process at a time and can include condition variables for signaling/waiting.
  - Events: Allow signaling between processes that a certain event has occurred. The processes can wait for specific events to happen.
- Correct synchronization is crucial for real-time systems to meet deadlines and avoid errors. Livelock and deadlock must be avoided.

The notes are written in a formal tone with points in Markdown format as requested. No emojis or external links have been included. Please let me know if you would like me to modify or expand the notes in any way.