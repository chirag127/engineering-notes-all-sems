# Access Control Concepts

Access control is a security technique that regulates who or what can view or use resources in a computing environment. It is a feature of modern Zero Trust security philosophy, which applies techniques like explicit verification and least-privileged access to help secure sensitive information and prevent it from falling into the wrong hands.

Access control relies heavily on two key principles—authentication and authorization:

- Authentication involves identifying a particular user based on their login credentials, such as usernames and passwords, biometric scans, PINs, or security tokens.
- Authorization refers to giving a user the appropriate level of access as determined by access control policies. These processes are typically automated.

Access control models have a subject and an object. The subject—the human user—is the one trying to gain access to the object—usually the software.

Some common access control models are:

- Discretionary Access Control (DAC): The owner of the object decides who can access it and with what permissions.
- Mandatory Access Control (MAC): The system assigns a security label to each object and user, and enforces access based on the comparison of these labels.
- Role-Based Access Control (RBAC): The system assigns roles to users based on their functions, and grants access to objects based on the roles.
- Attribute-Based Access Control (ABAC): The system grants access to objects based on the attributes of the user, the object, and the environment.

Key concepts that make up access control are permissions, ownership of objects, inheritance of permissions, user rights, and object auditing:

- Permissions are the actions that a user can perform on an object, such as read, write, execute, delete, etc.
- Ownership of objects is the relationship between a user and an object that gives the user full control over the object.
- Inheritance of permissions is the process of propagating permissions from a parent object to a child object.
- User rights are the abilities that a user has to perform system-level tasks, such as logging on, changing the system time, shutting down the system, etc.
- Object auditing is the process of recording and reviewing the events that occur on an object, such as who accessed it, when, and what actions they performed.

Access control is an essential component of computer system security, as it helps to protect the confidentiality, integrity, and availability of the system and its resources. Access control also helps to enforce the principle of least privilege, which states that a user should only have the minimum level of access required to perform their tasks.