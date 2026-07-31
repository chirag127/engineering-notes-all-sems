### Detour Unix user IDs, process IDs, and privileges

- In Unix-like operating systems, every user is assigned a unique user ID (UID) that identifies them to the system.
- The UID is used to control access to system resources, such as files and directories, by determining the user's privileges.
- The UID is also used to determine the ownership of processes, which are instances of running programs.
- Every process has a unique process ID (PID) that identifies it to the system.
- Processes are associated with the UID of the user who started them, and inherit the privileges of that user.
- The superuser, or root user, has a UID of 0 and has the highest level of privileges on the system.
- The root user can perform any action on the system, including changing the ownership of files and directories, and modifying system settings.
- It is important to use the root user account sparingly and only for necessary system administration tasks, as it can pose a security risk if used improperly.
- Other users can be granted elevated privileges through the use of the `sudo` command, which allows them to temporarily perform actions as the root user.
- The use of `sudo` is logged and can be audited to ensure that it is being used appropriately.
