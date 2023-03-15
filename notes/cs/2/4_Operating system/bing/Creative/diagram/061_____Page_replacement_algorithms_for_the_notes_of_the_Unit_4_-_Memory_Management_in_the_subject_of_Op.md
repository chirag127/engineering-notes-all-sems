### Page replacement algorithms

Page replacement algorithms are the techniques used by an operating system to manage the memory allocation and deallocation of the physical memory (RAM) of a computer. When a program requests a page of memory that is not present in the RAM, a page fault occurs and the operating system has to decide which page to replace with the requested one. The goal of page replacement algorithms is to minimize the page fault rate and improve the performance of the system.

Some of the common page replacement algorithms are:

- **First In First Out (FIFO)**: This is the simplest page replacement algorithm. In this algorithm, the operating system maintains a queue of pages in the RAM and replaces the oldest page (the one at the front of the queue) with the new page. This algorithm is easy to implement but may not be optimal as it does not consider the frequency or recency of page usage.

- **Optimal Page Replacement**: This is the best page replacement algorithm as this algorithm replaces the page that will not be used for the longest duration of time in the future. This algorithm guarantees the minimum number of page faults but it is impossible to implement in practice as it requires the knowledge of the future page requests.

- **Least Recently Used (LRU)**: This is a practical approximation of the optimal page replacement algorithm. In this algorithm, the operating system replaces the page that has not been used for the longest period of time in the past. This algorithm assumes that the pages that have been used recently are more likely to be used again in the near future. This algorithm can be implemented using a stack or a linked list.

- **Least Frequently Used (LFU)**: This is another approximation of the optimal page replacement algorithm. In this algorithm, the operating system replaces the page that has the lowest frequency of usage. This algorithm assumes that the pages that have been used more often are more likely to be used again in the near future. This algorithm can be implemented using a counter or a priority queue.

- **Clock**: This is a variation of the FIFO algorithm that uses a circular list of pages and a pointer that moves through the list. Each page has a reference bit that indicates whether it has been accessed recently or not. When a page fault occurs, the pointer checks the reference bit of the current page. If it is 0, the page is replaced with the new page and the pointer moves to the next page. If it is 1, the reference bit is set to 0 and the pointer moves to the next page. This process is repeated until a page with a reference bit of 0 is found. This algorithm is also known as the second chance algorithm.

: https://www.prepbytes.com/blog/operating-system/page-replacement-algorithms-in-os/
: https://examradar.com/page-replacement-algorithms/
: https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/
: https://www.scaler.com/topics/operating-system/page-replacement-algorithm/
: https://eng.libretexts.org/Courses/Delta_College/Operating_System%3A_The_Basics/08%3A_Virtual_Memory/8.1%3A_Memory_Paging/8.1.1%3A_Memory_Paging_-_Page_Replacement