 Here is the formal notes on the topic of Address Mapping and Replacement for Unit 4 - Memory in Computer Organization and Architecture:

### Address Mapping

1. Address mapping is the process of converting virtual addresses to physical addresses. This is done to provide an abstraction from limited physical memory and enable processes to have a large virtual address space.
2. The two common address mapping techniques are:
- Page mapping: The virtual address space is divided into fixed-size blocks called pages. The pages are mapped to physical memory pages.
- Segment mapping: The virtual address space is divided into variable-sized segments. The segments are mapped to physical memory segments.
3. The hardware that performs address mapping is present in the Memory Management Unit (MMU). The mapping is done using a table called the Page Table or Segment Table which contains the mapping information.
4. Address mapping enables the below key features:
- Relocation: Physical memory can be allocated to processes dynamically.
- Protection: Access rights can be set for pages or segments.
- Sharing: Pages can be shared between multiple processes.
- Swapping: Pages can be swapped out to the hard disk when not in use.

### Replacement Algorithms

1. When all frames are full, a page replacement algorithm is used to determine which page needs to be replaced. The general goals of a replacement algorithm are:
- Maximizing the hit rate: Choose least recently used pages as they are less likely to be accessed soon.
- Minimizing the number of writes to the swap disk.
2. Common page replacement algorithms are:
- First In First Out (FIFO): Oldest page is replaced first. Simple but can result in unnecessary swapping.
- Least Recently Used (LRU): Least recently used page is replaced. Requires keeping track of the usage of pages which can be complex to implement.
- Clock algorithm: An approximation of LRU which is easier to implement using a clock hand.
3. The performance of a replacement algorithm depends on the memory access pattern of the processes and the nature of the workload. No single algorithm is best for all workloads. The operating system can choose an algorithm based on the workload.