According to the search results, regression testing is a type of software testing that re-executes test cases to check the previous functionality of the application is working fine, and the new changes have not produced any bugs. Regression testing can be performed on a new build when there is a significant change in the original functionality, or when a bug fix, a patch, or an optimization is applied to the source code. Regression testing is important to ensure the overall stability and functionality of the existing features, and to detect new bugs early in the deployment cycle. Regression testing is often automated, and it is the final step before the changes are integrated into the main development branch.

The following diagram illustrates the basic process of regression testing using ASCII characters:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Source Code   +---->+  Build System  +---->+  Test System   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       ^                      ^                      |
       |                      |                      |
       |                      |                      v
       |                      |             +----------------+
       |                      |             |                |
       |                      +-------------+  Test Results  |
       |                                    |                |
       +------------------------------------+----------------+
```

The source code is the input for the build system, which produces a new build that is deployed to the test system. The test system runs the test cases, which may include functional, non-functional, and regression tests, and generates the test results. The test results are then used to evaluate the quality of the new build, and to identify any regression bugs. If any regression bugs are found, they are reported back to the source code, where they are fixed and the cycle repeats.