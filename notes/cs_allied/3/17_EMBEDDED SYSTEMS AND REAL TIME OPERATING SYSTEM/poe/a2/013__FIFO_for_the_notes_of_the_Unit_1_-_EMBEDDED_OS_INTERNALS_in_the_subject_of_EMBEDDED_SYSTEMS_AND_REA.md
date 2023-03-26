 Here are the notes on FIFO for Unit 1 - Embedded OS Internals in Markdown format:

### FIFO

- FIFO stands for First In First Out.
- It is a method for organizing and processing items where the first item added to the queue is the first item to be processed.
- In OS, FIFO is used for resource allocation like CPU scheduling. The process that requests the CPU first gets allocated the CPU first.
- Advantages:
  - Simplicity - easy to implement.
  - Fairness - processes get CPU in the order they requested.
- Disadvantages:
  - Starvation - a process can be delayed indefinitely if higher priority processes keep coming.
  - Low throughput - avg waiting time can be high if there are more processes than CPU.
- Examples:
  - Printer queue - print jobs are processed in the order they are received.
  - CPU scheduling.

The notes are written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or add anything.