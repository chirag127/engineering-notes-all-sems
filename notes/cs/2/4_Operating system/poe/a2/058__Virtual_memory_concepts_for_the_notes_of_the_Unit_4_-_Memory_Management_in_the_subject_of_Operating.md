 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Virtual memory concepts for the notes of the Unit 4 - Memory Management in the subject of Operating system.

1. Virtual memory is a memory management technique where the operating system provides an "illusion" of very large memory size by using  the concept of virtual memory using HDD.
2. The main memory (RAM) is mapped into virtual address space which is logically contiguous. Whenever a program accesses an address in the virtual address space, the corresponding physical address is located and accessed in main memory. If the required page is not present in main memory, it leads to page fault and the page is brought in from the HDD to main memory.
3. The OS keeps track of pages in main memory using page tables. Page tables contain mapping between virtual pages and physical pages in main memory. The pages in main memory can be swapped out to accommodate more important pages leading to page replacement.
4. The main advantages of virtual memory are - it enables execution of programs larger than the actual RAM size and it increases the effective processing speed by reducing the frequency of accessing the HDD as only required pages are swapped in on demand. The main disadvantage is increased access time for pages since they have to be fetched from and stored to the HDD.
5. The two main functions of virtual memory are translation and management. The translation function translates the virtual address to physical address using page tables and the management function performs the swapping of pages between the RAM and HDD.

The content summarizes the key concepts of virtual memory in a formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or expand the content in any way.