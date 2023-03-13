Effort and cost estimation techniques in software project management (SPM) are methods and tools that help to estimate the size, effort, and cost of a software project. They are used to plan, budget, and control the software development process. Some of the common techniques are:

- **Decomposition technique**: This technique breaks down a project into smaller and manageable units, such as functions, modules, or activities. The size, effort, and cost of each unit are estimated separately and then aggregated to get the total estimate. This technique can use different methods to estimate the size, such as lines of code, function points, or use cases.  
- **Analogy technique**: This technique uses historical data from similar completed projects to estimate the size, effort, and cost of the current project. The similarity can be based on various factors, such as domain, technology, complexity, or team size. This technique requires a database of past projects and a method to adjust the estimates for the differences between the projects.  
- **Expert judgment technique**: This technique relies on the experience and intuition of experts who have knowledge of the project domain, technology, and methodology. The experts can use various sources of information, such as requirements, specifications, prototypes, or benchmarks, to provide their estimates. This technique can use different methods to elicit and combine the expert opinions, such as Delphi method, wideband Delphi method, or planning poker.  
- **Algorithmic technique**: This technique uses mathematical models and formulas to estimate the size, effort, and cost of a software project based on some input parameters, such as size, complexity, productivity, or quality. The models can be empirical, derived from statistical analysis of historical data, or theoretical, based on assumptions and principles of software engineering. Some of the well-known models are COCOMO, SLIM, Function Point Analysis, or SEER-SEM.  

The following diagram illustrates the basic architecture of a software cost estimation process using these techniques:

```
+-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |
| Decomposition   |     | Analogy         |     | Expert Judgment |     | Algorithmic     |
| Technique       |     | Technique       |     | Technique       |     | Technique       |
|                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+
         |                     |                     |                     |
         |                     |                     |                     |
         +---------------------+---------------------+---------------------+
                                       |
                                       |
                                       v
                              +-----------------+
                              |                 |
                              | Cost Estimation |
                              | Process         |
                              |                 |
                              +-----------------+
                                       |
                                       |
                                       v
                              +-----------------+
                              |                 |
                              | Cost Estimate   |
                              |                 |
                              +-----------------+
```