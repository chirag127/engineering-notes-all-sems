Multiple access protocols are a set of protocols operating in the Medium Access Control sublayer (MAC sublayer) of the Open Systems Interconnection (OSI) model. These protocols allow a number of nodes or users to access a shared network channel . Depending on the channel's state (idle or busy), each station transmits the data frame. However, if more than one station sends the data over a channel, there may be a collision or data conflict.

There are different types of multiple access protocols, such as random access protocols, controlled access protocols, and channelization protocols. Random access protocols allow any station to transmit data at any time without coordination with other stations, such as ALOHA, CSMA, CSMA/CD, and CSMA/CA. Controlled access protocols require stations to obtain permission before transmitting data, such as reservation, polling, and token passing. Channelization protocols divide the channel into smaller units and assign them to different stations, such as frequency division multiple access (FDMA), time division multiple access (TDMA), and code division multiple access (CDMA).

The following diagram illustrates the basic architecture of a multiple access protocol in medium access control:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Station 1    |     |    Station 2    |     |    Station 3    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Station 4    |     |    Station 5    |     |    Station 6    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows six stations that want to access a shared network channel. Each station has a transmitter and a receiver that can send and receive data frames over the channel. The channel is a broadcast medium that can carry one data frame at a time. If two or more stations transmit data frames at the same time, a collision occurs and the data frames are corrupted. The multiple access protocol is responsible for coordinating the access of the stations to the channel and resolving any collisions that may occur. Different multiple access protocols use different techniques to achieve this goal, such as carrier sensing, collision detection, collision avoidance, reservation, polling, token passing, frequency division, time division, and code division .