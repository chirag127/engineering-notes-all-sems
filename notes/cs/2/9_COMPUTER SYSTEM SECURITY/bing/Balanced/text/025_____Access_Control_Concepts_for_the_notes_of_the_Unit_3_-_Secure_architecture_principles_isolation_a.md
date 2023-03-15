### Access Control Concepts

Access control is a security technique that regulates who or what can view or use resources in a computing environment. It is a fundamental concept in security that minimizes risk to the business or organization.

Access control relies heavily on two key principles—authentication and authorization:

- Authentication involves identifying a particular user based on their login credentials, such as usernames and passwords, biometric scans, PINs, or security tokens.
- Authorization refers to giving a user the appropriate level of access as determined by access control policies. These processes are typically automated.

Access control models have a subject and an object. The subject—the human user—is the one trying to gain access to the object—usually the software.

Some of the common access control models are:

- Discretionary Access Control (DAC): The owner of the object decides who can access it and with what permissions.
- Mandatory Access Control (MAC): The system assigns a security label to each object and user, and enforces access based on the comparison of these labels.
- Role-Based Access Control (RBAC): The system grants access based on the role of the user in the organization, rather than the individual identity.
- Attribute-Based Access Control (ABAC): The system grants access based on the attributes of the user, the object, and the environment, and evaluates them against a set of policies.

Some of the key concepts that make up access control are:

- Permissions: The actions that a user can perform on an object, such as read, write, execute, delete, etc.
- Ownership: The user or group that has the ultimate control over an object and can assign or revoke permissions to other users or groups.
- Inheritance: The mechanism by which permissions are propagated from a parent object to a child object, such as from a folder to a file.
- User rights: The actions that a user can perform on a system, such as logging on, changing the system time, shutting down the system, etc.
- Auditing: The process of recording and reviewing the events related to access control, such as who accessed what, when, and how.

Access control is a feature of modern Zero Trust security philosophy, which applies techniques like explicit verification and least-privileged access to help secure sensitive information and prevent it from falling into the wrong hands.