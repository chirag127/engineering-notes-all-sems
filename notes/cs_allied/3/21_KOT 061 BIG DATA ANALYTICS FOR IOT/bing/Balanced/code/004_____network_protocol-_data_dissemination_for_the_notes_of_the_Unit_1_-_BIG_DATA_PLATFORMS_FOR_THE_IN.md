# Network Protocol- Data Dissemination

- Data dissemination is the process of delivering data that matches the interest of the querying nodes in a network.
- Data dissemination is essential for IoT applications that generate massive amounts of data from various sensors and devices.
- Data dissemination protocols aim to provide efficient, reliable, and secure communication among the nodes in the network.
- Data dissemination protocols can be classified into two categories: push-based and pull-based.
  - Push-based protocols: the data source initiates the data transmission to the interested nodes without waiting for their requests. This is suitable for time-sensitive and event-driven applications, but may cause redundant transmissions and network congestion.
  - Pull-based protocols: the interested nodes send requests to the data source and wait for the data delivery. This is suitable for on-demand and query-based applications, but may cause delay and overhead in the network.
- Data dissemination protocols can also be classified into three types: flooding, gossiping, and routing.
  - Flooding: the data source broadcasts the data to all its neighbors, and each neighbor repeats the same process until the data reaches all the nodes in the network. This is simple and robust, but may cause high energy consumption and network collision.
  - Gossiping: the data source randomly selects a subset of its neighbors and sends the data to them, and each neighbor repeats the same process until the data reaches a certain percentage of the nodes in the network. This is scalable and resilient, but may cause low reliability and coverage.
  - Routing: the data source sends the data to a specific node or a group of nodes based on some criteria, such as location, distance, or interest. This is efficient and accurate, but may cause high complexity and vulnerability.