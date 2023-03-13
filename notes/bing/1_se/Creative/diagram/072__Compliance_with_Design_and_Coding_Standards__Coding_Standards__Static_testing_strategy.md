Compliance with Design and Coding Standards (Coding Standards) Static testing strategy is a process of verifying the quality, security, and compliance of the source code by using static analysis tools. Static analysis tools check the code against predefined rules and guidelines, such as MISRA, CERT, or ISO 26262, and report any violations or defects. Static analysis can be performed at any stage of the software development life cycle, but it is recommended to perform it as early as possible, preferably during the coding phase, to reduce the cost and effort of fixing the issues later.

The following diagram illustrates the basic architecture of a Compliance with Design and Coding Standards (Coding Standards) Static testing strategy:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Source Code  |------>| Static Analysis|------>|  Report and    |
|                |       |     Tools      |       |  Review Issues |
+----------------+       +----------------+       +----------------+
```

The diagram shows the following steps:

- The source code is the input for the static analysis tools. The source code can be written in any programming language, such as C, C++, Java, Python, etc.
- The static analysis tools scan the source code and check it against the predefined rules and guidelines. The tools can be configured to enforce different levels of compliance, such as mandatory, required, or advisory. The tools can also be integrated with the development environment, such as IDEs, code editors, or version control systems, to provide real-time feedback and suggestions to the developers.
- The report and review issues step is the output of the static analysis tools. The report contains the list of issues found by the tools, such as defects, vulnerabilities, or compliance violations. The report also provides the severity, priority, and location of each issue, as well as the suggested fix or mitigation. The report can be viewed in various formats, such as HTML, XML, PDF, etc. The report can also be exported to other tools, such as bug tracking systems, code review tools, or quality management systems, to facilitate the resolution and verification of the issues.