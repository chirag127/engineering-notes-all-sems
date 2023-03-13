The following diagram illustrates the basic architecture of a service-oriented system using different technologies for service integration. The diagram is drawn using ASCII characters.

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Application   |     |   Application   |     |   Application   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Service     |     |     Service     |     |     Service     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     SOAP        |     |     REST        |     |     Thrift      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     HTTP        |     |     HTTP        |     |     TCP         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     JMS         |     |     ActiveMQ    |     |     Lambda      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     ESB         |     |     ESB         |     |     ESB         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     SOA         |     |     SOA         |     |     SOA         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```