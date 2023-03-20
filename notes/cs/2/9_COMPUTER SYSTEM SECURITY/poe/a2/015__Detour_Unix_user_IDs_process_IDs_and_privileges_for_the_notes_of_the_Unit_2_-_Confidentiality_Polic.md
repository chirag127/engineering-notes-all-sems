 Here is the content in markdown format without any emojis or external links:

### Detour: Unix user IDs, process IDs, and privileges

- Unix uses user IDs (UIDs) to identify users and control access to resources.
- Each process running on Unix has a process ID (PID) to uniquely identify it.
- Unix uses privileges to control what kinds of access a process has to system resources.
- The root user has full privileges. Most user processes have restricted privileges for security.
- Privileges can be changed (raised or lowered) during process execution with the setuid and setgid system calls, allowing a process limited access to resources beyond a user's normal privileges. This is commonly used to allow users to run certain programs with elevated privileges without giving them full root access.
- These features can introduce security vulnerabilities if misused or exploited by malware. Proper access controls and least privilege principles should be applied.

The content follows the requested points format and is written formally like study material without any feelings or friendliness. The markdown format is used and there are no emojis or external links included. Please let me know if you would like me to modify or expand the content in any way.