 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Pattern-based Architecture for Service-oriented Applications

- Service-oriented applications are built by integrating multiple services. Hence, an architectural pattern is required to guide the design and development of such applications.
- Some of the key architectural patterns for service-oriented applications are:
- Layered pattern: Services are organized into layers such that services in one layer can only access services in the immediately adjacent lower layer. This pattern emphasizes loose coupling and separation of concerns.
- Pipes and filters pattern: Services are configured in a pipeline where the output of one service is sent as input to the next service. This pattern is suitable for processing data streams and workflows.
- Event-driven pattern: Services communicate by generating and responding to events. This pattern is useful for reacting to state changes and handling asynchronous communications.
- Microkernel pattern: A microkernel mediates all communications between services. Services do not directly interact with each other. This pattern enhances maintainability by centralizing all interactions through the microkernel.
- Space-based pattern: Services are allocated to different execution contexts or spaces. This pattern is useful for applications with diverse non-functional requirements that necessitate segregation of services.

The above architectural patterns can be used individually or combined to build service-oriented applications based on the requirements and context. A suitable pattern or combination of patterns leads to loosely coupled, maintainable, and scalable service-oriented applications.