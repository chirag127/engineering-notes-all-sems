Mutation testing is a white box testing technique that involves modifying a program in small ways and evaluating the quality of existing test cases. It can be applied to various software artifacts, such as code, design models, specifications, databases, etc.  

The following diagram illustrates the basic architecture of a mutation testing system:

```
+-----------------+     +-----------------+     +-----------------+
| Original source |     | Mutant generator|     | Mutant programs |
| code            |---->|                 |---->|                 |
+-----------------+     +-----------------+     +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 +-----------------+
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |                 |
                                                 |