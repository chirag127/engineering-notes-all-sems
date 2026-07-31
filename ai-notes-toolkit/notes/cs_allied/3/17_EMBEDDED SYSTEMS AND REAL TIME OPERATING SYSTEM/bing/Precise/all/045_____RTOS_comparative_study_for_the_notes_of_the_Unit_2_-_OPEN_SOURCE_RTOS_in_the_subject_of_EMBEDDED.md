# RTOS Comparative Study

Real-Time Operating Systems (RTOSs) are operating systems in which the time taken to process an input stimulus is less than the time lapsed until the next input stimulus of the same type .

When choosing an RTOS, the size of the RTOS should depend on your requirements. For example, the default configuration of LynxOS-178® is 1.4MB, which includes a POSIX RTOS with thread and process support, floating point, a filesystem, USB, networking, optional bash shell, and printf . On the other hand, Zephyr is a small open source RTOS with a minimum configuration of 8K, which includes threading, interrupts, and memory allocation. If Bluetooth communication is needed, the footprint doubles to 16K . This is perfect for tiny Internet of Things (IoT) devices that Zephyr is aimed at.

In general, an RTOS with lots of features can be expected to be about 1.5MB, whereas a minimal specialist RTOS like Zephyr would be around 16KB . Each RTOS is built as small as possible with the features it needs to satisfy its intended purpose.