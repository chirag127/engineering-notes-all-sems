### Detour Unix user IDs process IDs and privileges

- Each user of a Unix account has a unique UID. UID 0 means the Superuser (system admin) .
- A user account belongs to multiple groups .
- Subjects are processes associated with UID/GID pairs .
- Objects are files .
- Every user in UNIX like the operating system is identified by a different integer number, this unique number is called a user ID .
- Each Linux process has 3 UIDs associated to it :
    - Real UID: The UID of the process that created THIS process .
    - Effective UID: This is used to evaluate privileges of the process to perform a particular action .
    - Saved UID: For the binary image file with a setuid bit on it .
- A process that executes a set-uid program can drop its privilege .
- The effective user or group ID for a process may be changed as long as the new ID is the same as either the real or the saved ID .
- Permanently dropping privileges involves ensuring that the effective, real, and saved IDs are all the same value .