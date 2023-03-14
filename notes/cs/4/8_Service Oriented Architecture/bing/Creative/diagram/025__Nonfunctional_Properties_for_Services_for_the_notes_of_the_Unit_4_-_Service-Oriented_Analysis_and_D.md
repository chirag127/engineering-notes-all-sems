Non-functional properties for services are the qualities and features that are desirable by the service users, but are not directly related to the functionality of the service. Some examples of non-functional properties are availability, performance, security, reliability, scalability, usability, etc. Non-functional properties are often specified in service level agreements (SLAs) between the service provider and the service consumer, and are measured by metrics such as response time, uptime, throughput, error rate, etc. Non-functional properties can have a significant impact on the cost, quality, and satisfaction of the service.

A possible diagram to illustrate the non-functional properties for services is shown below. The diagram uses the Unified Modeling Language (UML) notation to represent the service as a component, and the non-functional properties as stereotypes. The diagram also shows the dependencies between the service and the non-functional properties, and the metrics used to measure them.

```ascii
+---------------------+
|      <<Service>>    |
|                     |
|    Service Name     |
+---------------------+
|                     |
|  Functionalities    |
|                     |
+---------------------+
|                     |
|  Service Interface  |
|                     |
+---------------------+
  ^       ^       ^
  |       |       |
  |       |       |
  |       |       |
  |       |       |
  |       |       |
  |       |       |
  |       |       |
  |       |       |
  |       |       |
  |       |       |
  |       |       |
  |       |       |
+---------------------+  +---------------------+  +---------------------+
|    <<Availability>> |  |    <<Performance>>  |  |     <<Security>>    |
|                     |  |                     |  |                     |
|  Availability Level |  |  Performance Level  |  |  Security Level     |
+---------------------+  +---------------------+  +---------------------+
|                     |  |                     |  |                     |
|  Uptime (%)         |  |  Response Time (ms) |  |  Encryption (bit)   |
|  Downtime (min)     |  |  Throughput (req/s) |  |  Authentication     |
|  MTBF (h)           |  |  Error Rate (%)     |  |  Authorization      |
|  MTTR (min)         |  |  Latency (ms)       |  |  Audit Trail        |
|                     |  |                     |  |                     |
+---------------------+  +---------------------+  +---------------------+
```