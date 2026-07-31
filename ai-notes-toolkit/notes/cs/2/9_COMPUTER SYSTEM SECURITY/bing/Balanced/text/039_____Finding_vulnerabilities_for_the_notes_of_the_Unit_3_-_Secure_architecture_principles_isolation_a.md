### Finding vulnerabilities for the notes of the Unit 3 - Secure architecture principles isolation and least privilege in the subject of COMPUTER SYSTEM SECURITY

- Secure architecture principles are guidelines for designing systems that are resilient to cyberattacks and protect the confidentiality, integrity and availability of data and resources.
- Isolation and least privilege are two important secure architecture principles that aim to limit the exposure and impact of potential vulnerabilities .
- Isolation means separating different components or layers of a system, such as data, processes, networks, or users, so that they cannot interfere with each other or access unauthorized information .
- Least privilege means granting the minimum level of access or permissions to each component or user of a system, so that they can only perform the tasks that are necessary for their role or function .
- Vulnerabilities are weaknesses or flaws in a system that can be exploited by malicious actors to compromise the security of the system or its data .
- Some common vulnerabilities that can violate the principles of isolation and least privilege are :
  - Privilege escalation: when an attacker gains higher-level access or permissions than intended, such as by exploiting a bug, misconfiguration, or stolen credentials, and uses it to access sensitive data or perform malicious actions .
  - Cross-site scripting (XSS): when an attacker injects malicious code into a web page or application that is executed by the browser of another user, and uses it to steal cookies, session tokens, or other information, or to perform actions on behalf of the victim .
  - SQL injection: when an attacker injects malicious SQL queries into a web page or application that interacts with a database, and uses it to read, modify, or delete data, or to execute commands on the database server .
  - Insecure direct object references: when an attacker accesses or modifies a resource or data object directly by manipulating its identifier, such as a file name, URL, or database key, without proper authorization or validation .
- Some general protection measures that can help prevent or mitigate these vulnerabilities are  :
  - Implementing strong authentication and authorization mechanisms, such as passwords, tokens, certificates, or multi-factor authentication, to verify the identity and access rights of users and components .
  - Encrypting data in transit and at rest, using secure protocols and algorithms, to protect it from unauthorized access or modification .
  - Validating and sanitizing user input, output, and parameters, to prevent malicious code or queries from being executed or injected .
  - Applying the principle of least privilege to all users and components, by assigning them the minimum permissions and access levels required for their tasks, and revoking them when no longer needed  .
  - Applying the principle of isolation to all components and layers, by separating them into different modules, processes, networks, or domains, and enforcing strict boundaries and controls between them  .
  - Keeping the system and its components updated, patched, and monitored, to fix any known bugs, vulnerabilities, or misconfigurations, and to detect and respond to any suspicious or anomalous activities .