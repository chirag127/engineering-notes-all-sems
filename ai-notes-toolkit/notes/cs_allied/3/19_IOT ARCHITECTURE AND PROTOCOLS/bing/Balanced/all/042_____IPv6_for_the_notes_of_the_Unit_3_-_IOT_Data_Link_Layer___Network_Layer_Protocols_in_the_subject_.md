# IPv6

IPv6 is the next generation Internet Protocol (IP) standard intended to eventually replace IPv4, the protocol many Internet services still use today. IPv6 is designed to solve many of the problems of IPv4, such as address depletion, security, auto-configuration, extensibility, and so on. IPv6 expands the capabilities of the Internet to enable new kinds of applications, including peer-to-peer and mobile applications.

Some of the important features and uses of IPv6 are:

- IPv6 addresses: An IPv6 address uses 128 bits, four times more than the IPv4 address, which uses only 32 bits. This allows for a much larger address space, which can accommodate more devices and networks on the Internet. IPv6 addresses are written using hexadecimal, as opposed to dotted decimal in IPv4. For example, an IPv6 address may look like this: 2001:db8:0:1234:0:567:8:1.
- Network and node addresses: In IPv4, address classes were used to split an address into two components: a network component and a node component. In IPv6, the address is divided into two parts: a 64-bit network prefix and a 64-bit interface identifier. The network prefix identifies the network to which the device belongs, and the interface identifier identifies the device on that network. The interface identifier can be derived from the MAC address of the device, or randomly generated.
- IPv6 address types and scope: IPv6 defines different types of addresses for different purposes and scopes. Some of the common address types are:

  - Link-local: These addresses are used for communication within a single network segment, such as a LAN. They are not routable on the Internet, and start with fe80::/10.
  - Global unicast: These addresses are used for communication on the global Internet, and are unique and routable. They start with 2000::/3.
  - Unique local: These addresses are used for communication within a private network, such as a VPN or a corporate network. They are not routable on the Internet, and are similar to IPv4 private addresses. They start with fc00::/7.
  - Multicast: These addresses are used for sending data to multiple recipients at the same time, such as video streaming or online gaming. They start with ff00::/8.
  - Anycast: These addresses are used for sending data to the nearest or best available node that provides a certain service, such as DNS or CDN. They are assigned from the global unicast address space, and are shared by multiple nodes.
  - Loopback: This address is used for testing the connectivity of the device to itself. It is equivalent to the IPv4 address 127.0.0.1, and is represented by ::1 in IPv6.

- Using IPv6 addresses in uniform resource locators (URLs): To use an IPv6 address in a URL, the address must be enclosed in square brackets, followed by the port number if needed. For example, http://[2001:db8:0:1234:0:567:8:1]:80/index.html.
- IPv6 loopback: The IPv6 loopback is a special address that is used for testing the connectivity of the device to itself. It is equivalent to the IPv4 address 127.0.0.1, and is represented by ::1 in IPv6. For example, to ping the loopback address, one can use the command ping ::1.