# Channel Allocation in Cellular Systems

- Channel allocation means to allocate the available channels to the cells in a cellular system .
- When a user wants to make a call request, the channel allocation strategies assign a channel to the user based on some criteria.
- Channel allocation strategies are designed to achieve efficient use of frequencies, time slots and bandwidth .
- Channel allocation strategies can be classified into three types:
  - Fixed channel allocation (FCA): Each cell is assigned a fixed number of channels that are not shared with other cells. The channels are allocated based on the traffic demand of each cell. FCA has low overhead but high blocking probability.
  - Dynamic channel allocation (DCA): Each cell can use any channel that is not used by any neighboring cell. The channels are allocated based on the current traffic demand and interference conditions of each cell. DCA has high overhead but low blocking probability.
  - Hybrid channel allocation (HCA): A combination of FCA and DCA, where some channels are fixed and some are dynamic. HCA can balance the trade-off between overhead and blocking probability.
- The channel allocation algorithms consider the following criteria:
  - Future blocking probability in neighboring cells: The probability that a channel request in a neighboring cell will be rejected due to interference from the current cell.
  - Reuse distance: The minimum distance between two cells that use the same channel to avoid interference.
  - Usage frequency of the candidate channel: The number of times the channel has been used in the past.
  - Average blocking probability of the overall system: The probability that a channel request in any cell will be rejected due to lack of available channels.
  - Instantaneous channel occupancy distribution: The number of channels that are currently occupied in each cell.