### Channel allocation in cellular systems

- Channel allocation means to assign the available channels (frequencies, time slots, codes, etc.) to the cells in a cellular system .
- Channel allocation is a key issue in cellular systems, as it affects the capacity, quality, and interference of wireless communications.
- Channel allocation strategies can be classified into three categories:
  - Fixed channel allocation (FCA): Each cell is assigned a fixed number of channels, regardless of the traffic demand. The channels are reused in different cells according to a reuse pattern. FCA is simple and robust, but it may cause wastage of channels or blocking of calls.
  - Dynamic channel allocation (DCA): The channels are not permanently assigned to any cell, but are allocated on demand according to the traffic load and interference conditions. DCA can adapt to traffic variations and improve the spectrum efficiency, but it requires more complex coordination and signaling.
  - Hybrid channel allocation (HCA): A combination of FCA and DCA, where some channels are fixed and some are dynamic. HCA can balance the trade-off between simplicity and adaptability, but it may introduce more interference and handoff failures.
- Channel allocation algorithms can be based on different criteria, such as:
  - Future blocking probability in neighboring cells: The probability that a channel request in a neighboring cell will be rejected due to the lack of available channels.
  - Reuse distance: The minimum distance between two cells that use the same channel, which determines the level of co-channel interference.
  - Usage frequency of the candidate channel: The number of times that a channel has been used in a given period, which reflects the channel quality and availability.
  - Average blocking probability of the overall system: The average probability that a channel request in any cell will be rejected due to the lack of available channels.
  - Instantaneous channel occupancy distribution: The distribution of the number of occupied channels in each cell, which indicates the traffic load and congestion.