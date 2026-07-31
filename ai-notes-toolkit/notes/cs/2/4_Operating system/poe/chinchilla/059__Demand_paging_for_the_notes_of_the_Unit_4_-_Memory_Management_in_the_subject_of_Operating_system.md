### Demand Paging

Demand Paging is a memory management technique used by operating systems to efficiently use memory resources. In this technique, pages are loaded into memory only when they are needed. This helps to reduce the amount of memory required to run an application and improves system performance.

#### How Demand Paging Works

Demand Paging works by dividing the physical memory into fixed-size pages and the logical memory into pages of the same size. When an application starts, only a small portion of the program is loaded into memory. As the application runs, additional pages are loaded into memory as needed.

When an application requests a page that is not currently in memory, a page fault occurs. The operating system then loads the required page into memory and updates the page table to reflect the new location of the page. The application is then allowed to continue running as normal.

#### Advantages of Demand Paging

Demand Paging has several advantages over other memory management techniques. Some of these advantages include:

- Reduced memory usage: Demand Paging only loads pages into memory when they are needed, which helps to reduce the amount of memory required to run an application.

- Improved performance: By only loading pages into memory when they are needed, Demand Paging can help to improve system performance.

- Efficient use of memory: Demand Paging helps to efficiently use memory resources by only loading pages into memory as needed.

#### Disadvantages of Demand Paging

Despite its advantages, Demand Paging also has some disadvantages that need to be considered. Some of these disadvantages include:

- Page faults: When a page fault occurs, the operating system has to load the required page into memory, which can cause a delay in the application's execution.

- Overhead: Demand Paging can introduce additional overhead into the system, which can affect system performance.

- Fragmentation: Demand Paging can lead to memory fragmentation, which can make it more difficult to allocate memory for new processes.

#### Conclusion

Demand Paging is a memory management technique that is widely used by operating systems to efficiently manage memory resources. By only loading pages into memory when they are needed, Demand Paging helps to reduce memory usage and improve system performance. However, it also has some disadvantages that need to be considered, such as page faults, overhead, and fragmentation. Overall, Demand Paging is a useful technique that can help to improve system performance when used properly.