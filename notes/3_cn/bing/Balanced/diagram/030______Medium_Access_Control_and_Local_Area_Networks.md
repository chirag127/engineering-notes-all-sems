Medium Access Control (MAC) is a protocol that regulates how devices access and share a common communication channel in a Local Area Network (LAN). There are two main approaches to MAC: contention and token-passing. Contention is a first-come, first-serve approach, where devices compete for the channel and may experience collisions. Token-passing is a cooperative approach, where devices take turns to use the channel by passing a token.

A diagram of contention-based MAC is shown below:

```
    +--------+        +--------+        +--------+
    | Device |        | Device |        | Device |
    +--------+        +--------+        +--------+
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        +---------------------------------+
                 Shared Channel
```

A diagram of token-passing MAC is shown below:

```
    +--------+        +--------+        +--------+
    | Device |        | Device |        | Device |
    +--------+        +--------+        +--------+
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        |                |                |
        +---------------------------------+
                 Shared Channel
                   +-----+
                   |Token|
                   +-----+
```

The token circulates among the devices in a predefined order. Only the device that holds the token can transmit data on the channel. After transmission, the device passes the token to the next device in the order.