Resource provisioning in cloud computing is the process of allocating the cloud provider's resources and services to the customer according to their needs and demands. Resource provisioning can be done manually or automatically, depending on the level of control and flexibility required by the customer. Resource provisioning can also be done dynamically, meaning that the resources can be scaled up or down according to the changing workload and demand.

The following diagram illustrates the basic architecture of resource provisioning in cloud computing using ASCII characters:

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|    Customer      |     |    Cloud         |     |    Cloud         |
|                  |     |    Provider      |     |    Provider      |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|    Cloud         |     |    Cloud         |     |    Cloud         |
|    Broker        |     |    Orchestrator  |     |    Manager       |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|    Cloud         |     |    Cloud         |     |    Cloud         |
|    Monitor       |     |    Provisioner   |     |    Meter         |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|    Cloud         |     |    Cloud         |     |    Cloud         |
|    Resources     |     |    Resources     |     |    Resources     |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
```

The diagram shows the following components and their roles:

- Customer: The end-user who requests and consumes the cloud resources and services.
- Cloud Broker: An intermediary who acts as a single point of contact between the customer and multiple cloud providers, and helps the customer to select the best provider and service level agreement (SLA) for their needs.
- Cloud Orchestrator: A software tool that automates the coordination and management of multiple cloud resources and services across different providers, and ensures that they work together as a single system.
- Cloud Manager: A software tool that oversees the overall performance, availability, security, and compliance of the cloud resources and services, and provides the customer with visibility and control over them.
- Cloud Monitor: A software tool that collects and analyzes the data about the cloud resources and services, such as their utilization, availability, quality, and cost, and provides feedback and alerts to the customer and the cloud provider.
- Cloud Provisioner: A software tool that allocates and configures the cloud resources and services according to the customer's request and the SLA, and releases them when they are no longer needed.
- Cloud Meter: A software tool that measures and records the usage and consumption of the cloud resources and services, and generates the billing and invoicing information for the customer and the cloud provider.
- Cloud Resources: The physical or virtual infrastructure and platforms that provide the computing, storage, network, and application capabilities for the cloud services.
- Cloud Services: The software applications and functions that run on the cloud resources and provide the customer with the desired functionality and value.