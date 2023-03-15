Software re-engineering is a process of software development which is done to improve the maintainability of a software system. It involves examining and modifying the system to reconstitute it in a new form. It can be done using different approaches, such as lump sum, incremental, or evolutionary .

A software re-engineering process model can be represented as a sequence of activities that are performed to transform a legacy system into a re-engineered system. One possible process model is shown below :

### Software Re- Engineering (SR) of Software

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Inventory      |     |  Document       |     |  Reverse        |
|  Analysis       |---->|  Restructuring  |---->|  Engineering    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
                                                            |
                                                            |
                                                            V
                                                    +-----------------+
                                                    |                 |
                                                    |  Source Code    |
                                                    |  Translation    |
                                                    |                 |
                                                    +-----------------+
                                                            |
                                                            |
                                                            V
                                                    +-----------------+
                                                    |                 |
                                                    |  Data           |
                                                    |  Re-engineering |
                                                    |                 |
                                                    +-----------------+
                                                            |
                                                            |
                                                            V
                                                    +-----------------+
                                                    |                 |
                                                    |  Forward        |
                                                    |  Engineering    |
                                                    |                 |
                                                    +-----------------+
                                                            |
                                                            |
                                                            V
                                                    +-----------------+
                                                    |                 |
                                                    |  Re-engineered  |
                                                    |  System         |
                                                    |                 |
                                                    +-----------------+
```

The process model consists of the following activities:

- Inventory Analysis: This activity involves identifying and assessing the legacy systems that need to be re-engineered. It also involves prioritizing and selecting the systems based on their business value, technical quality, and maintenance cost.
- Document Restructuring: This activity involves improving the quality and consistency of the documentation of the legacy systems. It also involves updating and standardizing the documentation to reflect the current state and requirements of the systems.
- Reverse Engineering: This activity involves extracting and recovering the design and functionality of the legacy systems from their source code, data, and documentation. It also involves creating abstract representations of the systems, such as models, diagrams, and specifications.
- Source Code Translation: This activity involves converting the source code of the legacy systems from one programming language to another, or from one platform to another. It also involves applying code restructuring and refactoring techniques to improve the readability, maintainability, and performance of the code.
- Data Re-engineering: This activity involves transforming the data structures and schemas of the legacy systems to make them compatible with the new platform, technology, or standards. It also involves migrating and cleansing the data to ensure its quality and integrity.
- Forward Engineering: This activity involves creating and implementing the new design and functionality of the re-engineered systems based on the abstract representations obtained from reverse engineering. It also involves testing and verifying the re-engineered systems to ensure their correctness and reliability.
- Re-engineered System: This is the final output of the software re-engineering process. It is a system that has been improved and modernized to meet the current and future needs of the users and stakeholders. It is also a system that has a lower maintenance cost and a higher quality than the legacy system.