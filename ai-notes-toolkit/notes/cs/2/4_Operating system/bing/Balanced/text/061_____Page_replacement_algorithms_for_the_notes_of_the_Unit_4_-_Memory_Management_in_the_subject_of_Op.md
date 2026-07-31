### Page replacement algorithms

- Page replacement algorithms are techniques used by an operating system to manage the memory allocation and deallocation of the physical memory (RAM) of a computer.
- Page replacement algorithms determine how the victim page (the page to be replaced) is selected when a page fault occurs. The aim is to minimize the page fault rate.
- A page fault happens when a running program accesses a memory page that is mapped into the virtual address space but not loaded in physical memory.
- Some common page replacement algorithms are:
  - First In First Out (FIFO): This is the simplest algorithm. In this algorithm, the operating system maintains a queue of all the pages in memory. The oldest page is selected as the victim page and replaced by the new page.
  - Optimal Page replacement: This is the best algorithm as this algorithm replaces the page that will not be used for the longest duration of time in the future. However, this algorithm is not feasible in practice as it requires the knowledge of the future page references.
  - Least Recently Used (LRU): This algorithm replaces the page that has not been used for the longest period of time. This algorithm approximates the optimal page replacement by using the past page references as an indicator of the future ones.
  - Least Frequently Used (LFU): This algorithm replaces the page that has the lowest frequency of use. This algorithm assumes that the page with the least frequency of use is likely to be used less in the future.
  - Clock: This algorithm uses a circular list of pages with a pointer that moves through the list. Each page has a use bit that is set when the page is accessed. When a page fault occurs, the pointer scans the list and replaces the first page with the use bit cleared. If all the pages have the use bit set, the pointer clears the use bit of each page and repeats the scan.