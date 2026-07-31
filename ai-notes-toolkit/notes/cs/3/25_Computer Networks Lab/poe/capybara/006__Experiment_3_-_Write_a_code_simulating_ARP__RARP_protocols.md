## Experiment 3 - Write a code simulating ARP /RARP protocols

In this experiment, we will be writing a code that simulates the ARP (Address Resolution Protocol) and RARP (Reverse Address Resolution Protocol) protocols. These protocols are used to map a network address (such as an IP address) to a physical address (such as a MAC address) and vice versa.

Here are the steps to simulate ARP/RARP protocols using code:

1. First, we need to create a table to store the IP address and MAC address mappings. This table will be used to look up the MAC address of a device when given its IP address and vice versa. We can create this table using a dictionary in Python.

2. Next, we need to simulate the ARP protocol. The ARP protocol is used to map an IP address to a MAC address. In this simulation, we will assume that the device sending the ARP request knows the IP address of the device whose MAC address it wants to find. The steps to simulate the ARP protocol are:

    a. The requesting device broadcasts an ARP request message to all devices on the network, asking for the MAC address of the device with the specified IP address.
    
    b. The device with the specified IP address responds with its MAC address.
    
    c. The requesting device receives the MAC address and stores it in its ARP table for future use.

3. Finally, we need to simulate the RARP protocol. The RARP protocol is used to map a MAC address to an IP address. In this simulation, we will assume that the device sending the RARP request knows the MAC address of the device whose IP address it wants to find. The steps to simulate the RARP protocol are:

    a. The requesting device broadcasts a RARP request message to all devices on the network, asking for the IP address of the device with the specified MAC address.
    
    b. The device with the specified MAC address responds with its IP address.
    
    c. The requesting device receives the IP address and stores it in its RARP table for future use.

By simulating the ARP and RARP protocols using code, we can better understand how these protocols work and how devices on a network communicate with each other.