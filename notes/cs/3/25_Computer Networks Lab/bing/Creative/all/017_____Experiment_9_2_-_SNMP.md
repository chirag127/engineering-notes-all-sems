# Experiment 9.2 - SNMP

## Objective
- To learn about the Simple Network Management Protocol (SNMP) and its components.
- To use SNMP commands to monitor and manage network devices.

## Theory
- SNMP is an application layer protocol that allows network administrators to remotely monitor and manage network devices such as routers, switches, servers, printers, etc.
- SNMP uses a client-server model, where the client is called a manager and the server is called an agent.
- The manager sends requests to the agent using SNMP messages, and the agent responds with the requested information or performs the requested action.
- The agent also sends unsolicited messages to the manager, called traps or notifications, to report significant events or errors.
- SNMP messages are encoded using the Abstract Syntax Notation One (ASN.1) and transmitted using the User Datagram Protocol (UDP).
- SNMP has three versions: SNMPv1, SNMPv2c, and SNMPv3. The main differences among them are the security and authentication mechanisms.
- SNMP uses a hierarchical data structure called the Management Information Base (MIB), which defines the variables that can be accessed by the manager and the agent.
- The MIB consists of a collection of objects, each identified by a unique name called an Object Identifier (OID).
- The OID follows a tree-like structure, where each node represents a specific organization, standard, or vendor.
- The MIB objects can be either scalar (single-valued) or tabular (multi-valued), and can have different data types, such as integer, string, counter, gauge, etc.
- The MIB objects can be read-only or read-write, depending on the access rights assigned to them.
- The MIB objects can be accessed using four basic SNMP operations: GET, GETNEXT, SET, and TRAP.
- The GET operation is used to retrieve the value of a specific MIB object, identified by its OID.
- The GETNEXT operation is used to retrieve the value of the next MIB object in the OID tree, starting from a given OID.
- The SET operation is used to modify the value of a writable MIB object, identified by its OID.
- The TRAP operation is used by the agent to send a notification to the manager, containing the OID and the value of the MIB object that triggered the event.

## Procedure
- To perform this experiment, you will need a network simulator software, such as Packet Tracer, GNS3, or NetSim, and a SNMP manager software, such as SNMPc, Net-SNMP, or SNMP Tester.
- You will also need to configure the network devices (routers, switches, etc.) with the appropriate IP addresses, SNMP agent settings, and MIB files.
- The following steps are an example of how to use SNMP commands to monitor and manage network devices, using Packet Tracer and SNMP Tester as the tools.

1. Launch Packet Tracer and create a simple network topology, consisting of a PC, a router, and a switch, as shown in the figure below.

![network topology](https://i.imgur.com/0JY8w5R.png)

2. Assign IP addresses to the PC and the router interfaces, as shown in the table below.

| Device | Interface | IP Address | Subnet Mask |
|--------|-----------|------------|-------------|
| PC     | FastEthernet0 | 192.168.1.2 | 255.255.255.0 |
| Router | FastEthernet0/0 | 192.168.1.1 | 255.255.255.0 |
| Router | FastEthernet0/1 | 192.168.2.1 | 255.255.255.0 |
| Switch | N/A | N/A | N/A |

3. Configure the router with the following SNMP agent settings, using the command-line interface (CLI).

- Enable SNMP service with the command `snmp-server enable`.
- Set the SNMP read-only community string to `public` with the command `snmp-server community public RO`.
- Set the SNMP read-write community string to `private` with the command `snmp-server community private RW`.
- Set the SNMP trap destination to the PC's IP address with the command `snmp-server host 192.168.1.2 public`.
- Save the configuration with the command `copy running-config startup-config`.

4. Launch SNMP Tester and enter the following settings in the main window.

- Set the IP address to `192.168.1.1`, the port to `161`, and the community string to `public`.
- Select the `Read Device Uptime` option from the drop-down menu and click the `Run Test` button.
- Observe the output in the lower window,