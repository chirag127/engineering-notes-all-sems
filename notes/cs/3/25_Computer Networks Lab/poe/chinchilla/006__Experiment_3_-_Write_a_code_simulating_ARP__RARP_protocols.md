## Experiment 3 - Write a code simulating ARP /RARP protocols

In this experiment, we will learn how to write a code that simulates Address Resolution Protocol (ARP) and Reverse Address Resolution Protocol (RARP) protocols. These protocols are used to map network layer addresses to physical layer addresses, and vice versa.

To simulate these protocols, we will follow the below steps:

1. Create a network topology - We need to create a network topology with multiple hosts connected to a single switch. We can use network simulation tools like GNS3, Packet Tracer, or ns-3 to create the network topology.

2. Assign IP addresses and MAC addresses - We need to assign unique IP addresses and MAC addresses to each host in the network. We can use the ifconfig command in Linux to assign IP addresses and the ifconfig -a command to view the assigned MAC addresses.

3. Implement ARP protocol - We need to implement the ARP protocol in our code to map IP addresses to MAC addresses. When a host needs to send data to another host, it first checks its ARP cache to see if it has the MAC address of the destination host. If it doesn't have the MAC address, it sends an ARP request to the network asking for the MAC address of the destination host. The destination host responds with its MAC address, and the source host updates its ARP cache with the MAC address of the destination host.

4. Implement RARP protocol - We also need to implement the RARP protocol in our code to map MAC addresses to IP addresses. When a host boots up, it sends a RARP request to the network asking for its IP address. The RARP server responds with the IP address of the host, and the host updates its IP address.

5. Test the code - Once we have implemented the ARP and RARP protocols in our code, we need to test it by sending data between hosts in the network. We can use packet sniffers like Wireshark to capture and analyze the network traffic and verify that our code is working correctly.

In conclusion, simulating the ARP and RARP protocols is an important exercise in understanding how network layer addresses are mapped to physical layer addresses. By following the above steps, we can write a code that simulates these protocols and test it in a network simulation environment.