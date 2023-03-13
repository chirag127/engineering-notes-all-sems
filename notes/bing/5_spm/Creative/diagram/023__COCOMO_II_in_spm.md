COCOMO II is a software cost estimation model that consists of three sub-models: Application Composition, Early Design, and Post-Architecture. Each sub-model uses different inputs and formulas to estimate the effort, cost, and schedule of a software project. The following diagram illustrates the basic architecture of COCOMO II in SPM (Software Project Management):

```
+-------------------+    +-------------------+    +-------------------+
| Application       |    | Early Design      |    | Post-Architecture |
| Composition       |    |                   |    |                   |
+-------------------+    +-------------------+    +-------------------+
| Inputs:           |    | Inputs:           |    | Inputs:           |
| - Object Points   |    | - Size (KLOC)     |    | - Size (KLOC)     |
| - Productivity    |    | - Scale Factors   |    | - Scale Factors   |
|   Rate            |    | - Cost Drivers    |    | - Cost Drivers    |
+-------------------+    +-------------------+    +-------------------+
| Outputs:          |    | Outputs:          |    | Outputs:          |
| - Effort (PM)     |    | - Effort (PM)     |    | - Effort (PM)     |
| - Schedule (M)    |    | - Schedule (M)    |    | - Schedule (M)    |
| - Cost ($)        |    | - Cost ($)        |    | - Cost ($)        |
+-------------------+    +-------------------+    +-------------------+
| Formulas:         |    | Formulas:         |    | Formulas:         |
| - Effort =        |    | - Effort =        |    | - Effort =        |
|   (Object Points  |    |   A * Size^E      |    |   A * Size^E      |
|   / Productivity  |    | - Schedule =      |    | - Schedule =      |
|   Rate) * 0.4     |    |   B * Effort^F    |    |   B * Effort^F    |
| - Schedule =      |    | - Cost =          |    | - Cost =          |
|   3.0 * Effort^0.33|    |   Effort *        |    |   Effort *        |
| - Cost =          |    |   Average Salary  |    |   Average Salary  |
|   Effort *        |    | - A, E, B, F are  |    | - A, E, B, F are  |
|   Average Salary  |    |   derived from    |    |   derived from    |
| - Object Points   |    |   Scale Factors   |    |   Scale Factors   |
|   are estimated   |    |   and Cost Drivers|    |   and Cost Drivers|
|   based on the    |    | - Size is         |    | - Size is         |
|   number and      |    |   estimated based |    |   estimated based |
|   complexity of   |    |   on analogy,     |    |   on analogy,     |
|   screens,        |    |   expert judgment,|    |   expert judgment,|
|   reports, and    |    |   or function     |    |   or function     |
|   components      |    |   points          |    |   points          |
+-------------------+    +-------------------+    +-------------------+
```