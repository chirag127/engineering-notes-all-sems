The following is a detailed ASCII diagram for types of cloud computing for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing.

### Types of Cloud Computing

There are three main types of cloud computing service models that you can select based on the level of control, flexibility, and management your business needs :

- Infrastructure as a service (IaaS) offers on-demand access to IT infrastructure services, such as compute, storage, networking, and virtualization. You can rent these resources from a cloud provider and pay only for what you use. You have full control over the configuration and management of the resources, but you are also responsible for their security and maintenance. Examples of IaaS providers are Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure.
- Platform as a service (PaaS) provides a cloud-based environment for developing, testing, and deploying applications. You can use the tools and frameworks provided by the cloud provider to create and run your applications, without worrying about the underlying infrastructure. You have less control over the resources, but you also have less responsibility for their management and security. Examples of PaaS providers are Heroku, Google App Engine, and AWS Elastic Beanstalk.
- Software as a service (SaaS) delivers ready-to-use applications over the internet, usually through a web browser. You can access these applications from any device, without installing or maintaining them. You have no control over the resources, but you also have no responsibility for their management and security. Examples of SaaS providers are Google Workspace, Salesforce, and Dropbox.

The following diagram illustrates the different levels of control and responsibility for each type of cloud computing service model:

```
+-----------------+-----------------+-----------------+-----------------+
|                 |      IaaS       |      PaaS       |      SaaS       |
+-----------------+-----------------+-----------------+-----------------+
| Control         | High            | Medium          | Low             |
+-----------------+-----------------+-----------------+-----------------+
| Responsibility  | High            | Medium          | Low             |
+-----------------+-----------------+-----------------+-----------------+
| Examples        | AWS, GCP, Azure | Heroku, GAE, EB | GWS, SF, DB     |
+-----------------+-----------------+-----------------+-----------------+
```

There are also different types of cloud computing deployment models that you can choose based on the level of privacy, security, and scalability your business needs  :

- Public clouds are cloud environments typically created from IT infrastructure not owned by the end user. You can access these clouds over the internet and share the resources with other users. Public clouds are usually cheaper, more scalable, and more reliable than private clouds, but they also have less security and privacy. Examples of public clouds are AWS, GCP, and Azure.
- Private clouds are cloud environments solely dedicated to a single end user or group, usually created from IT infrastructure owned by the end user. You can access these clouds over a private network and have exclusive use of the resources. Private clouds are usually more secure and private than public clouds, but they also have higher costs, lower scalability, and lower reliability. Examples of private clouds are VMware, OpenStack, and Red Hat OpenShift.
- Hybrid clouds are a combination of public and private clouds, connected by a common network. You can use hybrid clouds to leverage the benefits of both types of clouds, such as security, privacy, scalability, and reliability. You can also use hybrid clouds to migrate applications and data between different clouds, or to create a backup or disaster recovery plan. Examples of hybrid clouds are AWS Outposts, Azure Stack, and Google Anthos.

The following diagram illustrates the different levels of privacy, security, and scalability for each type of cloud computing deployment model:

```
+-----------------+-----------------+-----------------+-----------------+
|                 |   Public Cloud  |   Private Cloud |   Hybrid Cloud  |
+-----------------+-----------------+-----------------+-----------------+
| Privacy         | Low             | High            | Medium          |
+-----------------+-----------------+-----------------+-----------------+
| Security        | Low             | High            | Medium          |
+-----------------+-----------------+-----------------+-----------------+
| Scalability     | High            | Low             | Medium          |
+-----------------+-----------------+-----------------+-----------------+
| Examples        | AWS, GCP, Azure | VMware, OS, RH  | AWSO, AS,