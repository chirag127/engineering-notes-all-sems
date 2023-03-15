Function Point (FP) Based Measures are a way of estimating the size and complexity of a software project based on the functionality that the user requests and receives. They are independent of the technology or programming language used for implementation. They are calculated by identifying and counting five types of components: external inputs, external outputs, external inquiries, internal logical files, and external interface files. Each component is assigned a complexity level (low, average, or high) based on the number of data elements and record element types involved. Then, each component is multiplied by a weight factor according to its type and complexity level. The sum of these products is the unadjusted function point (UFP) count. The UFP count is then adjusted by applying a complexity adjustment factor (CAF) that ranges from 0.65 to 1.35 based on 14 general system characteristics. The final result is the adjusted function point (AFP) count, which represents the size of the software functionality.

A possible ASCII diagram for Function Point (FP) Based Measures in software design is:

```
+-----------------+     +-----------------+     +-----------------+
| External Inputs |     | External Outputs|     | External Inquiries |
+-----------------+     +-----------------+     +-----------------+
| Complexity:     |     | Complexity:     |     | Complexity:     |
| Low: 3          |     | Low: 4          |     | Low: 3          |
| Average: 4      |     | Average: 5      |     | Average: 4      |
| High: 6         |     | High: 7         |     | High: 6         |
+-----------------+     +-----------------+     +-----------------+
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         |                       |                       |
         v                       v                       v
+-----------------+     +-----------------+     +-----------------+
| Internal Logical|     | External Interface|    | Unadjusted      |
| Files           |     | Files            |    | Function Point  |
+-----------------+     +-----------------+     +-----------------+
| Complexity:     |     | Complexity:     |    | UFP = Sum of    |
| Low: 7          |     | Low: 5          |    | (Component      |
| Average: 10     |     | Average: 7      |    | Count x Weight) |
| High: 15        |     | High: 10        |    +-----------------+
+-----------------+     +-----------------+              |
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
                                                        v
+-----------------+     +-----------------+
| Complexity      |     | Adjusted        |
| Adjustment      |     | Function Point  |
| Factor          |     +-----------------+
+-----------------+     | AFP = UFP x CAF |
| CAF = 0.65 +    |     +-----------------+
| (Sum of GSCs /  |
| 100)            |
+-----------------+
| GSCs: 14        |
| General System  |
| Characteristics |
+-----------------+
```