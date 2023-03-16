# Differences between General Purpose OS & RTOS

1. **Purpose**: A General Purpose Operating System (GPOS) is designed to provide a platform for multiple applications to run on a single device, while a Real-Time Operating System (RTOS) is designed to run a specific application with precise timing and reliability requirements.

2. **Scheduling**: GPOS uses a priority-based scheduling algorithm, where the highest priority task is executed first. RTOS, on the other hand, uses a deterministic scheduling algorithm, where the execution of tasks is guaranteed within a specific time frame.

3. **Interrupt Handling**: GPOS handles interrupts in a non-deterministic manner, where the time taken to service an interrupt is not guaranteed. RTOS, on the other hand, handles interrupts in a deterministic manner, where the time taken to service an interrupt is guaranteed.

4. **Memory Management**: GPOS uses dynamic memory allocation, where memory is allocated and deallocated at runtime. RTOS, on the other hand, uses static memory allocation, where memory is allocated at compile-time and remains fixed throughout the execution of the program.

5. **Performance**: GPOS is designed to provide good performance for a wide range of applications, while RTOS is designed to provide high performance for a specific application.

6. **Footprint**: GPOS has a larger footprint, as it includes features and services that may not be required by all applications. RTOS, on the other hand, has a smaller footprint, as it includes only the features and services required by the specific application it is designed to run.

7. **Examples**: Examples of GPOS include Windows, Linux, and macOS, while examples of RTOS include FreeRTOS, VxWorks, and QNX.
