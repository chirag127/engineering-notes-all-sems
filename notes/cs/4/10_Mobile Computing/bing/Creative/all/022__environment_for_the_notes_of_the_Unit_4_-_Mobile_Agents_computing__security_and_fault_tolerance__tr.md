### Environment for Mobile Agents Computing

Mobile agents are autonomous software entities that can move from one host to another in a network, carrying their code and data, and resume their execution in the new environment . Mobile agents can be used for various applications in mobile computing, such as information retrieval, service discovery, network management, data processing, and distributed computing .

The environment for mobile agents computing consists of the following components :

- **Agent host**: A computer system that provides the execution environment for mobile agents. It can run one or more agent platforms that support the creation, migration, and communication of mobile agents.
- **Agent platform**: A software system that implements the mobile agent model and provides the services and resources for mobile agents. It can support different agent languages, protocols, and security mechanisms. It can also interact with other agent platforms to enable agent mobility and interoperability.
- **Agent**: A software entity that encapsulates its code, data, and state, and can move from one agent platform to another. It can act autonomously, communicate with other agents, and adapt to the changing environment. It can also have a graphical user interface to interact with the user or the host system.
- **Agent server**: A software entity that acts as a proxy for a mobile agent on a remote host. It can receive, store, and forward the agent's code, data, and state, and can also execute the agent on behalf of the original host.
- **Agent manager**: A software entity that manages the life cycle of mobile agents on an agent platform. It can create, suspend, resume, terminate, and migrate mobile agents. It can also monitor and control the resource consumption and behavior of mobile agents.
- **Agent transport service**: A software service that enables the mobility of mobile agents across different agent platforms. It can handle the serialization, compression, encryption, and transmission of mobile agents. It can also support different transport protocols, such as TCP/IP, HTTP, or RMI.
- **Agent communication service**: A software service that enables the communication of mobile agents with other agents or with the agent platform. It can support different communication paradigms, such as message passing, remote method invocation, or publish/subscribe. It can also support different communication protocols, such as KQML, FIPA-ACL, or SOAP.
- **Agent security service**: A software service that provides the security mechanisms for mobile agents and their hosts. It can support different security aspects, such as authentication, authorization, confidentiality, integrity, non-repudiation, and audit. It can also support different security techniques, such as digital signatures, certificates, encryption, firewalls, or sandboxing.

The following diagram illustrates the environment for mobile agents computing:

```
+-----------------+       +-----------------+       +-----------------+
|   Agent Host    |       |   Agent Host    |       |   Agent Host    |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | Agent       | |       | | Agent       | |       | | Agent       | |
| | Platform    | |       | | Platform    | |       | | Platform    | |
| | +---------+ | |       | | +---------+ | |       | | +---------+ | |
| | | Agent   | | |       | | | Agent   | | |       | | | Agent   | | |
| | | Manager | | |       | | | Manager | | |       | | | Manager | | |
| | +---------+ | |       | | +---------+ | |       | | +---------+ | |
| | +---------+ | |       | | +---------+ | |       | | +---------+ | |
| | | Agent   | | |       | | | Agent   | | |       | | | Agent   | | |
| | | Server  | | |       | | | Server  | | |       | | | Server  | | |
| | +---------+ | |       | | +---------+ | |       | | +---------+ | |
| | +---------+ | |       | | +---------+ | |       | | +---------+ | |
| | | Agent   | | |       | | | Agent   | | |       | | | Agent   | | |
| | | Transport| | |       | | | Transport| | |       | | | Transport| | |
| | | Service  | | |       | | | Service  | |