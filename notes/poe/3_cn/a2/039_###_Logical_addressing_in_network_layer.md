 Here is the content written in markdown format on the topic ### Logical addressing in network layer:

### Logical addressing in network layer

The network layer uses logical addresses to identify the source and destination machines. The logical addresses are mapped to physical addresses using address resolution protocols.

The key points to remember about logical addressing are:

1. Logical addresses areindependent of physical topology and physical components of the network. They remain same even if the network topology changes or physical components like NICs are changed.
2. Logical addresses are arranged in a hierarchical structure which makes routing efficient. The IP addresses used for logical addressing are hierarchical and structured.
3. Multiple logical addresses can be mapped to a single physical address using techniques like network address translation (NAT). This helps in efficient utilization of limited IP address space.
4. Broadcast domains are identified using logical addresses. All machines in a broadcast domain will have same initial digits in their logical address.
5. Subnetting is performed on logical addresses to create smaller broadcast domains and increase efficiency. The subnet mask is used to extract subnet information and identify the subnet an IP address belongs to.

Some mnemonics to remember:

-Logical addresses are like house addresses. They identify machines like house addresses identify houses, independent of the internal structure or changes made.
-The hierarchical structure of IP addresses can be remembered as ' troops marching order' where the army (network), battalion (subnet) and soldier (host) can be identified from the address.

[Detailed diagrams, examples, codes can be added here if required to explain the concepts]

Logical addressing is a key concept in understanding how communication happens in a network. Understanding the key points about logical addressing will help in grasping other network layer concepts and protocols easily.