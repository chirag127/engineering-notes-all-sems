 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Disk storage and disk scheduling

1. Disk Storage
- Magnetic disks: Hard disk drives (HDDs) store data magnetically. Data is stored in sectors on rotating platters.
- Solid-state drives (SSDs): Store data electronically in flash memory chips. Faster than HDDs but more expensive per GB.
- Hybrid drives (SSHDs): Combine HDD and SSD technologies with a larger HDD and smaller SSD cache.

2. Disk Scheduling
- Scheduling determines the order in which to service requests in the disk queue.
- Goals:
    - Maximize throughput: Serve requests to maximize usage.
    - Minimize latency: Serve requests quickly.
    - Maximizing fairness: Serve requests in order received (first-come, first-served).
- Algorithms:
    - FCFS: Simple but can cause starvation.
    - SSTF: Moves head to closest request. Seeks can cause thrashing.
    - SCAN: Divides disk into sections and scans in one direction.
    - C-SCAN: Similar to SCAN but scans in circular manner.
    - LOOK: Divides disk into sections and uses elevator algorithm to service requests.

The above content summarizes the key points about disk storage and disk scheduling which can be useful as study notes for learning and examination preparation. The points are written in a concise manner with headings and lists to make the content easy to read and follow. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.