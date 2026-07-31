### Converting a normal Linux kernel to real time kernel

- A real time kernel is a kernel that provides a bounded response time to an external event, regardless of the system load or complexity.
- A normal Linux kernel is not designed for real time applications, as it may incur unpredictable delays due to scheduling, interrupts, locking, memory management, and other factors.
- To convert a normal Linux kernel to a real time kernel, one needs to apply a patch that modifies the existing kernel code to increase predictability and reduce latencies.
- One such patch is the PREEMPT_RT patch, which aims to make the Linux kernel fully preemptible, meaning that any task can be interrupted at any time by a higher priority task.
- The PREEMPT_RT patch also introduces other features, such as priority inheritance, high resolution timers, threaded interrupts, and improved locking mechanisms, to enhance the real time performance of the kernel.
- To install a real time kernel on a Linux system, one needs to follow these steps:

  - Download the PREEMPT_RT patch that matches the kernel version and architecture of the system.
  - Apply the patch to the kernel source code using the patch command.
  - Configure the kernel options using the make menuconfig command, and enable the CONFIG_PREEMPT_RT option under the General setup menu.
  - Compile and install the patched kernel using the make and make install commands, and update the bootloader configuration.
  - Reboot the system and select the real time kernel from the GRUB menu.

- Alternatively, one can install a pre-built real time kernel from a repository, such as the -ml series kernel from CERN, or the kernel-rt package from Red Hat, using the package manager of the system, such as yum or apt.
- After installing a real time kernel, one can verify its functionality by using tools such as rt-tests, which provides a set of tests to measure the latency and jitter of the kernel, or tuned, which provides a set of profiles to optimize the system settings for real time applications.