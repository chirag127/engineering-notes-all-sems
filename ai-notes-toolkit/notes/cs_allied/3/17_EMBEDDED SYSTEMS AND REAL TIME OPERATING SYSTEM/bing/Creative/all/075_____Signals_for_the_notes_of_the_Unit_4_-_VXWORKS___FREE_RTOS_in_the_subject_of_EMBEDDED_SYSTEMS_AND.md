# Signals for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Signals are a form of inter-process communication (IPC) that allow a process to send a notification to another process or to itself.
- Signals can be used to indicate events such as termination, segmentation fault, alarm, user input, etc.
- Signals can also be used to implement software interrupts, timers, and asynchronous I/O.
- Signals are not supported by FreeRTOS, but are supported by VxWorks.

## Signals in VxWorks

- VxWorks provides a signal API that is similar to the POSIX standard, but with some differences and limitations.
- VxWorks signals are associated with tasks, not processes. A task can send a signal to another task or to itself using the `kill()` function.
- VxWorks signals are delivered to tasks asynchronously, meaning that the signal handler is executed as soon as possible after the signal is sent, regardless of the current state of the task.
- VxWorks signals are not queued, meaning that only one instance of each signal can be pending for a task at any time. If a signal is sent to a task that already has that signal pending, the new signal is ignored.
- VxWorks signals have predefined numbers and names, such as `SIGINT`, `SIGSEGV`, `SIGALRM`, etc. The signal numbers range from 1 to 31, and the signal names are defined in the header file `signal.h`.
- VxWorks signals can be blocked, ignored, or handled by a task. A task can block or unblock signals using the `sigprocmask()` function, which manipulates the signal mask of the task. A task can ignore a signal by setting its handler to `SIG_IGN`, or handle a signal by setting its handler to a user-defined function using the `sigaction()` function.
- VxWorks signals can be used to implement software interrupts, timers, and asynchronous I/O. For example, a task can use the `sigqueue()` function to send a signal with a value to another task, which can then use the `sigwaitinfo()` function to receive the signal and the value. A task can also use the `timer_create()` and `timer_settime()` functions to create and start a timer that sends a signal to the task when it expires. A task can also use the `aio_read()` and `aio_write()` functions to perform asynchronous I/O operations that send a signal to the task when they are completed.

## Signals in FreeRTOS

- FreeRTOS does not support signals, but provides other mechanisms for inter-task communication and synchronization, such as queues, semaphores, mutexes, event groups, etc.
- FreeRTOS also provides software timers, which are similar to VxWorks timers, but do not use signals. A software timer is a special type of task that executes a callback function when it expires. A software timer can be created and started using the `xTimerCreate()` and `xTimerStart()` functions, respectively.
- FreeRTOS also provides interrupt service routines (ISRs), which are similar to VxWorks signal handlers, but are executed in response to hardware interrupts, not software signals. An ISR is a special type of function that is registered to handle a specific interrupt vector using the `vPortSetInterruptHandler()` function. An ISR can communicate with tasks using the `xQueueSendFromISR()` and `xSemaphoreGiveFromISR()` functions, which are designed to be safe to use from an ISR context.