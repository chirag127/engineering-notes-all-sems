 Here are the task states for the notes of Unit 3 - Real Time Kernel Basics:

### Task States
1. Running: The task is currently executing on the processor.
2. Ready: The task is ready to execute but waiting for the processor.
3. Waiting: The task is waiting for some event to occur (e.g. I/O completion, timeout, etc.).
4. Suspended: The task is suspended and will not become ready unless explicitly resumed.

The scheduler is responsible for transitioning tasks between the ready, running and waiting states. The dispatcher is responsible for switching the running task when its time slice expires or when it performs a blocking operation.

The key properties of a real-time system are:

- Predictability: The behaviour of the system should be predictable and adhere to timing constraints.
- Timeliness: The system must respond to events within strict time requirements.
- Reliability: The system must be dependable and fault-tolerant.

The major challenge in designing a real-time system is meeting all these properties under the given constraints. The real-time kernel provides services to schedule tasks and resources for this purpose.

How's this? I have tried to write in a formal tone without any emojis or external links as you specified. Let me know if you would like me to modify or add anything.