#### Link layer switches & bridges in local area network

A link layer switch or a bridge is a network device that connects multiple LANs (local area networks) together to form a larger LAN. It operates at the data link layer of the OSI model and uses MAC addresses to forward Ethernet frames from one device to another device in the same LAN or across different LANs. A switch or a bridge can also filter frames based on their MAC addresses and prevent unnecessary traffic from reaching other devices.

A possible ASCII diagram for a link layer switch or a bridge in a local area network is shown below:

```
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |   LAN Segment   |     |   LAN Segment   |     |   LAN Segment   |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             |                      |                      |
             +----------------------+----------------------+-----------------+
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  |                      |
                                  +----------------------+-----------------+
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     |                      |
                                                     +----------------------+-----------------+
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            |                      |
                                                                            +----------------------+-----------------+
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   |                      |
                                                                                                   +----------------------+-----------------+
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          |                      |
                                                                                                                          +----------------------+-----------------+
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 |                      |
                                                                                                                                                 +----------------------+-----------------+
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        |                      |
                                                                                                                                                                        +----------------------+-----------------+
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               |                      |
                                                                                                                                                                                               +----------------------+-----------------+
                                                                                                                                                                                                                      |                      |
                                                                                                                                                                                                                      |                      |

```
