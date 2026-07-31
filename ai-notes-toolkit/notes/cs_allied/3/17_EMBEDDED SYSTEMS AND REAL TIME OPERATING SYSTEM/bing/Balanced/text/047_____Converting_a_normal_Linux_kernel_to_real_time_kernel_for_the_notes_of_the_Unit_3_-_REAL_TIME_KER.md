### Converting a normal Linux kernel to real time kernel

- A real time kernel is a kernel that guarantees a deterministic response time to events, such as interrupts, system calls, or signals.
- A normal Linux kernel is not fully preemptible, meaning that some critical sections of code cannot be interrupted by higher priority tasks, resulting in unpredictable latencies.
- To convert a normal Linux kernel to a real time kernel, one needs to apply a set of patches that modify the kernel code to make it fully preemptible and reduce the duration of critical sections.
- The most widely used set of patches for real time Linux is the PREEMPT_RT patchset, maintained by the Linux Foundation Real-Time Linux project.
- The steps to convert a normal Linux kernel to a real time kernel using the PREEMPT_RT patchset are:

  - Download the source code of the normal Linux kernel and the corresponding PREEMPT_RT patch from the official websites.
  - Apply the patch to the kernel source code using the patch command.
  - Configure the kernel options using the make menuconfig command. In the config options, set the ‘Fully Preemptible kernel (RT)’ option .
  - Build the kernel using the make command. This may take some time depending on the hardware and the number of cores available.
  - Install the kernel modules using the make modules_install command. This will copy the modules to the /lib/modules directory.
  - Install the kernel image using the make install command. This will copy the kernel image to the /boot directory and update the grub boot loader.
  - Reboot the system and select the real time kernel from the boot menu.

- To verify that the real time kernel is running, one can use the uname -a command and check for the rt suffix in the kernel version. Alternatively, one can use the cat /sys/kernel/realtime command and check for the value 1, indicating that the kernel is fully preemptible.