### More on confinement techniques

Confinement techniques are methods to prevent unauthorized information flow from a process or a system to another entity. They are used to enforce the principle of least privilege, which states that a process or a system should only have the minimum access rights necessary to perform its function. Confinement techniques can be classified into two categories: static and dynamic.

- Static confinement techniques are applied before the execution of a process or a system, and they do not change during the execution. They include:

  - Access control mechanisms, such as discretionary access control (DAC), mandatory access control (MAC), or role-based access control (RBAC), that restrict the access rights of a process or a system to the resources it needs. For example, a web server can be run as a low-privilege user that can only read the web pages and write to the log files, but not access other files or execute other programs.
  - Encryption techniques, such as symmetric or asymmetric encryption, that protect the confidentiality of data stored or transmitted by a process or a system. For example, a file can be encrypted with a secret key before being stored on a cloud storage service, and only the authorized users can decrypt it with the same key.

- Dynamic confinement techniques are applied during the execution of a process or a system, and they can change according to the context or the behavior of the process or the system. They include:

  - Sandboxing techniques, such as virtual machines, containers, or software fault isolation, that isolate a process or a system from the rest of the system and limit its interactions with the external environment. For example, a browser can run a web application in a sandbox that prevents it from accessing the local files or the network, except for the web server that hosts the application.
  - Information flow control techniques, such as taint analysis, information flow labels, or declassification policies, that track the sources and the destinations of the data used or produced by a process or a system, and enforce rules to prevent or limit the leakage of sensitive data. For example, a database can label the data with different security levels, and only allow the data to flow to the processes or the systems that have the same or higher security levels.