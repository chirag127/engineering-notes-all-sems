### Detour Unix user IDs, process IDs, and privileges

- In Unix-like operating systems, each user is assigned a unique user ID (UID) that identifies them to the system.
- Processes are also assigned unique process IDs (PIDs) that identify them to the system.
- The UID of the user who started a process is associated with that process, and determines the privileges that the process has.
- The superuser, or root user, has a UID of 0 and has the ability to perform any action on the system.
- Other users have UIDs greater than 0 and have more limited privileges.
- The setuid and setgid bits can be used to allow a process to run with the privileges of a different user or group.
- The effective UID (EUID) and effective GID (EGID) of a process determine the actual privileges of the process at any given time.
- The real UID (RUID) and real GID (RGID) of a process represent the user and group that started the process.
- The saved UID (SUID) and saved GID (SGID) of a process are used to restore the EUID and EGID when a process drops privileges temporarily.
- Access control mechanisms, such as file permissions and access control lists (ACLs), use the UID and GID of a process to determine whether it is allowed to access a particular resource.
