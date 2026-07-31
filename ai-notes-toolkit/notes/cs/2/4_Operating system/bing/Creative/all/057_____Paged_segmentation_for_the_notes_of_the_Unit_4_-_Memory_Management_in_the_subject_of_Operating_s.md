# Paged Segmentation

Paged segmentation is a memory management technique that combines the advantages of paging and segmentation. It allows the logical address space of a process to be divided into variable-sized segments, and each segment to be further divided into fixed-sized pages. This way, the process can have a non-contiguous physical address space, and the memory can be allocated more efficiently.

Some of the main points of paged segmentation are:

- The logical address of a process consists of two parts: a segment number and an offset within the segment.
- The segment number is used to index a segment table, which contains the base address and the limit of each segment in the process.
- The offset within the segment is divided into two parts: a page number and a displacement within the page.
- The page number is used to index a page table, which contains the frame number of each page in the segment.
- The displacement within the page is added to the frame number to obtain the physical address of the byte in memory.
- The segment table and the page tables are stored in memory and managed by the operating system.
- The segment table and the page tables are also cached in special registers called segment table base register (STBR) and segment table length register (STLR) for faster access.
- The segment table base register (STBR) contains the base address of the segment table in memory, and the segment table length register (STLR) contains the number of entries in the segment table.
- The segment number is compared with the segment table length register (STLR) to check for segmentation violation, i.e., if the segment number is out of bounds.
- The base address of the segment is added to the page number to obtain the address of the page table entry in memory.
- The page table entry contains a valid bit, a protection bit, and a frame number. The valid bit indicates if the page is present in memory or not, the protection bit indicates the access rights of the page, and the frame number indicates the physical location of the page in memory.
- The valid bit and the protection bit are checked for page fault and protection violation, i.e., if the page is not present in memory or if the access rights are violated.
- The frame number is added to the displacement within the page to obtain the physical address of the byte in memory.

The following diagram illustrates the paged segmentation technique:

![Paged Segmentation](https://www.baeldung.com/wp-content/uploads/sites/4/2021/10/paged-segmentation.png)