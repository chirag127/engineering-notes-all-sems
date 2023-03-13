Cohesion is a measure of how strongly related and focused the various responsibilities of a software module are. It shows the functional strength of a module of software. Cohesion is an ordinal type of measurement and is usually described as “high cohesion” or “low cohesion”. Modules with high cohesion tend to be preferable, because high cohesion is associated with several desirable traits of software including robustness, reliability, reusability, and understandability. In contrast, low cohesion is associated with undesirable traits such as being difficult to maintain, test, reuse, or even understand.

There are different types of cohesion, such as functional cohesion, sequential cohesion, communicational cohesion, procedural cohesion, temporal cohesion, logical cohesion, and coincidental cohesion. These types can be arranged in a hierarchy from the most desirable (functional cohesion) to the least desirable (coincidental cohesion).

#### Cohesion Measures in Software Design

The following diagram illustrates the different types of cohesion and their relative desirability using a scale from 1 (low) to 7 (high):

```
+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| Functional     | Sequential     | Communicational| Procedural     | Temporal       | Logical        | Coincidental   |
| Cohesion       | Cohesion       | Cohesion       | Cohesion       | Cohesion       | Cohesion       | Cohesion       |
+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
|                |                |                |                |                |                |                |
|                |                |                |                |                |                |                |
|                |                |                |                |                |                |                |
|                |                |                |                |                |                |                |
|                |                |                |                |                |                |                |
|                |                |                |                |                |                |                |
|                |                |                |                |                |                |                |
|                |                |                |                |                |                |                |
|                |                |                |                |                |                |                |
|                |                |                |                |                |                |                |
+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
| 7              | 6              | 5              | 4              | 3              | 2              | 1              |
+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
```

A brief description of each type of cohesion is given below:

- Functional cohesion: The module performs a single specific task or function. For example, a module that calculates the area of a circle.
- Sequential cohesion: The module performs a series of related tasks or functions that must be executed in a specific order. For example, a module that reads data from a file, processes it, and writes the output to another file.
- Communicational cohesion: The module performs a series of related tasks or functions that operate on the same data or input/output device. For example, a module that performs different calculations on the same set of data.
- Procedural cohesion: The module performs a series of related tasks or functions that are grouped together because they follow a certain sequence of steps or a common procedure. For example, a module that validates user input, performs some calculations, and displays the results.
- Temporal cohesion: The module performs a series of related tasks or functions that are grouped together because they are executed at the same time or within the same time span. For example, a module that initializes a system, loads configuration files, and sets up connections.
- Logical cohesion: The module performs a series of related tasks or functions that are grouped together because they share some logical category or condition. For example, a module that handles different types of errors or exceptions.
- Coincidental cohesion: The module performs a series of unrelated tasks or functions that are grouped together arbitrarily or by coincidence. For example, a module that performs some calculations, prints a report, and sends an email.