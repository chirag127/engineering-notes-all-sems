Software version control is a management strategy to track and store changes to a software development document or set of files that follow the development project from beginning to end-of-life. It helps software teams manage changes to source code over time, compare earlier versions of the code, and resolve conflicts between concurrent work. Software version control systems are software tools that facilitate this process.

One of the common models of software version control is the centralized model, where a single server hosts the master repository and all developers work on their own local copies of the files. The developers can commit their changes to the server, update their local copies with the latest changes from the server, and merge their work with others. The centralized model is simple and easy to use, but it has some drawbacks, such as a single point of failure, dependency on network connectivity, and limited scalability.

Another model of software version control is the distributed model, where every developer has a full copy of the repository on their own machine, and can work independently without relying on a central server. The developers can commit their changes locally, and push or pull their changes to or from other repositories as needed. The distributed model is more flexible and robust, but it also requires more coordination and communication between developers, and more complex workflows.

The following diagram illustrates the basic architecture of a centralized and a distributed version control system using ASCII art:

```
Centralized Version Control System

    +-----------------+       +-----------------+
    | Developer 1     |       | Developer 2     |
    | Local Copy      |       | Local Copy      |
    +-----------------+       +-----------------+
          |   ^                     |   ^
          |   |                     |   |
          v   |                     v   |
    +-----------------------------------------+
    | Server                                 |
    | Master Repository                      |
    +-----------------------------------------+

Distributed Version Control System

    +-----------------+       +-----------------+
    | Developer 1     |       | Developer 2     |
    | Local Repository|       | Local Repository|
    +-----------------+       +-----------------+
          |   ^                     |   ^
          |   |                     |   |
          v   |                     v   |
    +-----------------------------------------+
    | Remote Repository                     |
    | (Optional)                            |
    +-----------------------------------------+
```