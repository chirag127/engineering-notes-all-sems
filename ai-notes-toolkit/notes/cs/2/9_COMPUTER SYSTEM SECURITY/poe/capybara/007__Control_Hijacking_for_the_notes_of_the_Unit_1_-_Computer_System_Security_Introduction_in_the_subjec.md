### Control Hijacking

Control hijacking, also known as code injection, is a type of computer security attack that involves taking control of a computer system by exploiting a vulnerability in its code. This type of attack is commonly used to gain access to sensitive information, such as passwords or financial data, or to take control of the system for malicious purposes.

Here are some important points to keep in mind when learning about control hijacking:

- Control hijacking attacks typically involve exploiting a buffer overflow vulnerability in a program's code. This vulnerability occurs when a program tries to write more data to a buffer than it can hold, causing the excess data to overwrite adjacent memory locations.
- By carefully crafting the data that overwrites the adjacent memory locations, an attacker can modify the program's execution flow to take control of the system.
- There are several techniques that attackers can use to achieve control hijacking, including stack-based attacks, heap-based attacks, and return-oriented programming attacks.
- Stack-based attacks involve overwriting the return address of a function in the program's call stack with the address of the attacker's code. When the function returns, the program jumps to the attacker's code instead of the expected location.
- Heap-based attacks involve exploiting vulnerabilities in the program's heap memory, which is used for dynamic memory allocation. By manipulating the heap, an attacker can modify the program's execution flow.
- Return-oriented programming attacks involve chaining together small pieces of code, known as gadgets, that already exist in the program's memory. By jumping to these gadgets in a specific order, an attacker can execute arbitrary code without injecting any new code into the program.
- There are several defensive measures that can be taken to protect against control hijacking attacks, including using stack canaries, data execution prevention, address space layout randomization, and control flow integrity. These techniques make it more difficult for attackers to exploit vulnerabilities in the program's code.

By understanding the techniques used in control hijacking attacks and the defensive measures that can be taken to prevent them, computer security professionals can better protect computer systems from these types of attacks.