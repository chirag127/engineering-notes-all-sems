Switching techniques and multiplexing are two concepts that are related to data transmission in computer networks. Switching techniques are methods of connecting multiple devices or nodes in a network, such that they can communicate with each other efficiently and reliably. Multiplexing is a technique of combining multiple signals or data streams into one signal or channel, such that they can share the same transmission medium or link.

There are three main types of switching techniques: circuit switching, message switching, and packet switching. Each of them has its own advantages and disadvantages, depending on the application and the network requirements. The following diagram illustrates the basic architecture of each switching technique:

```
Circuit switching: A dedicated path is established between the source and the destination nodes for the duration of the communication.

  +-----+      +-----+      +-----+      +-----+
  |Node |      |Node |      |Node |      |Node |
  |  A  |------|  B  |------|  C  |------|  D  |
  +-----+      +-----+      +-----+      +-----+
     |            |            |            |
     |            |            |            |
  +-----+      +-----+      +-----+      +-----+
  |Node |      |Node |      |Node |      |Node |
  |  E  |------|  F  |------|  G  |------|  H  |
  +-----+      +-----+      +-----+      +-----+

Message switching: The whole message is treated as a data unit and is stored and forwarded by each intermediate node until it reaches the destination node.

  +-----+      +-----+      +-----+      +-----+
  |Node |      |Node |      |Node |      |Node |
  |  A  |----->|  B  |----->|  C  |----->|  D  |
  +-----+      +-----+      +-----+      +-----+
     |            |            |            |
     |            |            |            |
  +-----+      +-----+      +-----+      +-----+
  |Node |      |Node |      |Node |      |Node |
  |  E  |----->|  F  |----->|  G  |----->|  H  |
  +-----+      +-----+      +-----+      +-----+

Packet switching: The message is broken down into smaller chunks called packets, which are transmitted independently and may take different paths to reach the destination node.

  +-----+      +-----+      +-----+      +-----+
  |Node |      |Node |      |Node |      |Node |
  |  A  |----->|  B  |----->|  C  |----->|  D  |
  +-----+      +-----+      +-----+      +-----+
     | \          | \          | \          | \
     |  \         |  \         |  \         |  \
     |   \        |   \        |   \        |   \
     |    \       |    \       |    \       |    \
     |     \      |     \      |     \      |     \
     |      \     |      \     |      \     |      \
     |       \    |       \    |       \    |       \
     |        \   |        \   |        \   |        \
     |         \  |         \  |         \  |         \
     |          \ |          \ |          \ |          \
     |           \|           \|           \|           \
  +-----+      +-----+      +-----+      +-----+
  |Node |      |Node |      |Node |      |Node |
  |  E  |----->|  F  |----->|  G  |----->|  H  |
  +-----+      +-----+      +-----+      +-----+
```

There are also different types of multiplexing techniques, such as frequency-division multiplexing (FDM), time-division multiplexing (TDM), wavelength-division multiplexing (WDM), and statistical multiplexing. Each of them has its own way of dividing the bandwidth or time slots of a channel among multiple signals or data streams. The following diagram illustrates the basic principle of each multiplexing