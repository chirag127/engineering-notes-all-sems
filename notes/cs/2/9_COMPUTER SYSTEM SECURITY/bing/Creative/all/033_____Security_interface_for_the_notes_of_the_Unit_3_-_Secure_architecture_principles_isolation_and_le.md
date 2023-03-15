# Security interface for the notes of the Unit 3 - Secure architecture principles isolation and leas in the subject of COMPUTER SYSTEM SECURITY

- Security interface is a set of user interface elements that provide security features such as authorization, access to digital certificates, and access to items in keychains.
- Secure architecture principles are the guidelines and best practices for designing and implementing secure systems that can resist attacks and ensure confidentiality, integrity, and availability of data and resources.
- Isolation and leas are two important secure architecture principles that aim to reduce the attack surface and limit the damage of potential breaches.
- Isolation means separating the components or processes of a system that have different security levels or requirements, so that they cannot interfere with each other or access unauthorized data or resources.
- Leas means following the principle of least privilege, which states that every component or process of a system should have the minimum amount of access or permissions necessary to perform its function, and nothing more.
- Web security landscape is the overview of the threats and challenges that web applications and users face, such as cross-site scripting, cross-site request forgery, session hijacking, phishing, malware, etc.

## Access Control Concepts
- Access control is a security technique that regulates who can view or use resources in a computing environment.
- Access control consists of three main components: subjects, objects, and rules.
- Subjects are the entities that request access to resources, such as users, processes, or devices.
- Objects are the resources that are protected by access control, such as files, databases, networks, or devices.
- Rules are the policies or mechanisms that define how subjects can access objects, such as permissions, roles, or encryption.
- There are different types of access control models, such as discretionary access control (DAC), mandatory access control (MAC), role-based access control (RBAC), or attribute-based access control (ABAC).

## Unix and Windows Access Control Summary
- Unix and Windows are two popular operating systems that have different approaches to access control.
- Unix uses a DAC model, where the owner of an object can grant or revoke permissions to other subjects. Unix permissions are based on three categories: user, group, and others. Each category has three types of permissions: read, write, and execute. Unix permissions are represented by a combination of letters (rwx) or numbers (0-7).
- Windows uses a combination of DAC and RBAC models, where the owner of an object can grant or revoke permissions to other subjects or roles. Windows permissions are based on access control lists (ACLs), which are lists of access control entries (ACEs) that specify the subject, the object, and the permissions. Windows permissions are more granular and complex than Unix permissions, and can include inheritance, auditing, and ownership.

## Other Issues in Access Control
- Some of the issues or challenges in access control are:
  - Scalability: how to manage access control for large and dynamic systems with many subjects and objects.
  - Usability: how to balance security and convenience for users and administrators.
  - Accountability: how to monitor and audit access control activities and enforce compliance.
  - Availability: how to ensure access control does not compromise the performance or reliability of the system.
  - Interoperability: how to integrate access control across different platforms, domains, or applications.

## Introduction to Browser Isolation
- Browser isolation is a security technique that isolates the web browser from the local system, so that any malicious or untrusted web content cannot harm the system or access sensitive data.
- Browser isolation can be achieved by different methods, such as:
  - Virtualization: running the browser in a virtual machine or a container that is separate from the host system.
  - Remote browsing: running the browser on a remote server and streaming the content to the local system via a secure protocol.
  - Sandboxing: running the browser in a restricted environment that limits its access to system resources and enforces security policies.
- Browser isolation can provide benefits such as:
  - Protection from web-based attacks, such as malware, phishing, or cross-site scripting.
  - Prevention of data leakage, such as cookies, passwords, or personal information.
  - Reduction of the attack surface, such as browser vulnerabilities, plugins, or extensions.