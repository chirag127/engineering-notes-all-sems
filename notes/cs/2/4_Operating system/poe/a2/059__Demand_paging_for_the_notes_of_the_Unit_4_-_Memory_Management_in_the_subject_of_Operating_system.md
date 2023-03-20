 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Demand Paging

- Demand paging is a memory management scheme in which pages are loaded into memory only when they are accessed for the first time.
- This is in contrast to prepaging, where pages other than the active page are brought into memory in advance.
- Demand paging potentially reduces the number of page faults since pages are not brought into memory unnecessarily.
- However, demand paging may result in slower execution, since pages have to be loaded when they are needed, rather than in advance. This leads to a trade-off between page faults and throughput.
- The details of demand paging are as follows:

1. When a process first references a page, a page fault occurs. The operating system brings the page into memory from disk and updates the page table.

2. Subsequent references to the page can be satisfied from memory.

3. If memory becomes full, some pages may have to be swapped out to accommodate new pages required by the executing processes. Pages that have not been used recently are good candidates to be swapped out.

- Demand paging requires operating system support for determining which pages to swap out, for loading pages into memory when required, and for updating page tables.