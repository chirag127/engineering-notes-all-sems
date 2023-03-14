### Channel allocation in cellular systems

Channel allocation is the process of assigning the available channels (frequencies, time slots, codes, etc.) to the cells in a cellular system. The objective is to achieve maximum system spectral efficiency (bit/s/Hz/site) by means of frequency reuse, but still assure a certain grade of service by avoiding co-channel interference and adjacent channel interference among nearby cells or networks that share the bandwidth. 

There are two main types of channel allocation schemes: fixed and dynamic. 

- Fixed channel allocation (FCA): Each cell is given a predetermined set of frequency channels. FCA requires manual frequency planning, which is an arduous task in time-division multiple access (TDMA) and frequency-division multiple access (FDMA) based systems since such systems are highly sensitive to co-channel interference from nearby cells that are reusing the same channel. Another drawback with TDMA and FDMA systems with FCA is that the number of channels in the cell remains constant irrespective of the number of customers in that cell. This results in traffic congestion and some calls being lost when traffic gets heavy in some cells, and idle capacity in other cells. FCA can be combined with spread spectrum, which allows cell breathing to be applied, by allowing an overloaded cell to borrow capacity from a nearby cell that is sharing the same frequency. FCA can also be extended into a dynamic channel allocation (DCA) system by using a borrowing strategy in which a cell can borrow channels from the neighboring cell which is supervised by Mobile Switching Center (MSC).  

- Dynamic channel allocation (DCA): Channels are not permanently allocated to cells, but are assigned to cells according to the current traffic demand and the interference situation. DCA can improve the system performance by adapting to the traffic variations and reducing the interference level. DCA can be classified into centralized and distributed schemes. In centralized DCA, the channel allocation decision is made by a central controller (such as MSC) based on the information collected from all the cells. In distributed DCA, each cell makes its own channel allocation decision based on the local information. DCA can also be classified into demand-assigned and pre-assigned schemes. In demand-assigned DCA, channels are allocated to cells only when there is a call request. In pre-assigned DCA, channels are allocated to cells in advance based on the predicted traffic demand.  

A simple mnemonic to remember the difference between FCA and DCA is:

- FCA: Fixed channels for fixed cells
- DCA: Dynamic channels for dynamic cells

Some examples of channel allocation schemes are:

- Fixed channel allocation (FCA) with frequency reuse
- Borrowing channel allocation (BCA)
- Dynamic channel allocation (DCA) with centralized control
- Dynamic channel allocation (DCA) with distributed control
- Dynamic channel allocation (DCA) with hybrid control
- Dynamic frequency selection (DFS) for wireless LANs    

Some advantages of channel allocation schemes are:

- They can increase the system capacity and spectral efficiency by reusing the channels among different cells
- They can reduce the interference level and improve the quality of service by avoiding or minimizing the co-channel and adjacent channel interference
- They can adapt to the traffic variations and optimize the resource utilization by allocating channels according to the demand and the interference situation

Some disadvantages of channel allocation schemes are:

- They can increase the complexity and cost of the system by requiring more hardware, software, and signaling overhead for channel allocation and management
- They can introduce delays and blocking probabilities for call requests by requiring channel searching and negotiation
- They can be affected by the errors and uncertainties in the channel measurement and estimation

Some applications of channel allocation schemes are:

- Cellular systems such as GSM, CDMA, LTE, etc.
- Wireless LANs such as Wi-Fi, WiMAX, etc.
- Wireless sensor networks, ad hoc networks, etc.