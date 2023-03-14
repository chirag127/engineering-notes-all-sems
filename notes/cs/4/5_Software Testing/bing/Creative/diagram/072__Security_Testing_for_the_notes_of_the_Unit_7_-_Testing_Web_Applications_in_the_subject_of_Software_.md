Security testing web applications is a process of identifying and mitigating vulnerabilities in web applications and web services. Security testing web applications can be done using various methodologies and tools, such as OWASP Web Security Testing Guide, Penetration Testing Execution Standard, Web Application Security Consortium Threat Classification, etc. Security testing web applications can be divided into several types, such as vulnerability scanning, penetration testing, code review, security audit, etc. Security testing web applications can also involve using a web application firewall to protect the web application from malicious attacks.

The following diagram illustrates the basic architecture of a web application and the security testing activities that can be performed on it:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Browser      |<----->|  Web Server     |<----->|  Database       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
      ^                         ^    ^                     ^
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| Vulnerability   |       | Penetration     |       | Code Review     |
| Scanner         |       | Testing         |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      |                         |    |                     |
      v                         v    v                     v
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| Security Audit  |       | Web Application |       | Security Audit  |
|                 |       | Firewall        |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows that security testing web applications can be done at different layers of the web application architecture, such as the browser, the web server, and the database. Security testing web applications can also involve different types of activities, such as vulnerability scanning, penetration testing, code review, security audit, and web application firewall. Each type of security testing activity has its own purpose, scope, and limitations, and they can complement each other to provide a comprehensive security assessment of the web application.