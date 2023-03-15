# Process Transition Diagram for CPU Scheduling

- A process transition diagram is a graphical representation of the possible states of a process and the transitions between them.
- A process state is a condition or mode that a process can be in during its execution.
- A process transition is a change of state that occurs due to some event or action.
- A process transition diagram helps to understand the behavior and life cycle of a process in an operating system.
- A process transition diagram also helps to design and implement a process scheduling policy that determines which process should run on the CPU at any given time.

## Process States

- There are five basic states that a process can be in, as shown in the following figure:

![Process State Transition Diagram](https://docs.oracle.com/cd/E19683-01/816-5042/psched-16/figures/psched-2.gif)

- The five states are:

  - **New**: The process is being created and initialized. It is not yet ready to run.
  - **Ready**: The process is waiting to be assigned to a CPU. It is ready to run, but not running.
  - **Running**: The process is executing on a CPU. It is the only state in which the process actually performs its tasks.
  - **Waiting**: The process is blocked and cannot run until some event occurs, such as an I/O completion or a signal. It is also called the blocked or the sleep state.
  - **Terminated**: The process has completed its execution and is being removed from the system. It is also called the exit or the zombie state.

## Process Transitions

- The transitions between the states are caused by various events or actions, such as:

  - **Admission**: The operating system creates a new process and puts it in the new state.
  - **Dispatch**: The scheduler selects a process from the ready queue and assigns it to a CPU, changing its state from ready to running.
  - **Preemption**: The scheduler interrupts a running process and puts it back in the ready queue, changing its state from running to ready. This can happen due to a timer interrupt, a higher priority process becoming ready, or a system call.
  - **I/O or event wait**: A running process requests an I/O operation or waits for an event to occur, changing its state from running to waiting. This can happen due to a system call, a trap, or an interrupt.
  - **I/O or event completion**: An I/O operation or an event that a waiting process was waiting for is completed, changing its state from waiting to ready. This can happen due to an interrupt or a signal.
  - **Exit**: A running process finishes its execution and releases its resources, changing its state from running to terminated. This can happen due to a system call, a trap, or an interrupt.

## Process Scheduling Policy

- A process scheduling policy is a set of rules or algorithms that determines which process should run on the CPU at any given time.
- A process scheduling policy aims to optimize some criteria, such as CPU utilization, throughput, response time, waiting time, or fairness.
- A process scheduling policy can be classified into two categories: preemptive and non-preemptive.
  - A preemptive policy allows the scheduler to interrupt a running process and replace it with another ready process, based on some priority or time quantum. This enables the scheduler to respond quickly to changes in the system and improve the performance of interactive processes.
  - A non-preemptive policy does not allow the scheduler to interrupt a running process until it voluntarily relinquishes the CPU, either by terminating or by waiting for an I/O or an event. This avoids the overhead of context switching and improves the performance of CPU-bound processes.
- Some examples of process scheduling policies are:

  - **First-Come, First-Served (FCFS)**: The scheduler selects the process that arrived first in the ready queue and runs it until it finishes or blocks. This is a non-preemptive policy that is simple and fair, but may cause long waiting times and poor CPU utilization.
  - **Shortest Job First (SJF)**: The scheduler selects the process that has the shortest estimated CPU burst time and runs it until it finishes or blocks. This is a non-preemptive policy that minimizes the average waiting time, but may cause starvation of long processes and requires prior knowledge of CPU burst times.
  - **Shortest Remaining Time First (SRTF)**: The scheduler selects the process that has the shortest remaining CPU burst time and runs it until it finishes, blocks, or is preempt