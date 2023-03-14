The following diagram illustrates the basic architecture of a virtual machine security system in cloud:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Virtual Switch  |    |  Virtual Switch  |    |  Virtual Switch  |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Virtual NIC     |    |  Virtual NIC     |    |  Virtual NIC     |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Virtual Disk    |    |  Virtual Disk    |    |  Virtual Disk    |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Virtual Machine |    |  Virtual Machine |    |  Virtual Machine |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Hypervisor      |    |  Hypervisor      |    |  Hypervisor      |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Host OS         |    |  Host OS         |    |  Host OS         |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Physical Server |    |  Physical Server |    |  Physical Server |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
```

The diagram shows how virtual machines are isolated from each other by using virtual switches, virtual NICs, and virtual disks. The virtual switches provide network security by preventing inter-switch link attacks and allowing network connectivity between the virtual and physical networks. The virtual NICs provide network interface security by encrypting the traffic between the virtual machines and the virtual switches. The virtual disks provide data security by encrypting the data at rest and in transit using encryption at host, customer-managed keys, and double encryption. The hypervisor provides the virtualization layer that enables multiple virtual machines to run on a single physical server. The host OS provides the operating system security by applying patches, updates, and antivirus software. The physical server provides the hardware security by using Trusted Platform Module (TPM) to store and protect keys, certificates, and secrets.

Some of the sources used to create this diagram are:

- Security architecture design - Azure Architecture Center
- Apply Zero Trust principles to virtual machines in Azure
- Virtual Machine Security in Cloud - GeeksforGeeks
- 10 Ways Virtualization Can Improve Security - Techopedia.com
- Azure Well-Architected Framework review - Virtual Machines