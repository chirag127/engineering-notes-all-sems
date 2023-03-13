### Constructive Cost Models (COCOMO) in software project management

COCOMO is a software cost estimation model that predicts the effort, cost, and schedule of a software project based on the size of the software measured in lines of code (LOC) and other factors such as project type, development mode, and cost drivers    .

COCOMO has three levels of complexity: basic, intermediate, and detailed. Each level provides more accuracy and detail in the estimation, but also requires more information and parameters to be specified    .

The following diagram illustrates the basic architecture of a COCOMO model using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Basic COCOMO   |    | Intermediate    |    |  Detailed       |
|                 |    |    COCOMO       |    |   COCOMO        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Effort = a *   |    |  Effort = a *   |    |  Effort = SUM   |
|  (Size)^b       |    |  (Size)^b *     |    |  (PMi)          |
|                 |    |  EAF            |    |                 |
|  Cost = c *     |    |  Cost = c *     |    |  Cost = c *     |
|  Effort         |    |  Effort         |    |  Effort         |
|                 |    |                 |    |                 |
|  Schedule = d * |    |  Schedule = d * |    |  Schedule = d * |
|  (Effort)^e     |    |  (Effort)^e     |    |  (Effort)^e     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  a, b, c, d, e  |    |  a, b, c, d, e  |    |  a, b, c, d, e  |
|  depend on      |    |  depend on      |    |  depend on      |
|  project type   |    |  project type   |    |  project type   |
|                 |    |                 |    |                 |
|  Size = LOC     |    |  Size = LOC     |    |  Size = LOC     |
|                 |    |                 |    |                 |
|  EAF = N/A      |    |  EAF = product  |    |  EAF = product  |
|                 |    |  of cost        |    |  of cost        |
|                 |    |  drivers        |    |  drivers        |
|                 |    |                 |    |                 |
|  PMi = N/A      |    |  PMi = N/A      |    |  PMi = effort   |
|                 |    |                 |    |  for each       |
|                 |    |                 |    |  module i       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

: Software Engineering | COCOMO Model - GeeksforGeeks
: Constructive Cost Model (COCOMO) - Techopedia.com
: COCOMO Model | Types of COCOMO Model | Pros and Cons - EDUCBA
: COCOMO - Wikipedia
: Software Engineering | COCOMO Model - GeeksforGeeks