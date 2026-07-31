# Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Layered architecture**: This model organizes the system into layers, where each layer provides services to the layer above it and uses the services of the layer below it. This model is commonly used in network protocols, where each layer corresponds to a different level of abstraction.

- **Client-server architecture**: This model divides the system into two main components: clients and servers. Clients request services from servers, which process the requests and return the results. This model is commonly used in web applications, where the client is a web browser and the server is a web server.

- **Peer-to-peer architecture**: This model organizes the system as a network of equal peers, where each peer can act as both a client and a server. This model is commonly used in file-sharing systems, where each peer can share files with other peers.

- **Service-oriented architecture**: This model organizes the system as a collection of loosely-coupled services, where each service provides a specific functionality. This model is commonly used in enterprise systems, where different services can be developed and deployed independently.

- **Event-driven architecture**: This model organizes the system as a collection of components that communicate through events. When an event occurs, the components that are interested in that event are notified and can react accordingly. This model is commonly used in graphical user interfaces, where user actions generate events that are handled by the appropriate components.

- **Microservices architecture**: This model organizes the system as a collection of small, independent services that communicate through well-defined interfaces. This model is commonly used in cloud-based systems, where each service can be developed, deployed, and scaled independently.

- **N-tier architecture**: This model organizes the system into multiple tiers, where each tier provides a specific functionality. This model is commonly used in enterprise systems, where different tiers can correspond to different layers of abstraction, such as the presentation layer, the business logic layer, and the data access layer.

- **Model-View-Controller architecture**: This model organizes the system into three main components: the model, which represents the data and the business logic; the view, which displays the data to the user; and the controller, which handles user input and updates the model and the view accordingly. This model is commonly used in graphical user interfaces, where it helps to separate concerns and improve maintainability.

- **Pipe-and-filter architecture**: This model organizes the system as a sequence of processing stages, where each stage reads data from the previous stage, processes it, and writes the results to the next stage. This model is commonly used in data processing systems, where it helps to modularize the processing logic and improve scalability.

- **Blackboard architecture**: This model organizes the system as a collection of independent components that communicate through a shared blackboard. The components can read from and write to the blackboard, and can react to changes in the blackboard. This model is commonly used in artificial intelligence systems, where it helps to coordinate the activities of multiple agents.

These are some of the common architectural models used in distributed systems. Each model has its own strengths and weaknesses, and the choice of model depends on the specific requirements of the system being designed. It is important to carefully evaluate the trade-offs between different models before making a decision.