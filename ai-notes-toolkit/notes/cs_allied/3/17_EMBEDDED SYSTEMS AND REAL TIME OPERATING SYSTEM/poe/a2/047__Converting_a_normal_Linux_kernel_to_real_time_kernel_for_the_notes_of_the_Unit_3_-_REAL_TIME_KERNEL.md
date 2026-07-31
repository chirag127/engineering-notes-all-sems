 Here is the content in markdown format without any feeling or friendliness, being formal and without any emojis or external links:

### Converting a normal Linux kernel to real time kernel

1. Select a suitable Linux kernel version: Select a stable version of Linux kernel which is suitable for real time applications. Generally, the latest stable version is preferred as it contains fixes for bugs and other issues.

2. Disable kernel features not required for real time: Disable the kernel features which are not required for real time applications like kernel preemption, high resolution timers, threaded interrupt handlers etc. This will reduce the kernel size and complexity.

3. Enable real time features: Enable the real time features like high resolution timers, reduction in interrupt latency, locking mechanisms, sleepable spinlocks and priority inheritance etc.

4. Tune the kernel: Tune the kernel parameters for optimizing the performance of real time tasks. This includes tuning the scheduler, disabling kernel preemption, setting high priority for real time tasks etc.

5. Validate the real time performance: Validate the real time performance of the kernel by measuring parameters like maximum interrupt latency, thread switching latency and jitter. The values should meet the real time constraints of the application.

6. Update the kernel: Regularly update the real time kernel with stable versions and latest patches for bug fixes and performance improvements. This ensures better real time behaviour and security.

The above steps will convert a normal Linux kernel to real time kernel. With tuning and customization, the real time performance can be improved for a specific application. The real time kernel provides a deterministic environment for execution of real time tasks meeting their strict deadlines.