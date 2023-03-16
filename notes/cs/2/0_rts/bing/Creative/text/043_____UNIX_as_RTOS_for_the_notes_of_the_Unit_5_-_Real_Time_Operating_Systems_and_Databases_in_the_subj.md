### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a RTOS because it does not guarantee timing requirements of the processes under its control. UNIX strives to provide good average performance, but not correct timing, which is the key feature of a RTOS.
- However, some variants of UNIX, such as Linux, have been modified to provide real-time capabilities by adding patches or modules to the kernel . These modifications aim to reduce the latency and jitter of the system, and to improve the predictability and responsiveness of the tasks .
- Some examples of real-time applications that use Linux as a RTOS are human-in-the-loop simulations, launch vehicles, and spacecrafts . However, using Linux as a RTOS also poses some challenges, such as compatibility, security, testing, and certification .