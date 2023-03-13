Network management in application layer is the process of monitoring, configuring, and controlling the network resources and services using various protocols and tools. The application layer is the topmost layer of the OSI model that provides the interface between the user applications and the network. Some of the protocols used for network management in application layer are:

- Simple Network Management Protocol (SNMP): A protocol that uses UDP port number 161/162 to collect and manipulate information about network devices and their status. SNMP consists of a manager, an agent, and a management information base (MIB). The manager sends requests to the agent, which responds with the data from the MIB. The MIB is a database that stores the information about the network device and its configuration.
- File Transfer Protocol (FTP): A protocol that uses TCP port number 21 to transfer files between hosts. FTP allows the user to log in to a remote host, browse the directory structure, and upload or download files. FTP can also be used to transfer configuration files or firmware updates to network devices.
- Telnet: A protocol that uses TCP port number 23 to provide remote access to a network device or a host. Telnet allows the user to log in to a network device and execute commands on its command-line interface. Telnet can also be used to configure or troubleshoot network devices.
- Trivial File Transfer Protocol (TFTP): A protocol that uses UDP port number 69 to transfer files between hosts. TFTP is a simplified version of FTP that does not require authentication or directory browsing. TFTP is mainly used to transfer configuration files or firmware updates to network devices.

The following diagram illustrates the basic architecture of a network management system in application layer using SNMP as an example:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Application   |       |   Application   |       |   Application   |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Transport     |       |   Transport     |       |   Transport     |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Network       |       |   Network       |       |   Network       |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Data Link     |       |   Data Link     |       |   Data Link     |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Physical      |       |   Physical      |       |   Physical      |
|     Layer       |       |     Layer       |       |     Layer       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       |                     |                         |
       +---------------------+-------------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |