 Here is the formal content in markdown format without any emojis or external links inside the header ## Unit 3 - REAL TIME KERNEL BASICS:

## Unit 3 - REAL TIME KERNEL BASICS

1. Real-time systems - Systems where correctness depends not only on logical correctness of computation but also on the time at which the results are produced. Missing deadlines can lead to system failure.
2. Hard real-time systems - Missing deadlines is unacceptable. Deadlines must be guaranteed to be met. Example - Aircraft control systems.
3. Soft real-time systems - Deadlines should be usually met but occasional missed deadlines are tolerable. Example - Video conferencing.
4. Real-time kernels - Specialized operating systems designed for real-time systems. They aim to provide deterministic and fast response times.
5. Preemptive kernels - Kernels where high priority tasks can preempt low priority tasks. This avoids priority inversion and ensures timely completion of high priority tasks.
6. Non-preemptive kernels - Once a task starts execution, it runs to completion without preemption. This can cause priority inversion and missed deadlines for high priority tasks.
7. Task scheduling - The order in which tasks are executed by the kernel. Common policies are rate monotonic scheduling, earliest deadline first, etc. The scheduler must ensure tasks meet their deadlines.
8. Interrupt handling - Hardware interrupts from I/O devices must be handled quickly and predictably to avoid unpredictable delays that can cause deadlines to be missed.