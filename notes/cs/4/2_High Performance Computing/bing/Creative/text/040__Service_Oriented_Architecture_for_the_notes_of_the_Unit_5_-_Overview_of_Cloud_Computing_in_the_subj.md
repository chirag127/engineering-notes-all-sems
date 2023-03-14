### Service Oriented Architecture

- Service Oriented Architecture (SOA) is an architectural style that focuses on discrete services instead of a monolithic design. 
- A service is a discrete unit of functionality that can be accessed remotely and acted upon and updated independently, such as retrieving a credit card statement online. 
- A service has four properties according to one of many definitions of SOA: 
  - It logically represents a repeatable business activity with a specified outcome.
  - It is self-contained.
  - It is a black box for its consumers, meaning the consumer does not have to be aware of the service's inner workings.
  - It may be composed of other services.
- SOA aims to allow users to combine large chunks of functionality to form applications which are built purely from existing services and combining them in an ad hoc manner. 
- A service presents a simple interface to the requester that abstracts away the underlying complexity acting as a black box. 
- Services and their corresponding consumers communicate with each other by passing data in a well-defined, shared format, or by coordinating an activity between two or more services. 
- SOA separates functions into distinct units, or services, which developers make accessible over a network in order to allow users to combine and reuse them in the production of applications. 
- Services use common interface standards and an architectural pattern so they can be rapidly incorporated into new applications. 
- This removes tasks from the application developer who previously redeveloped or duplicated existing functionality or had to know how to connect or provide interoperability with existing functions. 
- Service interfaces provide loose coupling, meaning they can be called with little or no knowledge of how the service is implemented underneath, reducing the dependencies between applications. 
- Service interfaces are frequently defined using Web Service Definition Language (WSDL) which is a standard tag structure based on xml (extensible markup language). 
- The services are exposed using standard network protocols—such as SOAP (simple object access protocol)/HTTP or Restful HTTP (JSON/HTTP)—to send requests to read or change data. 
- Service governance controls the lifecycle for development and at the appropriate stage the services are published in a registry that enables developers to quickly find them and reuse them to assemble new applications or business processes. 
- These services can be built from scratch but are often created by exposing functions from legacy systems of record as service interfaces. 
- SOA represents an important stage in the evolution of application development and integration over the last few decades. 
- An ESB, or enterprise service bus, is an architectural pattern whereby a centralized software component performs integrations between applications. 
- An ESB provides a common communication channel for services and applications, and handles tasks such as routing, transformation, security, and monitoring. 
- An ESB can help to decouple services and applications, and reduce the complexity and cost of integration. 

: Service-oriented architecture - Wikipedia
: What is SOA (Service-Oriented Architecture)? | IBM