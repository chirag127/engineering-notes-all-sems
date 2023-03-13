## Unit 3 - Cloud Architecture, Services And Storage

The following is a possible diagram for the cloud architecture, services and storage of an organization. It is based on the information from the web search results    . It is not intended to be a definitive or comprehensive representation, but rather an illustrative example.

The diagram shows the following components and relationships:

- The organization has a hybrid cloud model, which means it uses both public cloud services and private cloud resources on-premises.
- The public cloud services are provided by Microsoft Azure, which offers various products and resources for compute, networking, storage, analytics, security, and management.
- The private cloud resources are hosted on the organization's own data center, which has servers, storage devices, network devices, and firewalls.
- The organization uses Azure Active Directory (Azure AD) as the identity and access management service for both the public and private cloud resources. Azure AD synchronizes with the on-premises Active Directory (AD) to provide a single sign-on experience for the users and applications.
- The organization uses Azure Blob Storage and Azure Data Lake Storage Gen2 as the object storage services for storing and processing large amounts of unstructured data, such as text, images, videos, and logs. These services support big data analytics and can scale to petabytes of data.
- The organization uses Azure Files as the file storage service for storing and sharing files across the cloud and on-premises. Azure Files supports the Server Message Block (SMB) protocol and can be accessed by Windows, Linux, and macOS clients.
- The organization uses Azure SQL Database and Azure Cosmos DB as the relational and non-relational database services for storing and querying structured and semi-structured data, such as tables, documents, graphs, and key-values. These services offer high availability, scalability, and performance.
- The organization uses Azure Virtual Machines (VMs) and Azure Kubernetes Service (AKS) as the compute services for running applications and workloads on the cloud. Azure VMs provide virtualized servers that can run Windows or Linux operating systems and support various sizes and configurations. Azure AKS provides a managed platform for orchestrating and scaling containerized applications using Kubernetes.
- The organization uses Azure Virtual Network (VNet) and Azure ExpressRoute as the networking services for connecting and securing the cloud and on-premises resources. Azure VNet provides a private and isolated network space for the cloud resources, and supports subnets, network security groups, firewalls, load balancers, and VPN gateways. Azure ExpressRoute provides a dedicated and private connection between the organization's data center and Azure, bypassing the public internet.
- The organization uses Azure Synapse Analytics and Azure Databricks as the analytics services for performing data integration, transformation, and analysis on the cloud. Azure Synapse Analytics provides a unified platform for data warehousing, data lake, and big data analytics, and supports SQL, Spark, and Power BI. Azure Databricks provides a collaborative workspace for data science and machine learning, and supports Spark, Python, R, and Scala.
- The organization uses Azure Security Center and Azure Sentinel as the security services for protecting and monitoring the cloud and on-premises resources. Azure Security Center provides a centralized dashboard for managing the security posture, policies, and alerts of the cloud resources, and supports threat detection and prevention. Azure Sentinel provides a cloud-native solution for security information and event management (SIEM) and security orchestration, automation, and response (SOAR), and supports data collection, analysis, and response.
- The organization uses Azure Monitor and Azure Automation as the management services for operating and optimizing the cloud and on-premises resources. Azure Monitor provides a comprehensive solution for collecting, analyzing, and visualizing the metrics, logs, and alerts of the cloud resources, and supports application insights and service health. Azure Automation provides a platform for automating the tasks and workflows of the cloud resources, and supports runbooks, PowerShell, and Python.

The diagram is drawn using ASCII characters and symbols, and follows the conventions of the Gliffy cloud architecture diagram tool. The diagram is not to scale and does not show all the details and connections of the components.

```
+-----------------------------------------------------------------------------------------------------------------+
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
|