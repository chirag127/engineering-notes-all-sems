### Network Protocol - Data Dissemination

- Data dissemination is the process of delivering data that matches the interest of the querying nodes in a network.
- Data dissemination is essential for IoT applications that generate massive amounts of data from various sensors and devices.
- Data dissemination protocols aim to provide efficient, reliable, and secure communication among the nodes in the network.
- Data dissemination protocols can be classified into two categories: push-based and pull-based.
  - Push-based protocols: the data source initiates the data transmission to the interested nodes without waiting for their requests. This is suitable for time-sensitive and event-driven data.
  - Pull-based protocols: the interested nodes initiate the data transmission by sending requests to the data source. This is suitable for on-demand and query-based data.
- Data dissemination protocols can also be classified into three types: flooding, gossiping, and probabilistic.
  - Flooding: the data source broadcasts the data to all its neighbors, and each neighbor repeats the same process until the data reaches all the nodes in the network. This is simple but inefficient and prone to network congestion and redundancy.
  - Gossiping: the data source randomly selects a subset of its neighbors and sends the data to them, and each neighbor repeats the same process until the data reaches a certain percentage of the nodes in the network. This is more efficient and reliable than flooding, but still suffers from some redundancy and delay.
  - Probabilistic: the data source and each neighbor decide whether to forward the data or not based on a probability function that depends on various factors, such as the number of neighbors, the distance to the destination, the energy level, and the data priority. This is more adaptive and scalable than gossiping, but requires more computation and coordination among the nodes.