# Address Mapping and Replacement

## Address Mapping

- Address mapping is a process of determining a logical address knowing the physical address of the device and determining the physical address by knowing the logical address of the device.
- Address mapping is required when a packet is routed from source host to destination host in the same or different network.
- Address mapping can be done using different techniques, such as pages, segments, or cache blocks.
- Pages are fixed-size blocks of data that are stored in the main memory and the secondary memory.
- Segments are variable-size blocks of data that are stored in the main memory and the secondary memory.
- Cache blocks are fixed-size blocks of data that are stored in the cache memory and the main memory.
- Address mapping using pages involves dividing the logical address space and the physical address space into equal-sized pages and frames, respectively.
- Address mapping using segments involves dividing the logical address space and the physical address space into segments of different sizes, depending on the program modules.
- Address mapping using cache blocks involves dividing the main memory into equal-sized blocks and mapping them to the cache memory using a mapping function.
- The mapping function can be direct, associative, or set-associative.
- Direct mapping involves mapping each block of main memory to a specific line of cache memory using a modulo operation.
- Associative mapping involves mapping each block of main memory to any line of cache memory using a tag and a comparator.
- Set-associative mapping involves mapping each block of main memory to a specific set of cache memory, and then using associative mapping within the set.

## Address Replacement

- Address replacement is a process of selecting a block of memory to be replaced by a new block of memory when the memory is full or when a cache miss occurs.
- Address replacement is necessary to maintain the consistency and efficiency of the memory system.
- Address replacement can be done using different algorithms, such as FIFO, LRU, LFU, or Random.
- FIFO (First In First Out) algorithm involves replacing the block that was brought into the memory first.
- LRU (Least Recently Used) algorithm involves replacing the block that was least recently accessed in the memory.
- LFU (Least Frequently Used) algorithm involves replacing the block that was least frequently accessed in the memory.
- Random algorithm involves replacing a block randomly chosen from the memory.
- The performance of the address replacement algorithms depends on the access pattern and the size of the memory.
- The goal of the address replacement algorithms is to minimize the number of page faults or cache misses.