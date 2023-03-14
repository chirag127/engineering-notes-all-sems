### EA and SOA for Business and IT Alignment for the notes of the Unit 10 - EA and SOA for Business and IT Alignment in the subject of Service Oriented Architecture

- Enterprise Architecture (EA) is a framework that covers all the dimensions of IT architecture for the enterprise, such as business, data, application, and technology architectures .
- Service Oriented Architecture (SOA) is an architectural strategy that uses the concept of "Services" as the underlying business-IT alignment entity .
- Both EA and SOA share the objective of achieving business and IT alignment, which means ensuring that the IT solutions support the business goals and processes.
- SOA can impact EA frameworks, methodologies, governance and tools by providing a service-oriented perspective and enabling reuse, standardization, and innovation .
- EA and SOA can work together to effectively build an optimal IT landscape that is based on the principles of SOA, such as loose coupling, interoperability, and contract-based interaction.
- The steps to bridge the gap between EA and SOA are:
  - Modeling the business architecture with the business users and business analysts, using business processes, services, and roles as the key elements.
  - Defining the application architecture with the solution architects, using application components, functions, and services as the key elements.
  - Defining the infrastructure architecture with the infrastructure architects, using physical nodes, networks, and infrastructure services as the key elements.
  - Mapping the business, application, and infrastructure architectures to identify the dependencies, gaps, and overlaps among them.
  - Applying the SOA governance principles and processes to ensure the quality, consistency, and compliance of the architectures and services.
  - Implementing the SOA solutions using the SOA reference architecture, standards, and best practices as the guidelines.
- A mnemonic to remember the steps is: **MAD MAPS** (Model, Define, Define, Map, Apply, Implement, SOA).
- An example of a business process model is:

```
+----------------+    +----------------+    +----------------+
| Order Product  | -> | Ship Product   | -> | Invoice Product |
+----------------+    +----------------+    +----------------+
```

- An example of an application architecture diagram is:

```
+----------------+    +----------------+    +----------------+
| Order Service  | -> | Shipping Service | -> | Invoice Service |
+----------------+    +----------------+    +----------------+
    |                      |                      |
    v                      v                      v
+----------------+    +----------------+    +----------------+
| Order System   |    | Shipping System |    | Invoice System |
+----------------+    +----------------+    +----------------+
```

- An example of an infrastructure architecture diagram is:

```
+----------------+    +----------------+    +----------------+
| Order Server   | -> | Shipping Server | -> | Invoice Server |
+----------------+    +----------------+    +----------------+
    |                      |                      |
    v                      v                      v
+----------------+    +----------------+    +----------------+
| Order Database |    | Shipping Database |  | Invoice Database |
+----------------+    +----------------+    +----------------+
```

- An example of a mapping table is:

| Business Process | Business Service | Application Service | Application Component | Infrastructure Service | Infrastructure Node |
|------------------|------------------|---------------------|-----------------------|------------------------|---------------------|
| Order Product    | Order Product    | Order Service       | Order System          | Order Database Service | Order Server        |
| Ship Product     | Ship Product     | Shipping Service    | Shipping System       | Shipping Database Service | Shipping Server      |
| Invoice Product  | Invoice Product  | Invoice Service     | Invoice System        | Invoice Database Service | Invoice Server       |