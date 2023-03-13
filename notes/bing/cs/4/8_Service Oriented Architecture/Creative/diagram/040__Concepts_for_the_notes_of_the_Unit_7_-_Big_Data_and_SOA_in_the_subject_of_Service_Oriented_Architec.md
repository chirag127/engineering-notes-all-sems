The following is a detailed ASCII diagram for the concepts of the notes of the Unit 7 - Big Data and SOA in the subject of Service Oriented Architecture.

### Concepts

- Big Data: The term used to describe the massive volume, variety and velocity of data that is difficult to process using traditional methods.
- SOA: Service-Oriented Architecture, an architectural approach that supports integrating business data and processes by creating reusable components of functionality, or services.
- Data Services: Services that provide access to data sources and perform data manipulation, transformation and integration tasks.
- Web Services: Services that use common interface standards and protocols, such as SOAP and REST, to communicate over the internet.
- BPM: Business Process Management, a discipline that involves modeling, executing, monitoring and optimizing business processes using software tools and methodologies.

### Diagram

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Data Source  |     |   Data Source  |     |   Data Source  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Data Service  |     |  Data Service  |     |  Data Service  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       +---------------------+---------------------+
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
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Web Service   |     |  Web Service   |     |  Web Service   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       +---------------------+---------------------+
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
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  BPM Process   |     |  BPM Process   |     |  BPM Process   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```