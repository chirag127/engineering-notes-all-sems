## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address of a device on the same network.
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address of a device on the same network.
- Both ARP and RARP are used to resolve the addresses of devices on a network, but they work in opposite directions.
- To write a code simulating ARP /RARP protocols, we need to use the following steps:

  - Import the socket and struct modules in Python. These modules provide low-level access to network interfaces and data structures.
  - Create a raw socket object using socket.AF_PACKET and socket.SOCK_RAW as the address family and socket type. This allows us to send and receive packets at the link layer.
  - Bind the socket object to a network interface using the bind() method. For example, bind(('eth0', 0)) binds the socket to the eth0 interface with any protocol.
  - Define the MAC and IP addresses of the source and destination devices. For example, src_mac = b'\x00\x0c\x29\x4f\x55\x1b' and src_ip = b'\xc0\xa8\x01\x64' are the MAC and IP addresses of the source device in hexadecimal format.
  - Construct the ARP packet using the struct.pack() method. The ARP packet consists of the following fields:

    - Hardware type: 2 bytes, specifies the type of network hardware. For Ethernet, it is 1.
    - Protocol type: 2 bytes, specifies the type of network protocol. For IPv4, it is 0x0800.
    - Hardware length: 1 byte, specifies the length of the hardware address. For MAC address, it is 6.
    - Protocol length: 1 byte, specifies the length of the protocol address. For IP address, it is 4.
    - Operation: 2 bytes, specifies the type of ARP operation. For ARP request, it is 1. For ARP reply, it is 2. For RARP request, it is 3. For RARP reply, it is 4.
    - Sender hardware address: 6 bytes, specifies the MAC address of the sender device.
    - Sender protocol address: 4 bytes, specifies the IP address of the sender device.
    - Target hardware address: 6 bytes, specifies the MAC address of the target device. For ARP request, it is 0. For ARP reply, it is the MAC address of the device that sent the ARP request. For RARP request, it is the MAC address of the device that needs an IP address. For RARP reply, it is the MAC address of the device that sent the RARP request.
    - Target protocol address: 4 bytes, specifies the IP address of the target device. For ARP request, it is the IP address of the device that needs a MAC address. For ARP reply, it is the IP address of the device that sent the ARP request. For RARP request, it is 0. For RARP reply, it is the IP address of the device that sent the RARP request.

  - For example, to construct an ARP request packet, we can use the following code:

    ```python
    arp_request = struct.pack('!HHBBH6s4s6s4s', 1, 0x0800, 6, 4, 1, src_mac, src_ip, b'\x00\x00\x00\x00\x00\x00', dst_ip)
    ```

  - To construct a RARP request packet, we can use the following code:

    ```python
    rarp_request = struct.pack('!HHBBH6s4s6s4s', 1, 0x0800, 6, 4, 3, src_mac, b'\x00\x00\x00\x00', dst_mac, b'\x00\x00\x00\x00')
    ```

  - Send the packet using the send() method of the socket object. For example, s.send(arp_request) sends the ARP request packet through the socket s.
  - Receive the packet using the recv() method of the socket object. For example, s.recv(1024) receives up to 1024 bytes of data from the socket s.
  - Unpack the packet using the struct.unpack() method. The format string should match the one used in the struct.pack() method. For example, to unpack an ARP reply packet, we can use the following code:

    ```python

```
