### Converting a normal Linux kernel to real time kernel

- A real time kernel is a kernel that provides deterministic response times to service events, such as interrupts, system calls, or signals.
- A real time kernel can be achieved by applying a patchset called PREEMPT_RT to the Linux kernel source code, which makes the kernel fully preemptible and reduces the latency of critical sections.
- The steps to convert a normal Linux kernel to a real time kernel are:

  - Download the Linux kernel source code from https://www.kernel.org/ and extract it to a directory.
  - Download the PREEMPT_RT patchset from https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/ and apply it to the kernel source code using the patch command.
  - Configure the kernel options using the make menuconfig command and enable the CONFIG_PREEMPT_RT option under the General setup menu.
  - Compile the kernel using the make command and install the kernel modules using the make modules_install command.
  - Install the kernel image using the make install command and update the bootloader configuration file.
  - Reboot the system and select the real time kernel from the bootloader menu.

- Alternatively, some Linux distributions provide pre-built real time kernels that can be installed from their repositories, such as:

  - Arch Linux: https://wiki.archlinux.org/title/Realtime_kernel_patchset
  - Ubuntu: https://ubuntu.com/engage/an-introduction-to-real-time-linux-part-i
  - CentOS: https://unix.stackexchange.com/questions/341933/install-a-real-time-kernel-on-centos 
  - Red Hat Enterprise Linux: https://www.redhat.com/sysadmin/real-time-kernel