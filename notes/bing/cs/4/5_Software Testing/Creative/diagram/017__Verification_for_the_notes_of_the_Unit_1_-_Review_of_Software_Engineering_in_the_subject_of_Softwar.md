### Verification for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

Verification is the process of checking that a software achieves its goal without any bugs. It is the process to ensure whether the product that is developed is right or not. It verifies whether the developed product fulfills the requirements that we have. Verification is Static Testing.

Verification operations include reviews, walk-throughs, and inspections. Although verification can assist to identify whether the program is of good quality, it cannot guarantee that the system is functional. The purpose of verification is to determine if the system is well-engineered and error-free.

A brief explanation of what is verification in software testing would be: it is the process of assessing software to evaluate if the results of a certain development phase meet the requirements established at the beginning of that phase.

Verification denotes precision of the end or final product. It conducts software review, walk through, inspection, and evaluates documents, plans, requirements, and specifications. It demonstrates the consistency, completeness, and correctness of the software during each stage of the software development life cycle.

Usually performed manually, software review is used to verify various documents like requirements, system designs, codes, test plans and test cases. To improve the productivity of the development team. To make the testing process time and cost effective. To make the final software with fewer defects.

The following diagram illustrates the basic architecture of a verification process in software testing:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Requirements   |     |  System Design  |     |  Source Code    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        v                     v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Requirements   |     |  System Design  |     |  Source Code    |
|    Review       |     |    Review       |     |    Review       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        v                     v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Requirements   |     |  System Design  |     |  Source Code    |
|  Inspection     |     |  Inspection     |     |  Inspection     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        v                     v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Requirements   |     |  System Design  |     |  Source Code    |
|  Walk-through   |     |  Walk-through   |     |  Walk-through   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        |                     |                       |
        v                     v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Verification   |     |  Verification   |     |  Verification   |