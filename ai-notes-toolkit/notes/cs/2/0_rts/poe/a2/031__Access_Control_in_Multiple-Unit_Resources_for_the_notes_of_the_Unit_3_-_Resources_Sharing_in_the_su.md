 Here is the content in Markdown format without any emojis or external links:

### Access Control in Multiple-Unit Resources

- Resources may have multiple identical units that can be shared among processes. For example, a system may have multiple printers, CPU's, etc. that can be shared.
- To control access to these multiple-unit resources, various access control mechanisms can be used:
- FCFS: Processes are granted resources on a first-come, first-served basis. Simple but can lead to resource starvation for processes.
- Priority: Higher priority processes are granted resources before lower priority processes. Requires a priority assignment algorithm.
- Round-Robin: Each process gets a time quantum to use the resource, and the resource is rotated among processes. Prevents starvation but can lead to internal fragmentation.
- Lottery: Each process gets a random ticket, and the process with the winning ticket gets the resource. Probability of getting the resource increases with number of tickets a process has.
- Other advanced schemes can use resource reservations, distribute resources proportional to needs or quotas, etc.

The content provides formal notes on the given topic without any feeling or friendliness as instructed. The points are written to learn and study the topic of access control in multiple-unit resources for real-time systems. Please let me know if you would like me to modify or expand the response.