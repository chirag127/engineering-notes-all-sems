### Demand paging

Demand paging is a method of virtual memory management that allows a process to execute without loading all of its pages into physical memory. It follows that:

- A process begins execution with none of its pages in physical memory, and many page faults will occur until most of a process’s working set of pages are located in physical memory .
- The operating system copies a disk page into physical memory only if an attempt is made to access it and that page is not already in memory (i.e., if a page fault occurs).
- The operating system will page out a page from physical memory to free up space for other pages when necessary.

The advantages of demand paging are:

- It reduces the loading time of a process, as only the pages that are needed are loaded into memory.
- It reduces the memory requirement of a process, as only the pages that are used are kept in memory.
- It allows more processes to run concurrently, as the total physical memory can be shared among them.

The disadvantages of demand paging are:

- It increases the overhead of the operating system, as it has to handle page faults, page replacement, and disk I/O.
- It increases the response time of a process, as it may incur page faults and disk latency.
- It may cause thrashing, which is a situation where the operating system spends more time paging than executing processes.

The following diagram illustrates the concept of demand paging:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    Process       |    |    Page Table    |    |    Disk          |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    Logical       |    |    Page          |    |    Page          |
|    Address       |    |    Number        |    |    Number        |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    P1            |    |    1             |    |    1             |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    P2            |    |    2             |    |    2             |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    P3            |    |    3             |    |    3             |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    P4            |    |    4             |    |    4             |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    P5            |    |    5             |    |    5             |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    P6            |    |    6             |    |    6             |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    P7            |    |    7             |    |    7             |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    P8            |    |    8             |    |    8             |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
```

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|    Physical      |    |    Page Table    |    |    Disk          |
|    Memory        |    |                  |    |                  |
+------------------+