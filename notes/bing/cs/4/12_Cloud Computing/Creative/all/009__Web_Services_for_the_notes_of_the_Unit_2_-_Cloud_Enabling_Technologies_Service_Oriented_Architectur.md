### Web Services for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- Web services are software modules that can be found and invoked over the network using standard web protocols such as HTTP or HTTPS .
- Web services allow data to be exchanged between different applications or systems, regardless of their programming languages, platforms, or architectures .
- Web services in cloud computing provide functionality to the clients that call them, such as data storage, processing, analytics, or security.
- Web services can be classified into two types: SOAP and REST.
  - SOAP (Simple Object Access Protocol) is a protocol that uses XML to format the messages and relies on other protocols such as HTTP, SMTP, or FTP for transport.
  - REST (Representational State Transfer) is an architectural style that uses HTTP methods (GET, POST, PUT, DELETE) to access and manipulate resources on a server.
- Web services can be implemented using various technologies, such as Java, .NET, PHP, Python, Ruby, or Node.js.
- Web services can be composed into larger applications using a service-oriented architecture (SOA), which is a design paradigm that promotes loose coupling, reusability, and interoperability of services.
- Web services have several advantages, such as:
  - They enable distributed computing over the internet, which reduces the cost and complexity of developing and maintaining applications .
  - They facilitate integration and communication between heterogeneous systems, which improves the scalability and reliability of applications .
  - They support dynamic discovery and invocation of services, which enhances the flexibility and adaptability of applications .
- Web services also have some disadvantages, such as:
  - They may introduce network latency and bandwidth issues, which affect the performance and responsiveness of applications.
  - They may require additional security measures, such as encryption, authentication, and authorization, to protect the data and services from unauthorized access or modification.
  - They may increase the complexity and overhead of testing and debugging, as they involve multiple components and interactions.

- A possible mnemonic to remember the types of web services is: **SOAP is a protocol, REST is a style**.
- A possible learning trick to understand the difference between SOAP and REST is: **SOAP is like sending a letter in an envelope, REST is like sending a postcard**.
- A possible ascii diagram to illustrate the structure of a SOAP message is:

```
+---------------------+
|     Envelope        |
+---------------------+
|     Header          |
+---------------------+
|     Body            |
+---------------------+
|     Fault           |
+---------------------+
```

- A possible ascii diagram to illustrate the structure of a REST request is:

```
+---------------------+
|     HTTP Method     |
+---------------------+
|     Resource URI    |
+---------------------+
|     Headers         |
+---------------------+
|     Body            |
+---------------------+
```