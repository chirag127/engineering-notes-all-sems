## Unit 2 - Real Time Scheduling

Real-time scheduling is a method of scheduling processes in a computer system where each process is assigned a deadline by which it must complete its execution. The objective of real-time scheduling is to guarantee that processes are completed within their deadlines. This is achieved by assigning priority levels to processes based on their deadlines and ensuring that higher priority processes are executed before lower priority ones. Real-time scheduling algorithms must also be deterministic, meaning that the same sequence of events will always occur for the same set of inputs. This is important for ensuring the reliability and repeatability of real-time systems.

User: What are the types of real-time scheduling algorithms?
ChatGPT: There are two main types of real-time scheduling algorithms:
1. Preemptive Scheduling: processes can be interrupted and resumed based on priority levels.
2. Non-Preemptive Scheduling: processes cannot be interrupted once they start executing.
