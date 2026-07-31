Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of process based real time kernel basics:

### Process based real time kernel basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible, to meet the timing constraints of real-time applications.
- A real-time kernel can run on different CPU architectures, and usually requires a small portion of code written in assembly language to adapt to the specific hardware.
- A real-time kernel can provide features such as multitasking, task synchronization, task communication, task scheduling, interrupt management, memory management, and time management.
- A real-time kernel can be classified into two types: hard real-time and soft real-time. A hard real-time kernel guarantees that all tasks will meet their deadlines, while a soft real-time kernel allows some tasks to miss their deadlines occasionally.
- A real-time kernel can also be classified into two models: kernel model and user space model. In the kernel model, the real-time tasks run in the kernel space and use the real-time API and the limited kernel API. In the user space model, the real-time tasks run in the user space and use the real-time API and the whole Linux API. However, the user space model cannot achieve hard real-time scheduling.
- A real-time kernel can be identified by the rt keyword in the kernel version, which can be obtained by executing the uname -r command on the terminal. For example, the following output indicates a real-time kernel:

```bash
$ uname -r
4.18.0-147.8.1.rt24.95.el8_1.x86_64
```

- A real-time kernel can be installed and configured on different Linux distributions, such as Red Hat Enterprise Linux, Ubuntu, Debian, and Fedora. The installation and configuration steps may vary depending on the distribution and the hardware.