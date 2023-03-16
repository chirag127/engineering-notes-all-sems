# Channel Allocation in Cellular Systems

- Channel allocation means to allocate the available channels to the cells in a cellular system .
- When a user wants to make a call request, then by using channel allocation strategies, their requests are fulfilled.
- Channel allocation strategies are designed in such a way that there is efficient use of frequencies, time slots and bandwidth .
- The channel is allocated following an algorithm which accounts the following criteria:
  - Future blocking probability in neighboring cells and reuse distance
  - Usage frequency of the candidate channel
  - Average blocking probability of the overall system
  - Instantaneous channel occupancy distribution
- There are three types of channel allocation schemes:
  - Fixed channel allocation (FCA): Each cell is assigned a fixed number of channels and the channels are not shared among the cells. If all the channels in a cell are occupied, then the call request is blocked or handed over to another cell.
  - Dynamic channel allocation (DCA): The channels are not permanently assigned to the cells, but are allocated on demand according to the traffic conditions. The channels are shared among the cells and the allocation algorithm tries to minimize the interference and maximize the utilization.
  - Hybrid channel allocation (HCA): A combination of FCA and DCA, where some channels are fixed for each cell and some are dynamically allocated. This scheme can balance the trade-off between performance and complexity.