# Unix and Windows Access Control Summary

## Unix Access Control

- Unix uses **access control lists (ACLs)** to specify the permissions of files and directories  .
- Each file or directory has an **owner**, a **group**, and an **other** category, each with a set of **mode bits** that indicate the read, write, and execute permissions   .
- The owner can change the permissions of the file or directory using the **chmod** command  .
- The owner can also change the group of the file or directory using the **chgrp** command  .
- The owner can also change the owner of the file or directory using the **chown** command, but only if the owner is the superuser (root) or has the appropriate privilege  .
- The mode bits can also include special bits such as the **setuid**, **setgid**, and **sticky** bits, which affect the behavior of the file or directory when executed or accessed  .
- Unix also supports **extended ACLs**, which allow more fine-grained control over the permissions of files and directories by specifying additional users and groups and their access rights  .
- Extended ACLs can be manipulated using the **getfacl** and **setfacl** commands  .

## Windows Access Control

- Windows uses **security identifiers (SIDs)** to represent users and groups (also called security principals).
- Each file or directory has an **owner** and a **discretionary access control list (DACL)**, which contains zero or more **access control entries (ACEs)** .
- An ACE consists of a **principal**, a **set of operations** (such as read, write, execute, etc.), and whether those operations are **allowed or denied** .
- The owner can grant or revoke permissions to principals by modifying the DACL using the **Properties** dialog or the **icacls** command.
- The DACL can also include **inheritance** and **propagation** flags, which determine how the permissions are applied to subdirectories and files.
- Windows also supports **mandatory access control (MAC)**, which enforces a system-wide policy based on the **integrity levels** of principals and objects.
- Integrity levels are assigned by the **Windows User Access Control (UAC)**, which restricts the privileges of users and applications to prevent unauthorized or malicious actions.
- Integrity levels can be viewed and changed using the **icacls** command with the **/setintegritylevel** option.