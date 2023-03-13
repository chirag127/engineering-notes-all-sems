The difference between verification and validation in software testing can be summarized as follows:

- Verification is the process of checking whether the software conforms to the specified requirements and design specifications. It is a static mechanism of testing and does not involve executing the code. Verification uses methods like reviews, inspections, walkthroughs, and audits to evaluate the quality of the software artifacts.
- Validation is the process of checking whether the software meets the customer's needs and expectations. It is a dynamic mechanism of testing and always involves executing the code. Validation uses methods like black box testing, white box testing, and gray box testing to evaluate the functionality and behavior of the software.

The following diagram illustrates the difference between verification and validation in software testing using an ASCII art:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Requirements   |        |    Design       |        |    Code         |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        V                         V                         V
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Verification   |        |  Verification   |        |  Verification   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +-------------------------+-------------------------+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        V                         V                         V
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Validation     |        |  Validation     |        |  Validation     |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```