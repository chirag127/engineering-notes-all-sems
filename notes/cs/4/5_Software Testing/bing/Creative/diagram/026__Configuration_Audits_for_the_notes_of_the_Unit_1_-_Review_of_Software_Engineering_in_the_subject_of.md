Configuration audits are essential processes in ensuring the quality and reliability of a software product. They provide an independent evaluation of the system's functionality, performance, and consistency with the relevant requirement specifications. Configuration audits also verify that the software configuration items (CIs) have been developed and completed following the documents and requirements that define them, and that they achieve their performance and functional characteristics goals.

There are two types of configuration audits: the Functional Configuration Audit (FCA) and the Physical Configuration Audit (PCA). The FCA examines the functional characteristics of the configured product and verifies that the product has met, via test results, the requirements specified in its functional baseline documentation approved at the preliminary design review (PDR) and critical design review (CDR). The PCA verifies that the actual configuration of the product matches the documentation that defines it, and that all associated operational and support documents are complete and meet their requirements.

The following diagram illustrates the basic steps of a configuration audit process in software engineering:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|   Configuration |        |   Configuration |        |   Configuration |
|     Planning    |------->|     Control     |------->|      Audit      |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
| Define the CIs, |        | Manage changes  |        | Perform FCA and |
| baselines, and  |        | to the CIs and  |        | PCA to verify   |
| audit criteria  |        | baselines       |        | the CIs and     |
|                 |        |                 |        | baselines       |
+-----------------+        +-----------------+        +-----------------+
```