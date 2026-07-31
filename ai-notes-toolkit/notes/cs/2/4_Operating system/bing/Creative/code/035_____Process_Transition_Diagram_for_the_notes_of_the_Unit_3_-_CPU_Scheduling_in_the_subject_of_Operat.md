### Process Transition Diagram for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- A process transition diagram is a graphical representation of the possible states of a process and the transitions between them.
- A process state is a condition or mode that a process can be in during its execution.
- The basic process states are:
  - New: The process is being created.
  - Ready: The process is waiting to be assigned to a CPU.
  - Running: The process is executing on a CPU.
  - Waiting: The process is waiting for some event to occur, such as an I/O completion or a signal.
  - Terminated: The process has finished its execution.
- A process can change its state due to various events, such as:
  - Admission: The operating system admits a new process into the system.
  - Dispatch: The scheduler selects a process from the ready queue and assigns it to a CPU.
  - Interrupt: The CPU is interrupted by an external event, such as a timer or an I/O device.
  - I/O or event wait: The process requests or waits for an I/O operation or another event to complete.
  - I/O or event completion: The I/O operation or the event that the process was waiting for is completed.
  - Exit: The process releases all its resources and terminates.
- A process transition diagram can be drawn as follows:

```text
    +--------+   admission   +-------+   dispatch   +---------+
    |  New   |-------------->| Ready |------------>| Running |
    +--------+               +-------+<------------+---------+
                                   ^ |   interrupt   ^     |
                                   | |               |     |
                                   | +---------------+     |
                                   |   I/O or event wait   |
                                   |                       |
                                   |   I/O or event       |
                                   |   completion         |
                                   |                       |
                                   +-----------------------+
                                   |   exit
                                   v
                               +-----------+
                               | Terminated|
                               +-----------+
```