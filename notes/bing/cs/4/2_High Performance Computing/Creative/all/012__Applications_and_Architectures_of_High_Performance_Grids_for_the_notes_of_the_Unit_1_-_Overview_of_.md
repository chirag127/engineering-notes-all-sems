### Applications and Architectures of High Performance Grids for the notes of the Unit 1 - Overview of Grid Computing Technology in the subject of High Performance Computing

- A grid is a distributed system that enables the sharing, selection, and aggregation of heterogeneous and geographically dispersed resources for solving large-scale problems in science, engineering, and commerce .
- A grid can harness the power of an arbitrarily large collection of computing resources to meet the needs of compute intensive high performance computing (HPC) applications such as finite element model (FEM) simulations .
- Grid applications can be classified into four categories based on their resource requirements and communication patterns:
  - High-throughput computing: These applications require a large number of independent tasks that can be executed in parallel on different resources. Examples include parameter sweep studies, Monte Carlo simulations, and bioinformatics applications.
  - On-demand computing: These applications require a large amount of computing power for a short duration of time. Examples include interactive simulations, online gaming, and real-time data analysis.
  - Data-intensive computing: These applications require a large amount of data that is distributed across multiple locations. Examples include data mining, scientific visualization, and multimedia applications.
  - Collaborative computing: These applications require a coordinated use of multiple resources by multiple users. Examples include teleconferencing, virtual reality, and distributed supercomputing.
- Grid architectures can be described by three layers:
  - The resource layer: This includes the physical and logical resources that are available on the grid, such as processors, memory, disk, network, software, and services. Grid users do not interact with this layer directly, but through the middleware layer.
  - The middleware layer: This includes the software components that provide the core functionality of the grid, such as resource discovery, allocation, scheduling, monitoring, security, and communication. Grid users interact with this layer through the application layer.
  - The application layer: This includes the grid applications and development toolkits that support the applications. Grid users interface with this layer and also provide general management and auditing functions. Different applications can be processed on grids and different organizations use grids for various use cases.
- A grid architecture can be designed and evaluated using the following criteria :
  - Scalability: The ability of the grid to handle a large number of resources and users without degrading the performance or functionality.
  - Interoperability: The ability of the grid to integrate heterogeneous and diverse resources and services from different domains and organizations.
  - Adaptability: The ability of the grid to adjust to the dynamic changes in the resource availability, user demand, and application requirements.
  - Reliability: The ability of the grid to provide consistent and correct results despite the failures and errors in the resources and services.
  - Security: The ability of the grid to protect the confidentiality, integrity, and availability of the resources, services, and data on the grid.
  - Usability: The ability of the grid to provide a user-friendly and intuitive interface for the grid users and developers.

- A possible mnemonic to remember the six criteria of grid architecture is **SIARUS** (Scalability, Interoperability, Adaptability, Reliability, Usability, Security).
- A possible learning trick to remember the four categories of grid applications is to associate them with the four elements of nature: **Fire** (High-throughput computing), **Air** (On-demand computing), **Water** (Data-intensive computing), and **Earth** (Collaborative computing).