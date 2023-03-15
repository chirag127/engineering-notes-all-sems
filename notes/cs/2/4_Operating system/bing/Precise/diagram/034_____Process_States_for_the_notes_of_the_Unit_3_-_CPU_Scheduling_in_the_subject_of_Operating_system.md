### Process States

In the context of CPU scheduling in an operating system, a process can be in one of the following states:

1. **New:** The process is being created.
2. **Ready:** The process is waiting to be assigned to a processor.
3. **Running:** Instructions are being executed.
4. **Waiting:** The process is waiting for some event to occur (such as an I/O completion or reception of a signal).
5. **Terminated:** The process has finished execution.

A process can transition between these states as it is executed by the CPU. The state diagram below illustrates the possible transitions between the different process states.

```
+---------+     +---------+
|         |     |         |
|   New   |---->|  Ready  |
|         |     |         |
+----+----+     +----+----+
     |               |
     |               |
     v               v
+----+----+     +----+----+
|         |     |         |
| Waiting |<--->| Running |
|         |     |         |
+----+----+     +----+----+
     |               |
     |               |
     v               v
+---------+     +---------+
|         |     |         |
|Terminated|<---|  Ready  |
|         |     |         |
+---------+     +---------+
```
