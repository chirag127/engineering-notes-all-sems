### Detour: Unix user IDs, process IDs and privileges

- Every user in Unix-like operating systems is identified by a unique integer number, called a user ID (UID) .
- Every process in Unix-like operating systems is identified by a unique integer number, called a process ID (PID) .
- Every process has three user IDs associated with it: the real user ID (RUID), the effective user ID (EUID), and the saved user ID (SUID)  .
- The RUID is the UID of the user who created or launched the process .
- The EUID is the UID that determines the privileges of the process when accessing shared resources such as message queues, shared memory, and semaphores .
- The SUID is the UID of the owner of the executable file that started the process, if the file has the setuid bit on .
- The setuid bit is a special permission bit that allows a process to run with the privileges of the file owner, regardless of the RUID .
- A process can change its user IDs by using system calls such as setuid, seteuid, or setreuid .
- A process can only set its EUID or SUID to its RUID or the file owner's UID, unless it has superuser privileges (UID=0)  .
- A process can use the setuid system call to drop its superuser privileges permanently by setting its RUID, EUID, and SUID to a non-zero UID .
- A process can use the seteuid system call to drop its superuser privileges temporarily by setting its EUID to a non-zero UID, and then regain them by setting its EUID back to 0 .
- A process can use the setreuid system call to swap its RUID and EUID, which allows it to switch between its original and elevated privileges .
- The purpose of these mechanisms is to allow a process to perform privileged operations only when necessary, and to reduce the risk of compromising the system security .