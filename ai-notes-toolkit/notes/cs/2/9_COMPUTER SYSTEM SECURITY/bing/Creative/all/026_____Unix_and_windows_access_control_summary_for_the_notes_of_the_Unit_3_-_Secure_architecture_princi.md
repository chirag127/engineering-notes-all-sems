# Unix and Windows Access Control Summary

## Unix Access Control

- Unix uses **access control lists (ACLs)** to specify the permissions of files and directories  .
- Each file or directory has an **owner**, a **group**, and an **other** category of users  .
- Each category has three **mode bits** that indicate the **read**, **write**, and **execute** permissions for that category   .
- The mode bits are represented by three octal digits, such as 755, which means the owner has read, write, and execute permissions (7), the group has read and execute permissions (5), and the other users have read and execute permissions (5)  .
- The mode bits can also be represented by a string of nine characters, such as rwxr-xr-x, which means the same as 755  .
- The mode bits can be changed by the owner or the superuser (root) using the **chmod** command  .
- Unix also supports **setuid**, **setgid**, and **sticky** bits, which modify the behavior of the executable files and directories  .
- The setuid bit allows a file to be executed with the permissions of the owner, regardless of who executes it  .
- The setgid bit allows a file to be executed with the permissions of the group, regardless of who executes it  .
- The sticky bit prevents users from deleting or renaming files in a directory, unless they own the file or the directory  .
- The setuid, setgid, and sticky bits are represented by a fourth octal digit or a character in the mode string, such as 4755 or rwsr-xr-x, which means the file has the setuid bit set  .

## Windows Access Control

- Windows uses **security identifiers (SIDs)** to represent users and groups (also called security principals).
- Each security principal has a unique SID that is assigned by the operating system or the domain controller.
- Each security principal can be assigned **rights** and **permissions** that inform the operating system what each user and group can do.
- Rights are system-wide privileges that allow security principals to perform certain actions, such as logging on, changing the system time, or shutting down the system.
- Permissions are resource-specific privileges that allow security principals to access or modify files, folders, registry keys, printers, or other objects.
- Each resource has an **owner** who grants permissions to security principals.
- Each resource also has a **discretionary access control list (DACL)** that contains **access control entries (ACEs)** .
- An ACE consists of a security principal, a set of operations (such as read, write, execute, etc.), and whether those operations are allowed or denied .
- The DACL is evaluated from top to bottom, and the first matching ACE determines the access decision.
- If there is no matching ACE, the access is denied by default.
- Windows also supports **inheritance** and **auditing** of permissions.
- Inheritance allows permissions to be propagated from a parent object to a child object, such as from a folder to a file.
- Auditing allows the operating system to record the access attempts of security principals to a resource in the **security log**.
- Windows also has a **mandatory access control (MAC)** mechanism that enforces the **integrity level** of processes and objects.
- The integrity level is a label that indicates the trustworthiness of a process or an object, such as low, medium, high, or system.
- The integrity level is enforced by the **Windows User Access Control (UAC)**, which prevents processes or objects with lower integrity levels from accessing