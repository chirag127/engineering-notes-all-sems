 Here is the content in markdown format for the given topic:

### Design of Activity Services (or Business Services)

For the notes of the Unit 4 - Service-Oriented Analysis and Design in the subject of Service Oriented Architecture

- Activity services (or business services) are coarse-grained services that provide business functionality to client applications.
- They encapsulate a business process or a business task and may invoke other services to accomplish the goal.
- The granularity of an activity service is quite high (for e.g. process a purchase order). It may consist of several steps and invoke multiple fine-grained services to complete the process.
- The main purpose of an activity service is to provide a service-oriented interface to the business logic and functionality. It hides the implementation details of the business process it implements.
- The key aspects to consider while designing an activity service are:
-- Define the business process/task it will implement.
-- Identify the steps/sub-tasks in the process and the corresponding services required.
-- Determine the input and output data formats. The input data format should have all the required information to initiate the process. The output data format should contain the results/status of the completed process.
-- Evaluate if the service can be reused across other business processes. If so, the input and output data formats need to be designed accordingly to make it reusable.
-- Determine the non-functional requirements like performance, scalability, security, etc. and design the service to meet those requirements.
-- Choose a suitable service interface type (synchronous vs asynchronous) based on the nature of the business process and client applications.

[Detailed diagrams and examples can be added if required to explain the concepts]

The key is to design the activity services at the right level of granularity with well-defined functional and non-functional interfaces to provide a service-oriented access to the business functionality. This enhances the reusability and composability of the services which are key principles of service-oriented architecture.