Data broadcasting is a group communication method in wireless LANs, where a sender transmits data to multiple receivers simultaneously. Data broadcasting can be used for various purposes, such as updating software, distributing news, or sending emergency alerts. Data broadcasting can be performed in two ways: unicast mode or multicast mode.

Unicast mode is when the sender transmits a copy of the data to each receiver individually. This mode is inefficient and consumes a lot of bandwidth and processing power. Unicast mode is used when the network does not support multicasting or when the number of receivers is very small.

Multicast mode is when the sender transmits a single copy of the data to a group of receivers that share a common address. This mode is efficient and reduces the overhead on the sender and the network. Multicast mode is used when the network supports multicasting and when the number of receivers is large.

The following diagram illustrates the basic architecture of a wireless LAN with data broadcasting in multicast mode:

```
    +-----------------+       +-----------------+
    |                 |       |                 |
    |  Wireless LAN   |       |  Wired LAN      |
    |  Controller     |       |  Router         |
    |                 |       |                 |
    +-----------------+       +-----------------+
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |  +-----------------+
            |                         |  |                 |
            |                         |  |  Data Source    |
            |                         |  |                 |
            |                         |  +-----------------+
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |  +-----------------+
            |                         |  |                 |
            |                         |  |  Data Receiver  |
            |                         |  |                 |
            |                         |  +-----------------+
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |  +-----------------+
            |                         |  |                 |
            |                         |  |  Data Receiver  |
            |                         |  |                 |
            |                         |  +-----------------+
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |  +-----------------+
            |                         |  |                 |
            |                         |  |  Data Receiver  |
            |                         |  |                 |
            |                         |  +-----------------+
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |  +-----------------+
            |                         |  |                 |
            |                         |  |  Data Receiver  |
            |                         |  |                 |
            |                         |  +-----------------+
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |  +-----------------+
            |                         |  |                 |
            |                         |  |  Data Receiver  |
            |                         |  |                 |
            |                         |  +-----------------+
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |  +-----------------+
            |                         |  |                 |
            |                         |  |  Data Receiver  |
            |                         |  |                 |
            |                         |  +-----------------+
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |  +-----------------+
            |                         |  |                 |
            |                         |  |  Data Receiver  |
            |                         |  |                 |
            |                         |  +-----------------+
            |                         |
            |