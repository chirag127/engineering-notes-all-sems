A pattern-based architecture for service-oriented applications is an architecture that uses proven solutions to common design problems in the context of service-oriented architecture (SOA). SOA is an architectural style that defines a way to make software components reusable and interoperable via service interfaces. Services use common interface standards and an architectural pattern so they can be rapidly incorporated into new applications .

One of the common patterns for service-oriented applications is the enterprise service bus (ESB) pattern. An ESB is an architectural pattern whereby a centralized software component performs integrations between applications. It performs transformations of data models, handles connectivity/messaging, performs routing, converts communication protocols and potentially manages the composition of multiple requests.

The following diagram illustrates the basic architecture of a service-oriented application using the ESB pattern:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Application A  |     |  Application B  |     |  Application C  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
       +-----------------------+-----------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Service A      |     |  Service B      |     |  Service C      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
+-----------------+
|                 |
|  Enterprise     |
|  Service Bus    |
|                 |
+-----------------+
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Service D      |     |  Service E      |     |  Service F      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Application D  |     |  Application E  |     |  Application F  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

In this diagram, the applications (A, B, C, D, E, F) are the consumers and providers of services (