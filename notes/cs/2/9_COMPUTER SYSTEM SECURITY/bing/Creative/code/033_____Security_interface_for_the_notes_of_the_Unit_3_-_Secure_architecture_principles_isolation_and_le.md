# Security interface for the notes of the Unit 3 - Secure architecture principles isolation and leas in the subject of COMPUTER SYSTEM SECURITY

- Security interface is a set of user interface elements that provide security features such as authorization, access to digital certificates, and access to items in keychains.
- Secure architecture principles are the guidelines and best practices for designing and implementing secure systems that can resist attacks and ensure confidentiality, integrity, and availability of data and resources.
- Isolation and leas are two important secure architecture principles that aim to reduce the attack surface and limit the damage of potential breaches.
- Isolation means separating the components or processes of a system that have different security levels or functions, so that they cannot interfere with each other or access unauthorized data or resources.
- Leas means following the principle of least privilege, which states that every component or process of a system should have the minimum amount of access or permissions necessary to perform its function, and no more.
- Web security landscape is the set of threats, vulnerabilities, and countermeasures that affect the security of web applications and services, such as browsers, servers, databases, and APIs.

## Access Control Concepts

- Access control is a security technique that regulates who can view or use resources in a computing environment.
- Access control consists of three main components: subjects, objects, and rules.
- Subjects are the entities that request access to resources, such as users, processes, or devices.
- Objects are the resources that are protected by access control, such as files, directories, databases, or network connections.
- Rules are the policies or mechanisms that define how access is granted or denied, such as permissions, roles, or encryption.
- There are different types of access control models, such as discretionary access control (DAC), mandatory access control (MAC), role-based access control (RBAC), or attribute-based access control (ABAC).

## Unix and Windows Access Control Summary

- Unix and Windows are two popular operating systems that have different approaches to access control.
- Unix uses a DAC model, where the owner of an object can assign permissions to other subjects based on their user ID (UID) or group ID (GID). The permissions are read (r), write (w), and execute (x), and they can be applied to the owner (u), the group (g), or others (o). For example, the permission string `-rwxr-xr--` means that the owner can read, write, and execute the object, the group can read and execute, and others can only read.
- Windows uses a combination of DAC and RBAC models, where the owner of an object can assign permissions to other subjects based on their user account or group membership. The permissions are more granular than Unix, and they can be applied to files, folders, registry keys, printers, or services. For example, the permission list `Full Control, Modify, Read & Execute, Read, Write` means that the subject can perform all actions, modify the object, read and execute the object, read the object, or write to the object, respectively.

## Other Issues in Access Control

- Some of the challenges or limitations of access control are:
  - Scalability: as the number of subjects and objects increases, the complexity and overhead of managing access control also increases.
  - Inconsistency: different systems or platforms may have different access control models or implementations, which can lead to conflicts or errors.
  - Revocation: removing or updating access rights for subjects or objects may not be easy or immediate, especially in distributed or dynamic environments.
  - Covert channels: unauthorized subjects may exploit hidden or unintended ways of communicating or transferring data, such as timing or storage channels, to bypass access control.
  - Collusion: two or more subjects may cooperate to violate access control policies, such as by sharing credentials or information.

## Introduction to Browser Isolation

- Browser isolation is a security technique that isolates the browser from the local system or network, so that any malicious web content or activity cannot harm or compromise the device or data.
- Browser isolation can be achieved by different methods, such as:
  - Virtualization: running the browser in a virtual machine or container that is separate from the host system and can be easily reset or destroyed.
  - Remote browsing: running the browser on a remote server or cloud service that renders the web content and sends only the visual output to the client device.
  - Sandboxing: running the browser in a restricted environment that limits its access to system resources or network connections.
- Browser isolation can provide benefits such as:
  - Protection: preventing