Cost monitoring in software project management is the process of tracking the costs associated with a software project, like the cost of development, the cost of maintenance, and any associated expenses. This process helps project managers to track progress and make sure they stay within budget.

One of the techniques used for cost monitoring is Earned Value Analysis (EVA), which provides an integrated view of the project by measuring planned effort (costs), actual progress (earned value), and effort (actual costs) in terms of monetary values.

The following diagram illustrates the basic architecture of a cost monitoring system in software project management using EVA:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Project Plan   |    |  Project Data   |    |  Project Report |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Planned Costs  |    |  Actual Costs   |    |  Cost Variance  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Planned Value  |    |  Earned Value   |    |  Schedule       |
|                 |    |                 |    |  Variance       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Planned Time   |    |  Actual Time    |    |  Performance    |
|                 |    |                 |    |  Indexes        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
        |                     |                      |
        |                     |                      |
        +---------------------+----------------------+
                              |
                              |
                              v
                      +-----------------+
                      |                 |
                      |  Cost Monitor   |
                      |                 |
                      +-----------------+
                      |                 |
                      |  EVA Formulae   |
                      |                 |
                      +-----------------+
                      |                 |
                      |  EVA Metrics    |
                      |                 |
                      +-----------------+
                      |                 |
                      |  EVA Charts     |
                      |                 |
                      +-----------------+
```

The cost monitor is a software tool that collects the project data from various sources, such as the project plan, the project management software, the accounting software, etc. It then applies the EVA formulae to calculate the EVA metrics, such as the cost variance, the schedule variance, the cost performance index, the schedule performance index, etc. It also generates the EVA charts, such as the S-curve, the cumulative cost curve, the earned value curve, etc. These charts help the project manager to visualize the project performance and identify any deviations from the plan. The cost monitor then produces the project report, which summarizes the project status and provides recommendations for corrective actions if needed.