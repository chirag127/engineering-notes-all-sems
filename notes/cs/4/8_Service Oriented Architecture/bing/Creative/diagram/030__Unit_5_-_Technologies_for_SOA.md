## Unit 5 - Technologies for SOA

Service-oriented architecture (SOA) is a software development model that allows services to communicate across different platforms and languages to form applications. In SOA, a service is a self-contained unit of software designed to complete a specific task. Service-oriented architecture allows various services to communicate using a loose coupling system to either pass data or coordinate an activity.

Some standard protocols to implement SOA include the following:

- Simple Object Access Protocol (SOAP)
- RESTful HTTP
- Apache Thrift
- Apache ActiveMQ
- Java Message Service (JMS)

The following diagram illustrates the basic architecture of a SOA-based system:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service        |       |  Service        |       |  Service        |
|  Provider       |       |  Provider       |       |  Provider       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
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
        |                       |                       |
        +-----------------------+-----------------------+
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
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +-----------------------+-----------------------+
        |                       |                       |
        |                       |                       |