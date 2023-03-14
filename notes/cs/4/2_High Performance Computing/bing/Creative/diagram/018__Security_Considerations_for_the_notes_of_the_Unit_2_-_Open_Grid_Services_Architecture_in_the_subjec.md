The following diagram illustrates the basic architecture of a security system for open grid services, based on the document by Nagaratnam et al. . It shows how different security models, mechanisms, protocols, platforms and technologies can be integrated and unified to enable secure interoperability of grid services.

```
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|    Application    |  |    Application    |  |    Application    |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|    Grid Service   |  |    Grid Service   |  |    Grid Service   |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|    Security       |  |    Security       |  |    Security       |
|    Framework      |  |    Framework      |  |    Framework      |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|    Security       |  |    Security       |  |    Security       |
|    Mechanisms     |  |    Mechanisms     |  |    Mechanisms     |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|    Security       |  |    Security       |  |    Security       |
|    Protocols      |  |    Protocols      |  |    Protocols      |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|    Security       |  |    Security       |  |    Security       |
|    Platforms      |  |    Platforms      |  |    Platforms      |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
|                   |  |                   |  |                   |
|    Security       |  |    Security       |  |    Security       |
|    Technologies   |  |    Technologies   |  |    Technologies   |
|                   |  |                   |  |                   |
+-------------------+  +-------------------+  +-------------------+
```

The security framework provides a common interface for grid services to access security functions, such as authentication, authorization, confidentiality, integrity, auditing, and delegation. The security mechanisms implement these functions using various cryptographic algorithms and techniques. The security protocols define the message formats and exchange patterns for secure communication between grid services. The security platforms provide the underlying infrastructure and support for security, such as certificates, keys, tokens, and policies. The security technologies are the specific implementations of security platforms, such as Kerberos, SSL, PKI, SAML, XACML, etc.

The security architecture aims to support, integrate and unify different security models, such as identity-based, role-based, attribute-based, and policy-based. It also aims to enable interoperability between different security domains, such as local, enterprise, and global. It also aims to provide flexibility and extensibility for grid services to choose the appropriate security mechanisms, protocols, platforms and technologies according to their requirements and preferences.

: Nagaratnam, N., Janson, P., Dayka, J., Nadalin, A., Siebenlist, F., Welch, V., ... & Tuecke, S. (2002). The security architecture for open grid services. In Proceedings of the 1st International Workshop on Grid Computing Environments (pp. 1-15). IEEE.