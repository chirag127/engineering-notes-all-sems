### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Layered architecture**: This model organizes the system into layers, where each layer provides services to the layer above it and uses the services of the layer below it. This model is commonly used in network protocols, where each layer corresponds to a different level of abstraction.

2. **Client-server architecture**: This model involves two types of components: clients and servers. Clients send requests to servers, which process the requests and return responses. This model is commonly used in web applications, where the client is a web browser and the server is a web server.

3. **Peer-to-peer architecture**: This model involves multiple components that act as both clients and servers. Each component can initiate requests and provide services to other components. This model is commonly used in file-sharing systems, where each component can share files with other components.

4. **Service-oriented architecture**: This model involves multiple components that provide services to other components. The components communicate using a standard protocol, such as SOAP or REST. This model is commonly used in enterprise systems, where different components provide different business services.

5. **Event-driven architecture**: This model involves multiple components that communicate by sending and receiving events. When a component receives an event, it processes the event and may generate new events. This model is commonly used in systems that need to respond to external events, such as user input or sensor data.

6. **Microservices architecture**: This model involves multiple small, independent components that communicate using a lightweight mechanism, such as HTTP or messaging. Each component provides a specific service and can be developed and deployed independently. This model is commonly used in cloud-native systems, where components can be easily scaled and updated.

These are some of the common architectural models used in distributed systems. Each model has its own advantages and disadvantages, and the choice of model depends on the specific requirements of the system. It is important to carefully evaluate the different models and choose the one that best fits the needs of the system.