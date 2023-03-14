## Unit 5 - Overview of Cloud Computing

Cloud computing is the delivery of computing services such as servers, storage, databases, networking, software, analytics, and intelligence over the internet. Cloud computing enables users to access scalable, on-demand, and pay-per-use IT resources without investing in physical infrastructure.

There are different types of cloud computing services, such as:

- Infrastructure as a Service (IaaS): Provides the basic building blocks of cloud computing, such as virtual machines, storage, networks, and operating systems.
- Platform as a Service (PaaS): Provides a platform for developing, testing, and deploying applications without managing the underlying infrastructure.
- Software as a Service (SaaS): Provides software applications that are hosted and managed by a cloud provider and accessed by users over the internet.
- Function as a Service (FaaS): Provides a serverless way of running code in response to events without provisioning or managing servers.

There are also different types of cloud deployment models, such as:

- Public cloud: Provides cloud services that are available to anyone over the internet, such as AWS, Azure, and GCP.
- Private cloud: Provides cloud services that are dedicated to a single organization and hosted either on-premises or by a third-party provider.
- Hybrid cloud: Provides a combination of public and private cloud services that are connected by a common network or technology.
- Multi-cloud: Provides a use of multiple public cloud services from different providers to leverage their unique capabilities and avoid vendor lock-in.

The following diagram illustrates the basic architecture of a cloud computing environment:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Public       |       |    Private      |       |    Hybrid       |
|    Cloud        |       |    Cloud        |       |    Cloud        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    IaaS         |       |    IaaS         |       |    IaaS         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    PaaS         |       |    PaaS         |       |    PaaS         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    SaaS         |       |    SaaS         |       |    SaaS         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    FaaS         |       |    FaaS         |       |    FaaS         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```