### Page replacement algorithms

- Page replacement algorithms refer to the techniques used by an operating system to manage the memory allocation and deallocation of the physical memory (RAM) of a computer.
- Page replacement algorithms are needed when a page fault occurs, which means that a requested page is not present in the physical memory and needs to be brought from the secondary storage (disk) to the RAM.
- The aim of page replacement algorithms is to minimize the page fault rate, which is the number of page faults per unit of time.
- Some of the common page replacement algorithms are:

  - First In First Out (FIFO): This is the simplest algorithm, which replaces the oldest page in the memory with the new page. It maintains a queue of pages in the memory and removes the page at the front of the queue when a page fault occurs .
  - Optimal Page Replacement: This is the ideal algorithm, which replaces the page that will not be used for the longest duration of time in the future. It requires the knowledge of the future page references, which is not possible in practice .
  - Least Recently Used (LRU): This is a practical approximation of the optimal algorithm, which replaces the page that has not been used for the longest time in the past. It assumes that the pages that are used recently are likely to be used again in the near future .
  - Least Frequently Used (LFU): This is another approximation of the optimal algorithm, which replaces the page that has the lowest frequency of use. It assumes that the pages that are used frequently are likely to be used again in the near future.
  - Clock: This is an efficient implementation of the LRU algorithm, which uses a circular list of pages with a pointer that moves clockwise. Each page has a use bit that is set to 1 when the page is accessed and reset to 0 by the pointer. When a page fault occurs, the pointer scans the list and replaces the first page with a use bit of 0.