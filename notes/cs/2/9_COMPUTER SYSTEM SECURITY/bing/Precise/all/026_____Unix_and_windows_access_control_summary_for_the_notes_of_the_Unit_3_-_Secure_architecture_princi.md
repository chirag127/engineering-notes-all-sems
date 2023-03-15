# Unix and Windows Access Control Summary

## Unit 3 - Secure Architecture Principles: Isolation and Least Privilege

### Unix Access Control
- Unix uses a discretionary access control (DAC) model.
- The owner of a file or directory has the ability to set permissions for themselves, their group, and others.
- Permissions include read, write, and execute.
- The `chmod` command is used to change permissions.
- The `chown` command is used to change the owner of a file or directory.
- The `chgrp` command is used to change the group of a file or directory.

### Windows Access Control
- Windows uses both discretionary access control (DAC) and mandatory access control (MAC) models.
- The owner of a file or directory has the ability to set permissions for themselves, their group, and others.
- Permissions include read, write, execute, and full control.
- The `icacls` command is used to change permissions.
- The `takeown` command is used to take ownership of a file or directory.
- The `cacls` command is used to display or modify access control lists (ACLs).

### Isolation and Least Privilege
- Isolation and least privilege are important principles in secure architecture.
- Isolation involves separating components or systems to limit the potential impact of a security breach.
- Least privilege involves granting users and systems the minimum level of access necessary to perform their tasks.
- Both principles help to reduce the attack surface and limit the potential damage of a security breach.
