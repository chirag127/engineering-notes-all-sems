### Inter Cloud Resource Management

- Inter Cloud Resource Management is the process of managing the resources of multiple clouds that are interconnected and cooperate to provide services to clients or other clouds.
- Inter Cloud Resource Management aims to address the limitations of single clouds, such as resource scarcity, vendor lock-in, geographic constraints, and service level agreements.
- Inter Cloud Resource Management can be classified into two types: Federation Clouds and Multi-Clouds.
  - Federation Clouds are inter-clouds where several cloud service providers voluntarily link their cloud infrastructures together to exchange resources. Cloud service providers in the federation trade resources in an open manner.
  - Multi-Clouds are inter-clouds where a client or service makes use of multiple independent clouds. A multi-cloud environment lacks voluntarily shared infrastructure across cloud service providers. It is the client’s or their agents’ responsibility to manage resource supply and scheduling.
- Inter Cloud Resource Management can use different topologies to organize the inter-cloud architecture, such as peer-to-peer, hierarchical, or hybrid.
  - Peer-to-peer inter-cloud federation is where clouds communicate and engage in direct negotiation without the use of intermediaries. The peer-to-peer federation inter-cloud projects are RESERVOIR, mOSAIC, and OPTIMIS.
  - Hierarchical inter-cloud federation is where clouds rely on centralized entities, such as brokers or directories, to facilitate resource discovery and allocation. The hierarchical inter-cloud federation projects are CONTRAIL, STRATOS, and CloudBroker.
  - Hybrid inter-cloud federation is where clouds use a combination of peer-to-peer and hierarchical approaches to achieve resource management. The hybrid inter-cloud federation projects are InterCloud and Cloud4SOA.
- Inter Cloud Resource Management can benefit from the following techniques and tools to organize and manage the resources effectively:
  - Management groups, subscriptions, resource groups, and resources are the four levels of management in Azure that help to define a management hierarchy and scope the management settings, such as policies and role-based access control.
  - Naming standards are the conventions that help to identify and classify the resources in a consistent and meaningful way. Naming standards can include prefixes, suffixes, separators, abbreviations, and acronyms.
  - Resource tags are the key-value pairs that help to categorize and group the resources based on common attributes, such as environment, application, owner, or cost center. Resource tags can also help to automate tasks, such as applying policies, generating reports, or deploying resources.