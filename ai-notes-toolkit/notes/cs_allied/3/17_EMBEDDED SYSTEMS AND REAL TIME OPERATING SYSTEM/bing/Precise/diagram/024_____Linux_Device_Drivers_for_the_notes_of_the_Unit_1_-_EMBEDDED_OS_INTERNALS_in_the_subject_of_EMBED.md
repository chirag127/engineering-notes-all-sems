### Linux Device Drivers

Linux device drivers are the mechanism through which the underlying hardware is exposed to the rest of the system. As a developer of embedded systems, you need to know how these device drivers fit into the overall architecture and how to access them from user space programs.

There are two ways of Linux device driver programming:
1. Compile the driver along with the kernel, which is monolithic in Linux.
2. Implement the driver as a kernel module, in which case you won’t need to recompile the kernel.

Linux device drivers fall into three broad categories: character, block, and network. Of the three, the character driver interface is the most flexible and therefore, the most common. Linux drivers fit into a framework known as the driver model, which is exposed through sysfs.

In essence, your Linux kernel driver needs to create a device file and you need to map the operations done on this device file (open, read, write, close, ioctl) to the device hardware-specific functions in your driver. Linux builds upon that to create specific driver subsystems.