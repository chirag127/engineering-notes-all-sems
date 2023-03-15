#### Learning bridge algorithms in local area network

A bridge is a device that connects two or more local area networks (LANs) at the data link layer. A bridge can filter, forward, or flood frames based on their destination MAC addresses. A bridge maintains a forwarding table that maps MAC addresses to ports. A bridge updates its forwarding table using a learning algorithm, which works as follows:

- A bridge examines the source MAC address of each packet that arrives on a particular port and memorizes that the source address is reachable via that port. This is done by adding the source MAC address and the port to the forwarding table.
- A bridge examines the destination MAC address of each packet and looks it up in the forwarding table. If the destination address is found, the bridge forwards the packet to the corresponding port. If the destination address is not found, the bridge floods the packet to all ports except the one it arrived on.
- A bridge periodically deletes old entries from the forwarding table to avoid stale information.

The following diagram shows an example of a bridge connecting two LANs, A and B. The bridge has two ports, 1 and 2. The bridge initially has an empty forwarding table.

```
    LAN A                LAN B
+----------+         +----------+
| Host A1  |         | Host B1  |
| MAC: AA1 |         | MAC: BB1 |
+----------+         +----------+
    |                    |
    |                    |
    |                    |
    |                    |
+----------+         +----------+
| Host A2  |         | Host B2  |
| MAC: AA2 |         | MAC: BB2 |
+----------+         +----------+
    |                    |
    |                    |
    |                    |
    |                    |
    +--------------------+
           |      |
           |      |
        +------+------+
        |  Bridge   |
        | 1      2  |
        +-----------+
```

Suppose Host A1 sends a packet to Host B1. The packet arrives on port 1 of the bridge with source MAC address AA1 and destination MAC address BB1. The bridge does the following:

- It adds the entry (AA1, 1) to the forwarding table, indicating that Host A1 is reachable via port 1.
- It looks up the destination MAC address BB1 in the forwarding table, but does not find it.
- It floods the packet to all ports except port 1, which means it sends the packet to port 2.
- The packet reaches Host B1 on LAN B, and Host B1 replies to Host A1. The reply packet arrives on port 2 of the bridge with source MAC address BB1 and destination MAC address AA1. The bridge does the following:
- It adds the entry (BB1, 2) to the forwarding table, indicating that Host B1 is reachable via port 2.
- It looks up the destination MAC address AA1 in the forwarding table, and finds the entry (AA1, 1).
- It forwards the packet to port 1, where it reaches Host A1 on LAN A.

The bridge has learned the locations of Host A1 and Host B1 by observing the traffic. The forwarding table now looks like this:

```
+--------+------+
| MAC    | Port |
+--------+------+
| AA1    | 1    |
| BB1    | 2    |
+--------+------+
```

If Host A2 sends a packet to Host B2, the bridge will repeat the same process and learn the locations of Host A2 and Host B2. The forwarding table will then look like this:

```
+--------+------+
| MAC    | Port |
+--------+------+
| AA1    | 1    |
| AA2    | 1    |
| BB1    | 2    |
| BB2    | 2    |
+--------+------+
```

Now, if Host A1 sends another packet to Host B1, the bridge will not flood the packet, but forward it directly to port 2, since it knows the destination MAC address. Similarly, if Host B2 sends a packet to Host A2, the bridge will forward it directly to port 1. The bridge has effectively reduced the traffic on both LANs by learning the MAC addresses of the hosts.
