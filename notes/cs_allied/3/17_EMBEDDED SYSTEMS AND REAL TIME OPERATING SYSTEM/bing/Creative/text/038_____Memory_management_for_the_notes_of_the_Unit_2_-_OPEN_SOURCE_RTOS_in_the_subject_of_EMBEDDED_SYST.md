### Memory management for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Memory management is the process of allocating and deallocating memory for the tasks and objects in an RTOS.
- Memory management can be done in two ways: static or dynamic.
- Static memory management means that the memory is allocated at compile time and cannot be changed at run time. This method is simple, fast, and deterministic, but it may waste memory or cause memory fragmentation.
- Dynamic memory management means that the memory is allocated and freed at run time, depending on the needs of the application. This method is flexible, efficient, and adaptable, but it may introduce overhead, latency, and non-determinism.
- An open source RTOS is an RTOS that is freely available and can be modified and distributed by anyone. Some examples of open source RTOS are FreeRTOS, Zephyr, and Azure RTOS.
- An open source RTOS may use different memory management options, such as:
  - Heap: a pool of memory that can be dynamically allocated and freed by the RTOS or the application. The heap can be implemented using different algorithms, such as first-fit, best-fit, or worst-fit. The heap may suffer from fragmentation, memory leaks, or allocation failures.
  - Stack: a region of memory that is used to store the local variables and return addresses of each task. The stack can be allocated statically or dynamically, depending on the RTOS configuration. The stack size should be sufficient to avoid stack overflow or underflow.
  - Static: a fixed amount of memory that is reserved for each task or object at compile time. The static memory can be allocated using macros or linker scripts. The static memory is deterministic and does not require any run time management.
  - User-provided: a custom memory allocation scheme that is implemented by the application writer. The user-provided memory can be passed to the RTOS API functions as a parameter. The user-provided memory gives the application writer full control over the memory management.