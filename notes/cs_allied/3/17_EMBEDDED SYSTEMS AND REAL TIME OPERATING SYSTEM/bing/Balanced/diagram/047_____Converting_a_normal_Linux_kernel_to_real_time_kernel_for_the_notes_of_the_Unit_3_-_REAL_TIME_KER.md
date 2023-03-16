### Converting a normal Linux kernel to real time kernel

- A real time kernel is a kernel that can guarantee a deterministic response time to events, such as interrupts, system calls, or user inputs.
- A normal Linux kernel is not fully preemptible, meaning that some critical sections of code cannot be interrupted by higher priority tasks, which can cause latency and jitter in real time applications.
- To convert a normal Linux kernel to a real time kernel, one needs to apply a patchset called RT-Preempt, which makes the kernel fully preemptible by replacing spinlocks with rtmutexes, adding priority inheritance to avoid priority inversion, and reducing the amount of non-preemptible code.
- The RT-Preempt patchset is maintained by the Linux Foundation Real-Time Linux project and is available for download from https://wiki.linuxfoundation.org/realtime/documentation/howto/applications/preemptrt_setup.
- Depending on the Linux distribution, there may be different ways to install a real time kernel. Some distributions may provide pre-built packages or repositories for real time kernels, while others may require compiling the kernel from source with the RT-Preempt patch applied.
- For example, to install a real time kernel on CentOS, one can use the -ml series kernel from CERN, which is based on the RT-Preempt patchset. To do so, one needs to install the CERN-RT repo and then install the RT kernel group:

```
wget http://linuxsoft.cern.ch/cern/centos/7/rt/CentOS-RT.repo
yum groupinstall RT
```

- After installing the real time kernel, one needs to reboot the system and select the real time kernel from the GRUB menu. To verify that the real time kernel is running, one can check the output of `uname -a` and look for the `-rt` suffix in the kernel version.
- To optimize the performance of the real time kernel, one may need to adjust some kernel parameters, such as the scheduler, the CPU frequency governor, the memory management, and the interrupt handling. For more details, see https://wiki.linuxfoundation.org/realtime/documentation/howto/applications/application_base_configuration.