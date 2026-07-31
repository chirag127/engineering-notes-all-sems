
### Paging for the Notes of Unit 4 - Memory Management in the Subject of Operating System

1. Paging is a memory management technique used by operating systems to efficiently manage memory. It divides the physical memory into fixed-size blocks called pages. 
2. Paging allows the operating system to quickly access any part of the memory by mapping virtual addresses to physical addresses. 
3. The operating system keeps track of the pages in memory using a page table. The page table is an array of page table entries (PTEs). 
4. Each PTE contains the physical address of the page in memory, as well as information about the page such as whether it is valid, read-only, or writable. 
5. When a program accesses a virtual address, the operating system looks up the corresponding PTE in the page table. 
6. If the PTE is valid, the operating system translates the virtual address to a physical address and accesses the page. 
7. If the PTE is invalid, the operating system triggers a page fault, which causes the operating system to load the page from disk into memory. 
8. Once the page has been loaded into memory, the operating system updates the page table and resumes execution of the program. 
9. Paging is an important part of memory management as it allows the operating system to efficiently manage memory and prevent programs from accessing memory that they are not allowed to access.