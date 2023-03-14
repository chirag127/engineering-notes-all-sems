The following is a detailed ASCII diagram for Open Stack for the notes of the Unit 5 - Cloud Technologies And Advancements Hadoop in the subject of Cloud Computing.

### Open Stack

```
+-----------------------------------------------------------------------------+
|                                                                             |
|  +----------------+  +----------------+  +----------------+  +------------+  |
|  |                |  |                |  |                |  |            |  |
|  |    Horizon     |  |    Keystone    |  |    Glance      |  |   Swift    |  |
|  |                |  |                |  |                |  |            |  |
|  |  Dashboard     |  |  Identity      |  |  Image         |  |  Object    |  |
|  |  Service       |  |  Service       |  |  Service       |  |  Storage   |  |
|  |                |  |                |  |                |  |  Service   |  |
|  +----------------+  +----------------+  +----------------+  +------------+  |
|                                                                             |
|  +----------------+  +----------------+  +----------------+  +------------+  |
|  |                |  |                |  |                |  |            |  |
|  |    Nova        |  |    Neutron     |  |    Cinder      |  |   Heat     |  |
|  |                |  |                |  |                |  |            |  |
|  |  Compute       |  |  Networking    |  |  Block         |  |  Orchest-  |  |
|  |  Service       |  |  Service       |  |  Storage       |  |  ration    |  |
|  |                |  |                |  |  Service       |  |  Service   |  |
|  +----------------+  +----------------+  +----------------+  +------------+  |
|                                                                             |
+-----------------------------------------------------------------------------+
|                                                                             |
|                             OpenStack Users                                 |
|                                                                             |
+-----------------------------------------------------------------------------+
```

The diagram illustrates the basic architecture of Open Stack, which consists of several components that provide different cloud services. The components are :

- Horizon: The dashboard service that provides a web-based user interface to access and manage the Open Stack resources.
- Keystone: The identity service that provides authentication and authorization for the Open Stack services and projects. It also manages the service catalog and endpoints.
- Glance: The image service that stores and manages virtual machine images. It also supports multiple image formats and storage backends.
- Swift: The object storage service that provides scalable and durable storage for unstructured data. It also supports replication and encryption of data.
- Nova: The compute service that manages the lifecycle of virtual machines and containers. It also supports multiple hypervisors and bare-metal provisioning.
- Neutron: The networking service that provides connectivity and network management for the Open Stack resources. It also supports various network plugins and drivers.
- Cinder: The block storage service that provides persistent and attachable storage volumes for virtual machines. It also supports multiple storage backends and drivers.
- Heat: The orchestration service that allows users to define and manage cloud applications using templates. It also supports multiple template formats and orchestration engines.