 Here is the content in markdown format for the given topic:

## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

1. **Router configuration**
- Connect to the router console and enter configuration mode
- Set router hostname: `hostname R1`
- Enable secret password for privileged exec mode
- Configure interface IP addresses and netmasks
- Configure static or dynamic routing protocols like OSPF or RIP
- Configure access control lists (ACLs) to filter traffic
- Save the configuration

2. **Hub configuration**
- Hubs are layer 1 devices that simply forward all traffic to all ports
- No configuration required for hub as it has no management capabilities
- Only purpose is to connect multiple devices and forward broadcasts

3. **Switch configuration**
- Connect to switch console and enter configuration mode
- Set switch hostname: `hostname S1`
- Enable secret password for privileged exec mode
- Configure interface IP addresses (if managed switch)
- Configure VLANs and assign interfaces to VLANs
- Configure spanning tree protocol (STP) to prevent layer 2 loops
- Configure inter-vlan routing if layer 3 switch
- Configure port security to allow/deny specific MAC addresses
- Save the configuration

**Advantages:**
- Increased security and control over network
- Flexibility to customize network based on requirements
- Remote management capability

**Disadvantages:**
- Requirement of technical knowledge to configure devices
- Possibility of misconfiguration leading to network issues
- Time and effort required to configure and maintain devices

**Examples and applications:**
- Used in enterprises, data centers, ISPs to build scalable networks
- Core routers and switches are powerful devices used in network backbone
- Access routers and switches are used to provide connectivity to end devices

**Diagrams:**

[Router diagram]

[Switch diagram]

[Hub diagram]