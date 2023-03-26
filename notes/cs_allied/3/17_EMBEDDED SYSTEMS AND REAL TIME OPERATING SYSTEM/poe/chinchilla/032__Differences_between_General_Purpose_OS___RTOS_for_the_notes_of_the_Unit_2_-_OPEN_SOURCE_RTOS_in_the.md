### Differences between General Purpose OS & RTOS

Real-time operating systems (RTOS) and general-purpose operating systems (GPOS) are two different types of operating systems used in embedded systems. Here are the differences between them:

1. **Real-time capabilities**: RTOS is designed to handle real-time applications that require quick and predictable response times, while GPOS is not specifically designed for real-time applications. RTOS can handle interrupt-driven I/O operations, and it guarantees that a task will be completed within a particular time frame.

2. **Resource management**: In RTOS, resources such as memory, CPU, and bandwidth are managed carefully to meet the real-time requirements of the system. On the other hand, GPOS does not prioritize the real-time requirements of the system, and resources are managed based on the demands of the applications.

3. **Concurrency**: RTOS is designed to manage multiple tasks running concurrently, and it can handle preemption, where a high-priority task can interrupt a low-priority task. GPOS can also handle concurrency, but it may not provide the same level of control as an RTOS.

4. **Kernel size**: RTOS has a smaller kernel size than GPOS because it is designed to handle specific tasks, while GPOS is designed to handle a wide range of applications. This makes RTOS more efficient and faster in responding to real-time events.

5. **Customizability**: RTOS can be customized to meet specific needs of the system, while GPOS is designed to work with a wide range of applications and may not be easily customizable.

6. **Cost**: RTOS is typically more expensive than GPOS because it is designed to handle real-time applications, which require more resources and specialized features. GPOS is more cost-effective and can handle a wide range of applications.

In conclusion, RTOS and GPOS are two different types of operating systems used in embedded systems. RTOS is designed to handle real-time applications that require quick and predictable response times, while GPOS is not specifically designed for real-time applications. RTOS is more efficient, customizable, and expensive than GPOS.