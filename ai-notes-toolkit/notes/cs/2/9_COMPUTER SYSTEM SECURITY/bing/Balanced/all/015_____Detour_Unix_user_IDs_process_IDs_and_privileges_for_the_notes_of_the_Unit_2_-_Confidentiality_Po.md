# Detour Unix user IDs process IDs and privileges

- Unix is a multi-user operating system that allows multiple users to access the same system and share its resources.
- Each user of a Unix system has a unique user ID (UID) that identifies them. The UID is an integer number that is stored in the /etc/passwd file along with other user information.
- The UID 0 is reserved for the superuser (root) who has full access and control over the system. Other users have limited privileges depending on their group memberships and file permissions.
- A user can belong to multiple groups, each with a group ID (GID). The GID is also an integer number that is stored in the /etc/group file along with other group information.
- A user's primary group is the one that is assigned to them when they log in. A user can also switch to other groups using the newgrp command or the setgid bit on a file or directory.
- A process is an instance of a running program that has a process ID (PID) that identifies it. The PID is also an integer number that is assigned by the kernel when the process is created.
- A process inherits the UID and GID of its parent process, unless it executes a setuid or setgid program, which changes its effective UID or GID to that of the program's owner or group.
- A process has three UIDs and three GIDs associated with it: real, effective, and saved. The real UID and GID are the ones that the process had when it was created. The effective UID and GID are the ones that are used to evaluate the process's privileges to perform a particular action. The saved UID and GID are used to store the original effective UID and GID when the process executes a setuid or setgid program, so that it can restore them later if needed.
- A process can change its effective UID or GID as long as the new ID is the same as either the real or the saved ID. This allows a process to drop or regain its privileges temporarily or permanently.
- A process can also change its real and saved UID or GID, but only if it has the superuser privilege or the new ID is the same as the effective ID. This allows a process to change its identity permanently and irreversibly.