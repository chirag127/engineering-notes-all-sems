# Finding vulnerabilities for the notes of the Unit 3 - Secure architecture principles isolation and least privilege in the subject of COMPUTER SYSTEM SECURITY

- Secure architecture principles are guidelines for designing and implementing systems that are resilient to attacks and can protect the confidentiality, integrity, and availability of data and resources.
- Isolation and least privilege are two of the most important secure architecture principles that aim to reduce the attack surface and limit the damage of a successful breach.
- Isolation means separating different components or layers of a system, such as processes, networks, data, or users, so that they cannot interfere with each other or access unauthorized information or resources.
- Least privilege means granting the minimum amount of permissions or access rights to each component or user of a system, so that they can only perform the tasks or activities that are necessary for their function or role.
- Finding vulnerabilities for these principles involves identifying and analyzing the potential ways that an attacker can exploit the lack of isolation or least privilege in a system, such as:
  - Escalating privileges by exploiting a weak or misconfigured authentication or authorization mechanism, or by exploiting a vulnerability in a component that has higher privileges than necessary.
  - Bypassing isolation by exploiting a vulnerability in a component that can communicate or interact with other components, or by exploiting a shared resource or dependency that is not properly isolated or protected.
  - Compromising data or resources by exploiting a vulnerability in a component that can access or manipulate sensitive or critical information or resources, or by exploiting a data leak or exposure that is not properly isolated or protected.
- Some examples of vulnerabilities for these principles are:
  - A buffer overflow vulnerability in a web server that allows an attacker to execute arbitrary code with the same privileges as the web server, which may be higher than necessary for serving web pages.
  - A SQL injection vulnerability in a web application that allows an attacker to execute arbitrary SQL commands on the database server, which may not be properly isolated from other servers or networks.
  - A cross-site scripting vulnerability in a web application that allows an attacker to inject malicious scripts into the web pages of other users, which may access or manipulate their cookies, session tokens, or other sensitive data.
  - A misconfigured firewall that allows an attacker to access or scan the internal network of a system, which may contain other vulnerable or unprotected components or resources.
  - A weak encryption or hashing algorithm that allows an attacker to decrypt or crack the passwords or data of a system, which may not be properly isolated or protected.