### Rootkits

- A rootkit is a **collection of software tools** that enable an **unauthorized user** to gain **control** of a computer system without being **detected**  .
- The term rootkit comes from the Unix and Linux operating systems, where **root** refers to the **administrative account** on the system, and **kit** refers to the **software** that implements the tool.
- A rootkit can **open a door** for other malware, such as viruses and keyloggers, to **infect** the system. It can also **hide** its presence and the presence of other software from the user and the security software .
- Rootkits can be classified into two main types: **user-mode rootkits** and **kernel-mode rootkits**.
  - User-mode rootkits operate in the **user space** of the system, where applications and processes run. They can **modify** or **replace** system files, libraries, drivers, or processes to **intercept** system calls or **alter** system behavior.
  - Kernel-mode rootkits operate in the **kernel space** of the system, where the core of the operating system runs. They can **load** as kernel modules or **patch** the kernel code to **manipulate** the system at a low level.
- Rootkits can be **installed** on a system through various methods, such as **exploiting** a vulnerability, **tricking** the user into running a malicious file, or **bundling** with other software.
- Rootkits can be **detected** by using specialized tools that **scan** the system for anomalies, **compare** the system files with trusted sources, or **monitor** the system activity for suspicious behavior.
- Rootkits can be **removed** by using anti-rootkit software that can **identify** and **clean** the infected files, or by **reinstalling** the operating system from a trusted source.