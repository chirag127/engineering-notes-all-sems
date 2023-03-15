 Here is the content in markdown format:

### REST and Systems of Systems for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

REST (Representational State Transfer) is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other. REST-compliant systems, often called RESTful systems, are characterized by how they are stateless and separate the concerns of client and server.

Some key concepts of REST are:

- Statelessness: The server does not store any client context information. Every request from the client contains all the information necessary to service the request and the server responds to the request in context of that specific request.
- Client-Server: There is a clear separation between the client and the server. The client initiates requests and the server responds to them.
- Cacheability: REST encourages caching responses to improve network efficiency.
- Layered System: A client cannot ordinarily tell whether it is connected directly to the end server, or to an intermediary along the way.
- Code on Demand (Optional): REST allows clients to extend the functionality of a server by downloading and executing a program.

Advantages of REST:

- Simplicity: REST is simple to understand and implement as it follows simple concepts and standards.
- Flexibility: REST is flexible to various data formats like JSON, XML, etc. and supports different platforms and languages.
- Scalability: REST can handle a huge amount of data and traffic as it is stateless and the server does not need to maintain the state of the client.
- Performance: Due to its stateless nature and caching capabilities, REST provides good performance.

Disadvantages of REST:

- Overhead: There can be extra overhead as every request from the client needs to carry all the information increasing the bandwidth usage.
- Caching: If caching is not implemented properly, it can lead to stale data.
- Security: As REST uses HTTP, the data is visible to all intermediaries posing security issues. OAuth and other authentication mechanisms need to be implemented to handle security.

Applications of REST:

- Web APIs: Most of the web APIs today are REST-based as it is easy to use and implement.
- Cloud-based services: Many cloud service providers use REST to expose their services and functionalities to the users.
- Microservices: Microservices architecture uses REST over HTTP for inter-service communication as it is lightweight and flexible.