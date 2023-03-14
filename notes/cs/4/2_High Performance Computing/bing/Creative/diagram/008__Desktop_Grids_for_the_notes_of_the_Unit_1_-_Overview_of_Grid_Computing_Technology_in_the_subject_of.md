Desktop grids are a type of grid computing that use idle computing resources of desktop computers connected by a network to perform large-scale parallel or distributed computations. Desktop grids are often used for scientific research, such as climate modeling, protein folding, or drug discovery. Desktop grids can be classified into two categories: volunteer computing and organizational computing. Volunteer computing involves users who voluntarily donate their computing power to a project, while organizational computing involves using the desktop computers within an organization, such as a university or a company, for internal purposes.

A desktop grid typically consists of three components: a server, a client, and a middleware. The server is the central component that manages the tasks, distributes them to the clients, and collects the results. The client is the software that runs on the desktop computers and executes the tasks assigned by the server. The middleware is the software that connects the server and the clients, and handles the communication, security, fault tolerance, and load balancing issues.

The following diagram illustrates the basic architecture of a desktop grid using ASCII characters:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Server       |      |    Server       |      |    Server       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    Client       |      |    Client       |      |    Client       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows three servers and three clients, but in reality, a desktop grid can have many more servers and clients, depending on the size and scope of the project. The servers and clients can be located in different geographical locations, and can communicate over the Internet or a local area network. The middleware can be implemented using various technologies, such as web services, message passing, or peer-to-peer protocols. Some examples of desktop grid middleware are BOINC, Condor, and XtremWeb.