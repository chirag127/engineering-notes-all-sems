The following is a detailed ASCII diagram for REST and Systems of Systems for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing.

REST is a style of architecture based on a set of principles that describe how networked resources are defined and addressed. RESTful systems are stateless and separate the concerns of client and server. They use a uniform interface to exchange representations of resources using HTTP methods such as GET, POST, PUT, and DELETE  .

A system of systems is a collection of task-oriented or dedicated systems that pool their resources and capabilities together to create a new, more complex system which offers more functionality and performance than simply the sum of the constituent systems. A system of systems can be composed of heterogeneous, autonomous, and distributed systems that interact through a shared environment.

A possible diagram for REST and Systems of Systems is shown below:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Client A      |       |   Client B      |       |   Client C      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   System A      |       |   System B      |       |   System C      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Resource A    |       |   Resource B    |       |   Resource C    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows how multiple clients can access multiple systems of systems using REST. Each system of systems consists of multiple systems that provide different resources. The clients can use HTTP methods to request, create, update, or delete the representations of the resources from the systems. The systems can communicate with each other through a shared environment to coordinate their actions and provide a consistent view of the resources. The systems can also be heterogeneous, autonomous, and distributed, meaning that they can have different architectures, operate independently, and be located in different locations. The system of systems can provide more functionality and performance than any single system by leveraging the capabilities and resources of the constituent systems.