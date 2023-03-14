Mutation testing is a technique that evaluates the quality of a test suite by introducing small changes (mutations) in the source code and checking if the test suite can detect them. The following diagram illustrates the basic steps of mutation testing:

```
+----------------+      +-----------------+      +-----------------+
| Original       |      | Mutant          |      | Test suite      |
| program (P)    |----->| generator       |----->| executor        |
+----------------+      +-----------------+      +-----------------+
                                    |                     |
                                    |                     |
                                    v                     v
                              +-----------------+      +-----------------+
                              | Mutant          |      | Test results    |
                              | program (P')    |----->| analyzer        |
                              +-----------------+      +-----------------+
                                                          |
                                                          |
                                                          v
                                                     +-----------------+
                                                     | Mutation score  |
                                                     | report          |
                                                     +-----------------+
```

The mutation score is the ratio of killed mutants (detected by the test suite) to the total number of mutants. A higher mutation score indicates a better test suite.