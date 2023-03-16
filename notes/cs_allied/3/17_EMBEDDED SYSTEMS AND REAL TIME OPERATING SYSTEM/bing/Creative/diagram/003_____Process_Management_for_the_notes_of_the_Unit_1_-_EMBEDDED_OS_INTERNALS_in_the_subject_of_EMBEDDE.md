Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on process management for the unit 1 of embedded OS internals:

### Process Management

- Process management is how the OS manages and views other software in the embedded system (via processes).
- A process (or a task) is created by an OS to encapsulate all the information that is involved in the executing of a program (stack, PC, source code, data, etc.).
- A process has a state, which can be one of the following: ready, running, waiting, suspended, or terminated.
- A process can be switched from one state to another by the OS, which is called context switching.
- Context switching involves saving the current state of the process and restoring the state of the next process to run.
- Context switching can be triggered by interrupts, system calls, or scheduling decisions.
- Process scheduling is the policy that the OS uses to decide which process to run next.
- Process scheduling can be based on different criteria, such as priority, deadline, or fairness.
- In an embedded system, processes are created to perform specific tasks.
- Depending on the importance of the task, each process is assigned a priority, which is usually static.
- Processes run either periodically or in response to external events.
- Process management in embedded systems must meet the strict requirements of the operational domain, such as real-time and event-driven functionality, safety, reliability, and longevity.