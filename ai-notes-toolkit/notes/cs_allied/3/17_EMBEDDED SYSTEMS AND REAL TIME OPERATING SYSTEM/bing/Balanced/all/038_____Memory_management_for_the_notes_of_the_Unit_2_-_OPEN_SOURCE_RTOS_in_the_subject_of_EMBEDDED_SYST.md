# Memory management for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Memory management is the process of allocating and deallocating memory for the tasks and objects in an RTOS.
- Memory management can be done in two ways: static or dynamic.
- Static memory management means that the memory is allocated at compile time and cannot be changed at run time. This method is simple, fast, and deterministic, but it can waste memory and limit flexibility.
- Dynamic memory management means that the memory is allocated and freed at run time, depending on the needs of the application. This method is more flexible and efficient, but it can introduce overhead, fragmentation, and non-determinism.
- An open source RTOS is an RTOS that is freely available and can be modified and distributed by anyone. Some examples of open source RTOS are FreeRTOS, Zephyr, and Azure RTOS.
- An open source RTOS may use different memory management options, depending on the features and requirements of the RTOS and the application.
- Some of the memory management options for open source RTOS are:

  - Heap: A heap is a pool of memory that can be dynamically allocated and freed by the RTOS or the application. A heap can be implemented using different algorithms, such as first fit, best fit, or worst fit. A heap can provide flexibility and efficiency, but it can also cause fragmentation, overhead, and non-determinism.
  - Stack: A stack is a region of memory that is allocated and freed in a last-in first-out (LIFO) order. A stack is typically used to store local variables and function call information for each task. A stack can provide fast and deterministic memory management, but it can also cause stack overflow or underflow if the size is not adequate.
  - Pool: A pool is a collection of fixed-size memory blocks that can be allocated and freed by the RTOS or the application. A pool can reduce fragmentation and overhead, but it can also limit the size and number of memory blocks available.
  - Static: Static memory management means that the memory is allocated at compile time and cannot be changed at run time. This can be done by using global variables, constants, or macros. Static memory management can provide simplicity and determinism, but it can also waste memory and limit flexibility.

- The choice of memory management option for an open source RTOS depends on several factors, such as:

  - The memory size and availability of the target device.
  - The performance and reliability requirements of the application.
  - The complexity and modularity of the application code.
  - The trade-off between memory usage and execution time.
  - The compatibility and portability of the RTOS and the application.