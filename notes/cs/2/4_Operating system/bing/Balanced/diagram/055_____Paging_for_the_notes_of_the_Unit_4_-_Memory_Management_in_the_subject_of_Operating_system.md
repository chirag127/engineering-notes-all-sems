### Paging

Paging is a memory management scheme that allows the operating system to store and retrieve data from secondary storage for use in main memory. In this scheme, the operating system retrieves data from secondary storage in same-size blocks called pages.

The main memory is divided into small fixed-size blocks of physical memory, which are called frames. The size of a frame is equal to the size of a page. The operating system maintains a page table for each process, which maps the logical address of a page to the physical address of a frame.

The advantages of paging are:

- It eliminates the need for contiguous allocation of physical memory, which reduces external fragmentation and compaction.
- It simplifies memory allocation and deallocation, as the operating system only needs to manage pages and frames, not variable-sized segments.
- It allows the operating system to use the secondary storage as an extension of the main memory, which increases the effective size of the address space.

The disadvantages of paging are:

- It introduces internal fragmentation, as a page may not be fully occupied by a process.
- It increases the overhead of the operating system, as it needs to maintain and update the page tables and perform page transfers between the main memory and the secondary storage.
- It may cause page faults, which occur when a process accesses a page that is not present in the main memory. A page fault requires the operating system to bring the requested page from the secondary storage to the main memory, which may cause a significant delay.

An example of paging is shown in the following diagram:

```
+----------------+    +----------------+    +----------------+
| Logical memory |    | Page table     |    | Physical memory|
|                |    |                |    |                |
| +-----+        |    | +-----+-----+  |    | +-----+        |
| |Page |        |    | |Page |Frame|  |    | |Frame|        |
| |  0  |--------+----> |  0  |  2  |  +----> |  0  |        |
| +-----+        |    | +-----+-----+  |    | +-----+        |
| |Page |        |    | |Page |Frame|  |    | |Frame|        |
| |  1  |--------+----> |  1  |  4  |  +----> |  1  |        |
| +-----+        |    | +-----+-----+  |    | +-----+        |
| |Page |        |    | |Page |Frame|  |    | |Frame|        |
| |  2  |--------+----> |  2  |  1  |  +----> |  2  |        |
| +-----+        |    | +-----+-----+  |    | +-----+        |
| |Page |        |    | |Page |Frame|  |    | |Frame|        |
| |  3  |--------+----> |  3  |  3  |  +----> |  3  |        |
| +-----+        |    | +-----+-----+  |    | +-----+        |
| |Page |        |    | |Page |Frame|  |    | |Frame|        |
| |  4  |--------+----> |  4  |  0  |  +----> |  4  |        |
| +-----+        |    | +-----+-----+  |    | +-----+        |
+----------------+    +----------------+    +----------------+
```