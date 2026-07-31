### System call interposition

- System call interposition (SCI) is a method for monitoring and regulating the behavior of applications by intercepting their calls to the operating system functions.
- SCI can be used to implement security policies that restrict the access of applications to system resources, such as files, network, devices, etc.
- SCI can be implemented in different ways, such as modifying the system call table, using ptrace, using LD_PRELOAD, or using a virtual machine monitor (VMM).
- SCI has some advantages, such as being able to enforce fine-grained policies, being transparent to applications, and being flexible and portable.
- SCI also has some challenges, such as being vulnerable to kernel attacks, being incomplete or inaccurate, being performance-intensive, and being difficult to write correct policies .
- SCI is a powerful technique for enhancing the security of computer systems, but it requires careful design and implementation to avoid pitfalls and limitations.