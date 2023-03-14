Compliance with design and coding standards is a static testing strategy that aims to ensure that the code is readable, maintainable, secure, and compliant with industry or regulatory requirements. Static analysis tools can help to enforce coding standards by automatically detecting violations and reporting them as alerts. The following diagram illustrates the basic architecture of a static analysis tool:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Source code    |     |  Coding rules   |     |  Static analysis|
|                 |     |                 |     |  tool           |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                                     |
                                     |
                                     v
                             +-----------------+
                             |                 |
                             |  Alerts         |
                             |                 |
                             +-----------------+
```

The source code is the input to the static analysis tool, which checks it against a set of coding rules that define the coding standard. The coding rules can be predefined (such as MISRA or CERT) or customized by the user. The static analysis tool generates alerts for any violations of the coding rules, which can be reviewed and fixed by the developers. The alerts can also be used to measure the code quality and compliance level.