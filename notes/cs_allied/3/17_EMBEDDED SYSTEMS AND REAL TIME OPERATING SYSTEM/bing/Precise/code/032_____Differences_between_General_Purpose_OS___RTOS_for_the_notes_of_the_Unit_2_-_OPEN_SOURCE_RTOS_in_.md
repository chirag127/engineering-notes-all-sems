### Differences between General Purpose OS & RTOS

1. **Purpose**: General Purpose Operating Systems (GPOS) are designed to provide a wide range of functionality and services to the user, while Real-Time Operating Systems (RTOS) are designed to meet the specific timing requirements of real-time applications.

2. **Scheduling**: GPOS use a scheduling algorithm that is designed to provide fair access to the CPU for all processes, while RTOS use a scheduling algorithm that is designed to ensure that real-time tasks meet their deadlines.

3. **Interrupt Handling**: GPOS may take longer to respond to interrupts, while RTOS are designed to respond to interrupts quickly and predictably.

4. **Memory Management**: GPOS use virtual memory and paging to manage memory, while RTOS typically use a fixed memory map and do not use virtual memory.

5. **Determinism**: GPOS are not designed to provide deterministic behavior, while RTOS are designed to provide deterministic behavior, meaning that the system will always respond to events in a predictable amount of time.

6. **Footprint**: GPOS typically have a larger memory footprint, while RTOS have a smaller memory footprint, making them suitable for use in embedded systems with limited memory.

7. **APIs**: GPOS provide a wide range of APIs for various functionality, while RTOS provide a more limited set of APIs that are focused on real-time functionality.
