#### InetAddress in Networking

The InetAddress class is a representation of an IP address, which is a numerical label assigned to a machine in a network. An IP address can be either 32-bit (IPv4) or 128-bit (IPv6). An instance of InetAddress encapsulates both the numerical IP address and the domain name for that address, if available. The InetAddress class can handle both unicast and multicast addresses. Unicast addresses are used to identify a single host, while multicast addresses are used to identify a group of hosts that can receive the same message.

The following diagram illustrates the basic architecture of an InetAddress:

```
+-----------------+      +-----------------+
|    InetAddress  |      |    InetAddress  |
+-----------------+      +-----------------+
| - address: int  |      | - address: int  |
| - family: int   |      | - family: int   |
| - hostName: String |   | - hostName: String |
+-----------------+      +-----------------+
| + getAddress(): byte[] |  | + getAddress(): byte[] |
| + getHostAddress(): String | | + getHostAddress(): String |
| + getHostName(): String |  | + getHostName(): String |
| + isMulticastAddress(): boolean | | + isMulticastAddress(): boolean |
| + isAnyLocalAddress(): boolean | | + isAnyLocalAddress(): boolean |
| + isLoopbackAddress(): boolean | | + isLoopbackAddress(): boolean |
| + isLinkLocalAddress(): boolean | | + isLinkLocalAddress(): boolean |
| + isSiteLocalAddress(): boolean | | + isSiteLocalAddress(): boolean |
| + isMCGlobal(): boolean |  | + isMCGlobal(): boolean |
| + isMCNodeLocal(): boolean | | + isMCNodeLocal(): boolean |
| + isMCLinkLocal(): boolean | | + isMCLinkLocal(): boolean |
| + isMCSiteLocal(): boolean | | + isMCSiteLocal(): boolean |
| + isMCOrgLocal(): boolean | | + isMCOrgLocal(): boolean |
+-----------------+      +-----------------+
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         +-----------------------+
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