 Here is the formal write-up for Experiment 9.2 - SNMP:

### Experiment 9.2 - SNMP

1. SNMP stands for Simple Network Management Protocol. It is a protocol used for managing devices on an IP network.
2. SNMP uses agents, managers and Management Information Bases (MIBs).
- Agents: Software running on the managed devices which stores the management data and responds to requests from the manager.
- Manager: Software running on the network management station which monitors and controls managed devices.
- MIBs: Database of objects that can be managed on the device.
3. Some important terms in SNMP:
- OID: Object Identifier, a numeric index which uniquely identifies a managed object.
- MIB: Management Information Base, a collection of hierarchically organized OIDs.
- Get-request: A manager-to-agent request to retrieve the value of a specific MIB object.
- Get-response: A agent-to-manager message containing the requested MIB object value.
4. SNMP uses UDP as its transport protocol and runs on port 161. It has three versions: SNMPv1, SNMPv2c and SNMPv3. SNMPv3 provides security features like authentication and encryption which are lacking in SNMPv1 and SNMPv2c.
5. This experiment illustrates how to configure SNMP on a router and monitor it using a network management station. The key steps are:
- Configure SNMP on the router.
- Install SNMP software on the NMS.
- Specify the router's IP address and community string on the NMS.
- Retrieve and view MIB data from the router using the NMS.