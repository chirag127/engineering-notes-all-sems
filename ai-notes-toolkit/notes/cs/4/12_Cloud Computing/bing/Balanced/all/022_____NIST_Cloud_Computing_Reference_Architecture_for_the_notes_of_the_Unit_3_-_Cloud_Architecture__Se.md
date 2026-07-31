# NIST Cloud Computing Reference Architecture

The NIST Cloud Computing Reference Architecture (NIST SP 500-292) is a document that provides a framework for describing the essential characteristics, service models, and deployment models of cloud computing. It also defines the roles and responsibilities of various actors involved in the delivery and consumption of cloud services. The NIST Cloud Computing Reference Architecture aims to facilitate communication, analysis, and comparison of cloud offerings and solutions.

The NIST Cloud Computing Reference Architecture consists of five major components:

- Cloud Consumer: The entity that uses cloud services to support its business or organizational needs. The cloud consumer may be a person, an organization, or a software system.
- Cloud Provider: The entity that provides cloud services to cloud consumers. The cloud provider may own and manage the physical infrastructure, or use the services of another cloud provider (e.g., cloud broker) to deliver cloud services.
- Cloud Auditor: The entity that conducts independent assessment of the cloud services, information system operations, performance, and security of the cloud implementation. The cloud auditor may be a third party, a government agency, or an internal department of the cloud provider or the cloud consumer.
- Cloud Broker: The entity that manages the use, performance, and delivery of cloud services, and negotiates relationships between cloud providers and cloud consumers. The cloud broker may act as an intermediary, an aggregator, or an arbitrator of cloud services.
- Cloud Carrier: The entity that provides connectivity and transport of cloud services between cloud providers and cloud consumers. The cloud carrier may be a telecommunication company, an internet service provider, or a dedicated network provider.

The NIST Cloud Computing Reference Architecture also defines a set of cloud service categories, based on the service models of cloud computing:

- Software as a Service (SaaS): The capability provided to the cloud consumer to use the provider's applications running on a cloud infrastructure. The cloud consumer does not manage or control the underlying cloud infrastructure, but has limited user-specific application configuration settings.
- Platform as a Service (PaaS): The capability provided to the cloud consumer to deploy onto the cloud infrastructure consumer-created or acquired applications created using programming languages, libraries, services, and tools supported by the provider. The cloud consumer does not manage or control the underlying cloud infrastructure, but has control over the deployed applications and possibly configuration settings for the application-hosting environment.
- Infrastructure as a Service (IaaS): The capability provided to the cloud consumer to provision processing, storage, networks, and other fundamental computing resources, and to deploy and run arbitrary software, which can include operating systems and applications. The cloud consumer does not manage or control the underlying cloud infrastructure, but has control over operating systems, storage, and deployed applications, and possibly limited control of select networking components (e.g., host firewalls).

The NIST Cloud Computing Reference Architecture also defines a set of cloud deployment models, based on the location and ownership of the cloud infrastructure:

- Private Cloud: The cloud infrastructure is provisioned for exclusive use by a single organization comprising multiple consumers (e.g., business units). It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist on or off premises.
- Community Cloud: The cloud infrastructure is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations). It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them, and it may exist on or off premises.
- Public Cloud: The cloud infrastructure is provisioned for open use by the general public. It may be owned, managed, and operated by a business, academic, or government organization, or some combination of them. It exists on the premises of the cloud provider.
- Hybrid Cloud: The cloud infrastructure is a composition of two or more distinct cloud infrastructures (private, community, or public) that remain unique entities, but are bound together by standardized or proprietary technology that enables data and application portability (e.g., cloud bursting for load balancing between clouds).

The NIST Cloud Computing Reference Architecture provides a graphical representation of the components and relationships, as shown below:

![NIST Cloud Computing Reference Architecture](https://www.nist.gov/sites/default/files/images/2017/05/09/nist_cloud_computing_reference_architecture.jpg)

Source: NIST SP 500-292, Figure 3. NIST Cloud Computing Reference Architecture

The NIST Cloud Computing Reference Architecture is intended to be a vendor-neutral, technology-neutral, and standard-based reference model that can be used by