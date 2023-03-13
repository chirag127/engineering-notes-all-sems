Configuration audits are essential processes in ensuring the quality and reliability of a software product. They provide an independent evaluation of the system's functionality, performance, and consistency with the relevant requirement specifications . Configuration audits are performed for all releases; however, audits of interim, internal releases may be less formal and rigorous, as defined by the project.

There are two types of configuration audits: the Functional Configuration Audit (FCA) and the Physical Configuration Audit (PCA) . The FCA verifies that the software product satisfies the functional requirements and the PCA verifies that the software product conforms to the physical design specifications.

The following diagram illustrates the basic steps of a configuration audit process in software engineering:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Prepare for    |       |  Conduct the    |       |  Report the     |
|  the audit      +------>+  audit          +------>+  audit results  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| - Identify the  |       | - Review the    |       | - Document the  |
|   audit scope   |       |   software      |       |   audit         |
| - Select the    |       |   configuration |       |   findings      |
|   audit team    |       |   items (CIs)   |       | - Communicate   |
| - Define the    |       | - Compare the   |       |   the audit     |
|   audit         |       |   CIs with the  |       |   outcomes      |
|   criteria      |       |   baseline      |       | - Recommend     |
| - Schedule the  |       |   documents     |       |   corrective    |
|   audit         |       | - Identify any  |       |   actions       |
| - Notify the    |       |   discrepancies |       | - Follow up on  |
|   stakeholders  |       |   or issues     |       |   the actions   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```