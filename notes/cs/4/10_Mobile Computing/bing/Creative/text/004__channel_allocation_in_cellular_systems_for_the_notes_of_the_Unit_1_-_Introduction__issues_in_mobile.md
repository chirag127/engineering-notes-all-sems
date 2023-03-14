### Channel Allocation in Cellular Systems

Channel allocation is the process of assigning the available channels to the cells in a cellular system. Channels are the basic units of communication in wireless networks, and they can be divided into frequency channels, time slots, or codes, depending on the multiple access technique used. Channel allocation aims to maximize the system capacity, which is the number of simultaneous calls that can be supported, while minimizing the interference among neighboring cells that share the same spectrum.

There are two main types of channel allocation strategies: fixed and dynamic.

- Fixed channel allocation (FCA) assigns a predetermined set of channels to each cell, and the channels remain fixed unless manually changed by the network operator. FCA requires careful frequency planning to avoid co-channel interference and adjacent channel interference, which degrade the quality of service. FCA also suffers from inefficient utilization of the spectrum, as some cells may have more traffic demand than the available channels, while others may have idle channels. FCA can be combined with traffic-adaptive handover threshold, which allows a cell to hand over a call to a neighboring cell with lower load, or with spread spectrum, which allows a cell to borrow capacity from a nearby cell by using the same frequency with different codes.

- Dynamic channel allocation (DCA) assigns channels to cells on demand, based on the current traffic and interference conditions. DCA does not require manual frequency planning, as the channels are allocated dynamically by a central controller or by the base stations themselves. DCA can achieve higher system capacity and better spectrum utilization than FCA, as the channels are allocated according to the needs of the cells. However, DCA also introduces higher complexity and overhead, as the channel allocation decisions have to be made in real time and communicated to the base stations and mobile stations. DCA can be classified into centralized or distributed, depending on where the channel allocation decisions are made, and into borrowing or non-borrowing, depending on whether a cell can borrow channels from other cells or not.

Some examples of DCA schemes are:

- Centralized borrowing DCA: A central controller maintains a pool of free channels and assigns them to the cells that request them. If a cell has no free channels, it can borrow channels from the pool or from neighboring cells, with the permission of the central controller.

- Distributed borrowing DCA: Each cell maintains a list of free channels and assigns them to the calls that request them. If a cell has no free channels, it can borrow channels from neighboring cells, by negotiating with them directly.

- Non-borrowing DCA: Each cell has a fixed number of channels, and no borrowing is allowed. If a cell has no free channels, it can reject or queue the incoming calls. The channels are allocated to the cells based on some criteria, such as traffic demand, interference level, or location.

- Dynamic frequency selection (DFS): A special case of DCA for wireless LANs, where the access points can select the best frequency channel to operate on, based on the interference from other sources, such as radar, satellite, or weather systems. DFS is designed to prevent interference with other usages of the spectrum, and to comply with the regulations of different countries.