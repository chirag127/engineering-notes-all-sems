# Converting a normal Linux kernel to real time kernel

- A real time kernel is a kernel that can guarantee a deterministic response time to events, such as interrupts, system calls, or user inputs.
- A normal Linux kernel is not fully preemptible, meaning that some critical sections of code cannot be interrupted by higher priority tasks, resulting in unpredictable latencies.
- To convert a normal Linux kernel to a real time kernel, one needs to apply a set of patches that modify the kernel code to make it fully preemptible and reduce the duration of critical sections.
- The most widely used set of patches for real time Linux is the PREEMPT_RT patchset, maintained by the Linux Foundation Real-Time Linux project.
- The steps to apply the PREEMPT_RT patchset to a normal Linux kernel are as follows:

  - Download the source code of the normal Linux kernel and the corresponding PREEMPT_RT patch from https://www.kernel.org/ and https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/, respectively.
  - Extract the kernel source code and apply the patch using the patch command, e.g., `patch -p1 < patch-5.15.6-rt21.patch`.
  - Configure the kernel options using the `make menuconfig` command. In the config options, set the `Fully Preemptible kernel (RT)` option.
  - Build the kernel using the `make` command and install the modules using the `make modules_install` command.
  - Update the grub boot loader and reboot into the newly installed real-time patched kernel.

- Alternatively, one can install a pre-built real time kernel from a repository, such as the CERN-RT repo for CentOS or the Ubuntu-RT repo for Ubuntu.
- To verify that the real time kernel is running, one can use the `uname -a` command and check for the `PREEMPT_RT` string in the output.