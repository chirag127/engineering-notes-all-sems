### Kernel Module Programming

- Kernel module programming is a way of extending the functionality of the kernel without modifying the kernel source code or recompiling the kernel.
- Kernel modules are object files that contain code that can be loaded into or unloaded from the kernel at runtime.
- Kernel modules are useful for implementing device drivers, file systems, network protocols, encryption algorithms, and other features that are not essential for the core kernel.
- Kernel modules must have at least two functions: a start (initialization) function called `init_module()` and an end (cleanup) function called `cleanup_module()`.
- Kernel modules can communicate with the kernel and other modules using symbols, parameters, and sysfs.
- Kernel modules can be compiled using the `make` command and the kernel headers.
- Kernel modules can be inserted into the kernel using the `insmod` command and removed from the kernel using the `rmmod` command.
- Kernel modules can be listed using the `lsmod` command and their information can be displayed using the `modinfo` command.
- Kernel modules can be debugged using tools such as `printk`, `kdb`, `kgdb`, and `kprobes`.

: https://www.engineersgarage.com/kernel-programming/
: https://linux-kernel-labs.github.io/refs/heads/master/labs/kernel_modules.html
: https://www.geeksforgeeks.org/linux-kernel-module-programming-hello-world-program/