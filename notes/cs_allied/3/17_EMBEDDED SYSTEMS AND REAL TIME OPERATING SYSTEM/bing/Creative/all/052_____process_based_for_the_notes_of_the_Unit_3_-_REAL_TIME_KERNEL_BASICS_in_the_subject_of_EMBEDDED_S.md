# Process Based Real Time Kernel Basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel can run on different CPU architectures and platforms, such as 8, 16 or 32-bit CPUs or DSP chips.
- A real-time kernel provides a real-time API (Application Programming Interface) that allows the application to create and manage tasks, semaphores, mutexes, queues, timers, etc .
- A real-time kernel also provides a scheduling algorithm that determines which task should run at any given time, based on the priority and state of each task .
- A real-time kernel can be classified into two types: preemptive and cooperative .
  - A preemptive kernel allows a higher priority task to interrupt a lower priority task at any time, ensuring that the most urgent task always gets the CPU .
  - A cooperative kernel requires a lower priority task to voluntarily yield the CPU to a higher priority task, which may result in longer delays and lower responsiveness .
- A real-time kernel can also be implemented in two ways: kernel model and user space model.
  - In a kernel model, the real-time kernel runs in the privileged mode of the CPU, and the application tasks run in the user mode.
  - In a user space model, the real-time kernel runs as a user space process, and the application tasks run as threads within the same process.
  - The advantages and disadvantages of each model are:
    - Kernel model: higher performance, lower overhead, simpler API, but limited kernel API, more complex development and debugging, less portability and compatibility.
    - User space model: lower performance, higher overhead, more complex API, but full Linux API, easier development and debugging, more portability and compatibility.
- A real-time kernel can be used for various applications that require deterministic and timely behavior, such as industrial control, robotics, multimedia, gaming, etc .
- A real-time kernel can be integrated with a standard Linux kernel, such as the Red Hat Enterprise Linux kernel, to provide both real-time and non-real-time functionality.
  - The real-time kernel is also known as kernel-rt or preempt-rt.
  - The real-time kernel can be identified by executing the uname -r command on the terminal, and then looking for the rt keyword in the kernel version.
  - The real-time kernel can be installed and configured using the yum or dnf commands, and the tuned-adm or rt-setup tools.