### Access Control Concepts

Access control is a security technique that regulates who or what can view or use resources in a computing environment. It is a fundamental concept in security that minimizes risk to the business or organization. There are two types of access control: physical and logical.

- Physical access control limits access to buildings, rooms, or physical assets.
- Logical access control limits access to digital assets, such as networks, websites, and cloud resources.

Access control relies heavily on two key principles—authentication and authorization:

- Authentication involves identifying a particular user based on their login credentials, such as usernames and passwords, biometric scans, PINs, or security tokens.
- Authorization refers to giving a user the appropriate level of access as determined by access control policies. These processes are typically automated.

Access control models have a subject and an object. The subject—the human user—is the one trying to gain access to the object—usually the software. Access control policies define the rules and conditions for granting or denying access to the object.

Some common access control models are:

- Discretionary Access Control (DAC): The owner of the object decides who can access it and with what permissions. This model is flexible but prone to human error and insider threats.
- Mandatory Access Control (MAC): The system assigns a security label to each object and subject based on their classification level. The system enforces the access control policy based on the security labels. This model is rigid but secure.
- Role-Based Access Control (RBAC): The system assigns roles to subjects based on their job functions and grants access to objects based on the roles. This model is scalable and easy to manage.
- Attribute-Based Access Control (ABAC): The system evaluates attributes of the subject, object, and environment to determine the access decision. This model is dynamic and granular.

Key concepts that make up access control are permissions, ownership of objects, inheritance of permissions, user rights, and object auditing:

- Permissions are the actions that a subject can perform on an object, such as read, write, execute, or delete.
- Ownership of objects is the ability to control the access to an object. The owner of an object can assign or change permissions on the object.
- Inheritance of permissions is the process of passing down permissions from a parent object to a child object. For example, a folder can inherit permissions from its parent folder.
- User rights are the abilities that a subject has to perform system-level tasks, such as logging on, changing the system time, or shutting down the system.
- Object auditing is the process of recording and reviewing the access events on an object, such as who accessed it, when, and what actions they performed.

Access control is a feature of modern Zero Trust security philosophy, which applies techniques like explicit verification and least-privileged access to help secure sensitive information and prevent it from falling into the wrong hands. Access control systems should be regularly reviewed and updated to ensure they are effective and compliant with the security standards and regulations.