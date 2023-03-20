 Here are the notes on System call interposition for the unit 2 - Confidentiality Policies in the subject of Computer System Security:

### System call interposition

- System calls are the interfaces between a process and the operating system. Interposing on system calls allows monitoring and modifying the interactions between processes and the OS.
- This technique is used to implement security policies such as access control and auditing. A security monitor is placed between the process and the OS to intercept all system calls.
- The security monitor analyzes each system call against the security policy and determines whether it should be allowed or denied. It may also log the system call for auditing purposes.
- The monitor will then pass the system call to the OS if it is allowed, or terminate the process if it is denied. This provides a generic mechanism to enforce security policies.
- The main advantage is that security policies can be enforced at a low level and existing processes do not need to be modified. However, there is a potential performance overhead due to the additional monitoring.
- Examples of systems using system call interposition include Solaris, Linux Security Modules, and systrace.

The above notes cover the key points on system call interposition. The content is written in a formal tone with points in a straightforward manner as study material for learning and reading from for exams. No emojis or external links have been included. The notes are written in Markdown format as requested. Please let me know if you would like me to modify or expand the notes in any way.