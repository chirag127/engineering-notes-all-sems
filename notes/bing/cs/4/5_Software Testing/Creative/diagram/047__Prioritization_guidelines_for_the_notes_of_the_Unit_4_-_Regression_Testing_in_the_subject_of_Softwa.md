The following is a detailed ASCII diagram for prioritization guidelines for the notes of the Unit 4 - Regression Testing in the subject of Software Testing.

```
+----------------------+----------------------+----------------------+
| High priority test   | Medium priority test | Low priority test    |
| cases                | cases                | cases                |
+----------------------+----------------------+----------------------+
| - Cover the critical | - Include negative   | - Cover the remaining|
|   function of the    |   test scenarios     |   functionality of   |
|   application        |                      |   an application     |
| - Cover defect prone | - Cover less         | - Cover UI and less  |
|   modules and        |   critical modules   |   defect prone       |
|   modules that have  |                      |   modules            |
|   undergone recent   |                      |                      |
|   changes            |                      |                      |
| - Based on business  | - Based on previous  | - Based on low       |
|   requirements and   |   test cycle         |   business impact    |
|   impact             |   experience and     |                      |
|                      |   feedback           |                      |
| - Executed well in   | - Executed after     | - Executed last or   |
|   advance to improve |   high priority test |   skipped based on   |
|   product quality    |   cases              |   delivery timelines |
|   and performance    |                      |                      |
+----------------------+----------------------+----------------------+
```