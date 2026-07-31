### Experiment 9.2 - SNMP

SNMP stands for Simple Network Management Protocol. It is a standard protocol for managing and monitoring network devices, such as routers, switches, servers, printers, etc. SNMP allows network administrators to collect information about the status, performance, and configuration of network devices, and to control them remotely.

The main components of SNMP are:

- **Managed devices**: These are the network devices that support SNMP and can be monitored and controlled by SNMP agents. Managed devices have a unique identifier called an SNMP Object Identifier (OID), which is a hierarchical string of numbers that represents the device's type, vendor, model, etc. For example, the OID for a Cisco router is 1.3.6.1.4.1.9.
- **SNMP agents**: These are software processes that run on managed devices and communicate with SNMP managers. SNMP agents collect information about the device's status, performance, and configuration, and store them in a database called a Management Information Base (MIB). SNMP agents also receive commands from SNMP managers and execute them on the device. SNMP agents use a protocol called SNMP to send and receive messages with SNMP managers.
- **SNMP managers**: These are software applications that run on network management systems and communicate with SNMP agents. SNMP managers query SNMP agents for information about the managed devices, and receive responses from them. SNMP managers can also send commands to SNMP agents to control the managed devices. SNMP managers use a protocol called SNMP to send and receive messages with SNMP agents.

The main operations of SNMP are:

- **Get**: This operation allows an SNMP manager to request information from an SNMP agent about a specific variable or a group of variables in the MIB. The SNMP agent responds with the requested information or an error message.
- **GetNext**: This operation allows an SNMP manager to request information from an SNMP agent about the next variable or group of variables in the MIB, following a specified variable. The SNMP agent responds with the requested information or an error message.
- **Set**: This operation allows an SNMP manager to modify the value of a specific variable or a group of variables in the MIB. The SNMP agent responds with a confirmation or an error message.
- **Trap**: This operation allows an SNMP agent to send an unsolicited notification to an SNMP manager about an event or a condition that occurred on the managed device. The SNMP manager can acknowledge the trap or ignore it.

The main versions of SNMP are:

- **SNMPv1**: This is the original version of SNMP, which supports basic operations and provides no security features. SNMPv1 messages are sent in clear text, which makes them vulnerable to interception, modification, and spoofing.
- **SNMPv2c**: This is an enhanced version of SNMP, which supports additional operations and provides better error handling. SNMPv2c messages are also sent in clear text, which makes them vulnerable to the same security threats as SNMPv1.
- **SNMPv3**: This is the latest version of SNMP, which supports the same operations as SNMPv2c and provides security features, such as authentication, encryption, and access control. SNMPv3 messages are protected from unauthorized access, modification, and spoofing.