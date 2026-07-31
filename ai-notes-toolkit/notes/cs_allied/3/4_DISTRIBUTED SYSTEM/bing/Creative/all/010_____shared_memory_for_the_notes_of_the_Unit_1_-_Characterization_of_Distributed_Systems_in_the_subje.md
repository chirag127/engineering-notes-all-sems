# Shared Memory

- Shared memory is a programming model for distributed systems that provides a virtual address space shared by all nodes in the system .
- Shared memory can be implemented by hardware or software. Hardware examples include cache coherence circuits and network interface controllers. Software examples include page-based, object-based, or tuple-based approaches.
- Shared memory has some advantages over message passing, such as:
  - It is a natural extension of the uniprocessor memory model and familiar to programmers.
  - It simplifies the communication and synchronization among processes .
  - It allows dynamic and flexible data sharing and load balancing.
- Shared memory also has some challenges and limitations, such as:
  - It requires a consistent view of the shared data among all nodes, which may incur high overhead and latency .
  - It may suffer from false sharing, coherence misses, or thrashing due to the granularity and placement of shared data .
  - It may not scale well with the number of nodes or the size of the shared data .