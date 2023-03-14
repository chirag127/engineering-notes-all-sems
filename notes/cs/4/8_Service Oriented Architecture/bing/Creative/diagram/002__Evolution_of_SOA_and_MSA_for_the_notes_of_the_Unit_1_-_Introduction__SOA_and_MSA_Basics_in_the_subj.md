The following diagram illustrates the basic architecture of a monolithic application, which is a single, self-contained unit that contains all the components of the application:

+---------------------+
|                     |
|   Monolithic App    |
|                     |
+---------------------+
|                     |
| UI | Business Logic |
|                     |
+---------------------+
|                     |
|      Database       |
|                     |
+---------------------+

The following diagram illustrates the basic architecture of a service-oriented architecture (SOA), which is an enterprise-wide approach to software development that takes advantage of reusable software components, or services, that are loosely coupled and communicate through an enterprise service bus (ESB):

+---------------------+     +---------------------+
|                     |     |                     |
|     Service 1       |     |     Service 2       |
|                     |     |                     |
+---------------------+     +---------------------+
|                     |     |                     |
| UI | Business Logic |     | UI | Business Logic |
|                     |     |                     |
+---------------------+     +---------------------+
|                     |     |                     |
|      Database       |     |      Database       |
|                     |     |                     |
+---------------------+     +---------------------+
         |                         |
         |                         |
         +-------------------------+
                   |
                   |
                   v
            +-----------------+
            |                 |
            | Enterprise      |
            | Service Bus     |
            | (ESB)           |
            |                 |
            +-----------------+

The following diagram illustrates the basic architecture of a microservices architecture (MSA), which is an architectural style that breaks large, complex applications into small, flexible components that are independently deployable, scalable, and testable:

+---------------------+     +---------------------+
|                     |     |                     |
|   Microservice 1    |     |   Microservice 2    |
|                     |     |                     |
+---------------------+     +---------------------+
|                     |     |                     |
| UI | Business Logic |     | UI | Business Logic |
|                     |     |                     |
+---------------------+     +---------------------+
|                     |     |                     |
|      Database       |     |      Database       |
|                     |     |                     |
+---------------------+     +---------------------+
         |                         |
         |                         |
         +-------------------------+
                   |
                   |
                   v
            +-----------------+
            |                 |
            | API Gateway     |
            |                 |
            +-----------------+

I hope this diagram helps you understand the evolution of SOA and MSA for the notes of the Unit 1 - Introduction: SOA and MSA Basics in the subject of Service Oriented Architecture. If you have any questions or feedback, please let me know.