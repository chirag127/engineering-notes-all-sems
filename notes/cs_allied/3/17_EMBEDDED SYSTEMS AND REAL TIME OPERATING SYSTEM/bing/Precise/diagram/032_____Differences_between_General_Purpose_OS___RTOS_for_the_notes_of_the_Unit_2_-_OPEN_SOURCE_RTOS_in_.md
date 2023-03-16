### Differences between General Purpose OS & RTOS

1. **Functionality**: General Purpose Operating Systems (GPOS) are designed to provide a wide range of functionality and services to the user, while Real-Time Operating Systems (RTOS) are designed to provide a specific set of services with a focus on meeting real-time constraints.

2. **Scheduling**: GPOS use a scheduling algorithm that is designed to provide fair access to the CPU for all processes, while RTOS use a scheduling algorithm that is designed to ensure that real-time tasks meet their deadlines.

3. **Interrupt handling**: GPOS handle interrupts in a way that can introduce significant latency, while RTOS handle interrupts in a way that minimizes latency.

4. **Memory management**: GPOS use virtual memory and paging to manage memory, while RTOS typically use a fixed memory map and do not use virtual memory.

5. **Determinism**: GPOS are not designed to provide deterministic behavior, while RTOS are designed to provide deterministic behavior.

6. **Performance**: GPOS are designed to provide good performance for a wide range of applications, while RTOS are designed to provide good performance for real-time applications.

7. **Footprint**: GPOS typically have a larger memory footprint than RTOS, due to the additional functionality and services they provide.

8. **Development**: GPOS are typically developed using a monolithic or layered approach, while RTOS are typically developed using a modular or microkernel approach.
