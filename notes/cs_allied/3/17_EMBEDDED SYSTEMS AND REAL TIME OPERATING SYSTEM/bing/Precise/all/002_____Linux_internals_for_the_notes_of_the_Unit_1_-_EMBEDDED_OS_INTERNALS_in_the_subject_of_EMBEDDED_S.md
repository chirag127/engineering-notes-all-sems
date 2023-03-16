# Linux Internals for Unit 1 - Embedded OS Internals

Embedded Linux is a type of Linux kernel that is specially designed for embedded devices. For example, the popular smartphone operating system, Android, is a type of embedded Linux customised for smartphones .

Operating systems based on the Linux kernel are used in embedded systems such as consumer electronics (e.g. set-top boxes, smart TVs and personal video recorders (PVRs)), in-vehicle infotainment (IVI), networking equipment (such as routers, switches, wireless access points (WAPs) or wireless routers), machine control, industrial automation, navigation equipment, spacecraft flight software, and medical instruments in general .

Embedded Linux is built on the same Linux kernel, available from kernel.org, as all Linux systems. But embedded systems have tight constraints that enterprise systems simply don’t have, ranging from higher reliability and security requirements to tighter resource availability and the need for engineering support that often lasts 10 years or more .

The file model in Linux is very simple. In operating systems before UNIX, the OS was expected to understand the structure of all kinds of files: typically files were organised as fixed (or variable) length records with one or more indices into them. By contrast, UNIX regular files are just a stream of bytes .

Linux supports a rich stack of networking protocols. Whether your embedded Linux project requires WiFi, mobile broadband (WWAN) or Ethernet connectivity, system network services like NetworkManager are supported on Linux .