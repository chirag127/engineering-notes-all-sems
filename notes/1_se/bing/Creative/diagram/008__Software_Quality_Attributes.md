Software quality attributes are the non-functional requirements of software that describe how well the software meets the expectations of the users and the stakeholders. Different software quality attributes may have different levels of importance depending on the type, domain, and purpose of the software. Some of the common software quality attributes are:

- Availability: The degree to which the software is operational and accessible when required.
- Correctness: The degree to which the software conforms to the specifications and requirements.
- Interoperability: The degree to which the software can exchange data and cooperate with other systems or components.
- Modifiability: The degree to which the software can be changed or extended to meet new or changing requirements.
- Maintainability: The degree to which the software can be modified, tested, and corrected with ease and efficiency.
- Performance: The degree to which the software responds and executes tasks within acceptable time and resource limits.
- Usability: The degree to which the software is easy to learn, use, and understand by the intended users.
- Reusability: The degree to which the software or its components can be reused in other software products or contexts.
- Security: The degree to which the software protects the data and the system from unauthorized access, modification, or damage.

The following diagram illustrates the basic architecture of a software quality model based on the ISO/IEC 25010 standard, which defines eight quality characteristics and five quality-in-use characteristics for software products.

### Software Quality Attributes

```
+---------------------+    +---------------------+
|                     |    |                     |
|  Quality-in-use     |    |    Product quality  |
|                     |    |                     |
+---------------------+    +---------------------+
|                     |    |                     |
|  Effectiveness      |    |  Functional         |
|  Efficiency         |    |  suitability        |
|  Satisfaction       |    |  Reliability        |
|  Freedom from risk  |    |  Performance        |
|  Context coverage   |    |  efficiency         |
|                     |    |  Operability        |
+---------------------+    |  Security           |
       ^                  |  Compatibility       |
       |                  |  Maintainability     |
       |                  |  Portability         |
       |                  |                     |
       +------------------+---------------------+
```