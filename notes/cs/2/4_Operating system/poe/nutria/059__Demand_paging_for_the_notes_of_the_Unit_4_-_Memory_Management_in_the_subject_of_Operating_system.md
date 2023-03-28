
### Demand Paging
Demand paging is a memory management technique used in operating systems to improve performance. It allows the system to only load pages of memory into RAM when they are needed, instead of loading all pages at once. This reduces the amount of RAM needed and improves the system's overall performance.

- Demand paging works by dividing memory into pages, which are blocks of memory that can be loaded into RAM.
- When a program needs to access a page of memory, the operating system checks to see if the page is already in RAM. If it is not, the operating system will load the page into RAM.
- This process is known as a page fault. The operating system will then update the page table to indicate that the page is now in RAM.
- The operating system keeps track of which pages are currently in RAM and which are not. When memory is needed, the operating system will look for the least recently used page and replace it with the new page.
- Demand paging is an effective way to improve the performance of an operating system, as it reduces the amount of RAM needed and allows the system to only load the pages of memory that are needed.