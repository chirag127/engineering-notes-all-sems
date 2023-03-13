## Unit 3 - Scripting

Scripting is a technique of writing code that can automate tasks, control other applications, or enhance the functionality of a system. Scripting languages are usually interpreted, high-level, and dynamically typed. Some examples of scripting languages are Python, Perl, JavaScript, and Ruby.

A scripting language can interact with other components of a system, such as applications, libraries, databases, or web servers. A scripting architecture is a way of organizing these components and defining how they communicate with each other. A scripting architecture can have different layers, such as:

- Scripting engine: The component that executes the scripts and provides an interface to the underlying system.
- Scripting language: The syntax and semantics of the code that the scripting engine can understand and execute.
- Scripting library: A collection of predefined functions or classes that the scripting language can use to perform common tasks or access system resources.
- Scriptable object: An object that can be manipulated by the scripting language, such as a file, a window, a button, or a database record.
- Script: A piece of code that uses the scripting language to control or communicate with the scriptable objects.

The following diagram illustrates the basic architecture of a scripting system using ASCII art:

```
+-----------------+     +-----------------+
| Scriptable      |     | Scriptable      |
| Object          |     | Object          |
+-----------------+     +-----------------+
         ^                       ^
         |                       |
         |                       |
+-----------------+     +-----------------+
| Script          |     | Script          |
+-----------------+     +-----------------+
         ^                       ^
         |                       |
         |                       |
+-----------------+     +-----------------+
| Scripting       |     | Scripting       |
| Library         |     | Library         |
+-----------------+     +-----------------+
         ^                       ^
         |                       |
         |                       |
+-----------------+     +-----------------+
| Scripting       |     | Scripting       |
| Language        |     | Language        |
+-----------------+     +-----------------+
         ^                       ^
         |                       |
         |                       |
+-----------------+     +-----------------+
| Scripting       |     | Scripting       |
| Engine          |     | Engine          |
+-----------------+     +-----------------+
         ^                       ^
         |                       |
         |                       |
+-----------------+     +-----------------+
| System          |     | System          |
| Resources       |     | Resources       |
+-----------------+     +-----------------+
```