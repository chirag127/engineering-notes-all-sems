### Access Control Concepts

Access control is a security technique that regulates who or what can view or use resources in a computing environment. It is a fundamental concept in security that minimizes risk to the business or organization.

Access control relies heavily on two key principles—authentication and authorization:

- Authentication involves identifying a particular user based on their login credentials, such as usernames and passwords, biometric scans, PINs, or security tokens.
- Authorization refers to giving a user the appropriate level of access as determined by access control policies. These processes are typically automated.

Access control models have a subject and an object. The subject—the human user—is the one trying to gain access to the object—usually the software.

Some of the common access control models are:

- Discretionary Access Control (DAC): The owner of the object decides who can access it and with what permissions.
- Mandatory Access Control (MAC): The system assigns a security label to each object and subject, and enforces access based on the security policy.
- Role-Based Access Control (RBAC): The system grants access based on the role of the subject in the organization.
- Attribute-Based Access Control (ABAC): The system grants access based on the attributes of the subject, object, and environment.

Key concepts that make up access control are permissions, ownership of objects, inheritance of permissions, user rights, and object auditing:

- Permissions are the actions that a subject can perform on an object, such as read, write, execute, delete, etc.
- Ownership of objects is the ability to control the permissions and access of an object. The owner can transfer ownership to another subject.
- Inheritance of permissions is the process of passing down permissions from a parent object to a child object. For example, a folder can inherit permissions from its parent folder.
- User rights are the abilities that a subject has to perform system-level tasks, such as logging on, changing the system time, shutting down the system, etc.
- Object auditing is the process of recording and reviewing the access events of an object, such as who accessed it, when, and what actions were performed.

Access control is a feature of modern Zero Trust security philosophy, which applies techniques like explicit verification and least-privileged access to help secure sensitive information and prevent it from falling into the wrong hands.