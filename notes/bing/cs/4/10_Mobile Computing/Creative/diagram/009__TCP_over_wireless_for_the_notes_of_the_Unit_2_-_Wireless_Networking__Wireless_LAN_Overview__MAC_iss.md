TCP over wireless is a technique to adapt the Transmission Control Protocol (TCP) to the characteristics of wireless networks, such as packet loss, variable bandwidth, and mobility. TCP is a reliable transport protocol that ensures the correct delivery of data over the Internet Protocol (IP). However, TCP was designed for wired networks and assumes that packet loss is mainly due to congestion. Therefore, TCP responds to packet loss by reducing the sending rate, which may not be optimal for wireless networks where packet loss can be caused by other factors, such as fading, interference, or handoffs.

One way to improve the performance of TCP over wireless networks is to split the TCP connection into two parts: a wireless part and a wired part. The wireless part is handled by a specialized TCP variant that can cope with the wireless channel conditions, while the wired part is handled by the standard TCP. The splitting point can be located at the access point, the base station, or the foreign agent in a mobile network. The following diagram illustrates the basic architecture of a TCP over wireless system:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Mobile Host    |       |  Access Point   |       |  Fixed Host     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Wireless TCP   |       |  Wireless TCP   |       |  Standard TCP   |
|                 |       |  Standard TCP   |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  IP             |       |  IP             |       |  IP             |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Wireless Link  |       |  Wired Link     |       |  Wired Link     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The wireless TCP can be a modified version of TCP that uses different mechanisms to deal with packet loss, such as selective acknowledgments, fast retransmit, fast recovery, or explicit loss notification. The standard TCP can be unaware of the wireless link and operate as usual. The access point can act as a proxy that translates between the two TCP variants and hides the wireless link from the fixed host. This way, the end-to-end semantics of TCP are preserved and the performance of TCP over wireless networks is improved.