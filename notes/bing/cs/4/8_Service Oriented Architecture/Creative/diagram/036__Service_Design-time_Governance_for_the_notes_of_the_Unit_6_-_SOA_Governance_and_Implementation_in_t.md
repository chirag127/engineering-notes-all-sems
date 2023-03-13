Service Design-time Governance is the process of defining and enforcing policies and standards for the design and implementation of services in a Service Oriented Architecture (SOA). It involves the use of tools and methodologies to ensure that services are consistent, reusable, secure, and aligned with the business goals and requirements.

The following diagram illustrates the basic architecture of a Service Design-time Governance system using Oracle's SOA Governance Suite components:

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Service Design  |     |  Service Testing |     |  Service Release |
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
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       V                        V                        V
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Service         |     |  Service         |     |  Service         |
|  Repository      |     |  Registry        |     |  Metadata Store  |
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
       V                        V                        V
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Service         |     |  Service         |     |  Service         |
|  Policy          |     |  Security        |     |  Reporting       |
|  Management      |     |  Management      |     |                  |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
```

The Service Design phase involves the use of a Service Repository to store and manage the service artifacts, such as service contracts, schemas, policies, and documentation. The Service Repository also provides tools for service modeling, analysis, and governance.

The Service Testing phase involves the use of a Service Registry to publish and discover the services and their metadata. The Service Registry also provides tools for service validation, simulation, and testing.

The Service Release phase involves the use of a Service Metadata Store to store and manage the runtime configuration and metadata of the services. The Service Metadata Store also provides tools for service deployment, monitoring, and auditing.

The Service Policy Management component provides tools for defining and enforcing the policies and standards for the services, such as service level agreements, quality of service, and compliance.

The Service Security Management component provides tools for securing the services and their interactions, such as authentication, authorization, encryption, and digital signatures.

The Service Reporting component provides tools for generating and analyzing reports on the performance, usage, and quality of the services.