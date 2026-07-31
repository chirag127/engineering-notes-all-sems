### Shared Memory

Shared memory is a concept in distributed systems where multiple nodes or computers are connected through a network and have their local memories. A distributed shared memory (DSM) system manages the memory across all the nodes, allowing them to transparently interconnect and process .

The DSM implements the shared memory model in distributed systems but doesn’t have physical shared memory. Instead, all the nodes share the virtual address space provided by the shared memory model, and data moves between the main memories of different nodes .

DSM can be achieved via software as well as hardware. Hardware examples include cache coherence circuits and network interface controllers. There are three ways of implementing DSM: Page-based approach using virtual memory .

From a programmer's perspective, the shared memory programming model is a natural extension of the uniprocessor memory model on a distributed system. S-DSM implementation is transparent to the programmer, allowing them to handle synchronizations in the familiar shared memory model .