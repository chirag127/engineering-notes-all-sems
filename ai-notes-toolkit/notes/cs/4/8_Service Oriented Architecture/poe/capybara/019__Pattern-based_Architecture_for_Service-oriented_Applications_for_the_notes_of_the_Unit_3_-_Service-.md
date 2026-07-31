### Pattern-based Architecture for Service-oriented Applications

Service-oriented architecture (SOA) is a software architecture style that emphasizes the use of services to support the requirements of software systems. A service is a self-contained, loosely coupled module that performs a specific business function and can be invoked by other software components.

To design and implement SOA-based applications, software architects use a pattern-based approach. Patterns are reusable solutions to common design problems that have been proven to be effective in practice. Here are some of the patterns commonly used in the design of service-oriented applications:

1. Service-Oriented Integration:
This pattern focuses on integrating existing systems and applications into a service-oriented architecture by exposing their functionality as services. It involves the use of middleware technologies such as Enterprise Service Bus (ESB) and service adapters to enable communication between services.

2. Service Façade:
This pattern provides a simplified interface to a complex service by exposing only a subset of its functionality through a façade. It enhances the usability of the service by making it easier to understand and use, while also promoting loose coupling between the service and its clients.

3. Service Registry:
This pattern provides a central repository for service descriptions that can be used to locate and invoke services. It promotes reuse and interoperability by enabling services to be discovered and used by other applications.

4. Service Choreography:
This pattern focuses on the coordination of services to achieve a specific business process. It involves the use of messaging and orchestration techniques to ensure that services are invoked in the correct order and with the correct data.

5. Service Composition:
This pattern involves combining multiple services to achieve a specific business function. It enables the creation of new services by combining existing ones, thereby promoting reuse and reducing development time and costs.

In summary, pattern-based architecture is a key approach to designing and implementing service-oriented applications. By using proven patterns, software architects can create robust, scalable, and maintainable systems that meet the requirements of modern business environments.