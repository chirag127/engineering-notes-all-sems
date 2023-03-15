Network management in application layer is the process of monitoring and controlling network devices and applications using protocols that operate at the application layer of the OSI model. One of the most common protocols for network management in application layer is the Simple Network Management Protocol (SNMP), which uses UDP port number 161/162. SNMP allows network administrators to collect information from network devices, such as routers, switches, servers, printers, etc., and to configure them remotely. SNMP consists of three components: SNMP agents, SNMP managers, and SNMP management information base (MIB).

A possible ASCII diagram for network management in application layer using SNMP is:

### Network management in application layer

```
+----------------+             +----------------+             +----------------+
|                |             |                |             |                |
|  SNMP Manager  |             |  SNMP Agent    |             |  SNMP Agent    |
|                |             |                |             |                |
+----------------+             +----------------+             +----------------+
|                |             |                |             |                |
|  SNMP MIB      |             |  SNMP MIB      |             |  SNMP MIB      |
|                |             |                |             |                |
+----------------+             +----------------+             +----------------+
|                |             |                |             |                |
|  Application   |             |  Application   |             |  Application   |
|  Layer         |             |  Layer         |             |  Layer         |
|                |             |                |             |                |
+----------------+             +----------------+             +----------------+
|                |             |                |             |                |
|  Transport     |             |  Transport     |             |  Transport     |
|  Layer         |             |  Layer         |             |  Layer         |
|                |             |                |             |                |
+----------------+             +----------------+             +----------------+
|                |             |                |             |                |
|  Network       |             |  Network       |             |  Network       |
|  Layer         |             |  Layer         |             |  Layer         |
|                |             |                |             |                |
+----------------+             +----------------+             +----------------+
|                |             |                |             |                |
|  Data Link     |             |  Data Link     |             |  Data Link     |
|  Layer         |             |  Layer         |             |  Layer         |
|                |             |                |             |                |
+----------------+             +----------------+             +----------------+
|                |             |                |             |                |
|  Physical      |             |  Physical      |             |  Physical      |
|  Layer         |             |  Layer         |             |  Layer         |
|                |             |                |             |                |
+----------------+             +----------------+             +----------------+
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       |                            |                            |
       +--------------------------------------------------------+
                            Network Media
```