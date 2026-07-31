#### Cohesion Measures in Software Design

Cohesion is a measure of how strongly related and focused the various responsibilities of a software module are . It shows the functional strength of a module of software. Modules with high cohesion tend to be preferable, because high cohesion is associated with several desirable traits of software including robustness, reliability, reusability, and understandability .

There are different types of cohesion, ranging from low to high, such as:

- Coincidental cohesion: The module has no logical relationship among its elements and performs multiple unrelated tasks.
- Logical cohesion: The module performs a series of related tasks, such as input, output, or error handling, based on some logical grouping.
- Temporal cohesion: The module performs a series of tasks that are related in time, such as initialization, termination, or event handling.
- Procedural cohesion: The module performs a series of tasks that follow a specific sequence of steps, such as a control flow or an algorithm.
- Communicational cohesion: The module performs a series of tasks that operate on the same data or input/output device, such as a file or a database.
- Sequential cohesion: The module performs a series of tasks in which the output of one task is the input of the next task, such as a data transformation or a pipeline.
- Functional cohesion: The module performs a single well-defined task or function, such as a mathematical calculation or a business logic.

One way to measure the cohesion of a module is to use the **Lack of Cohesion in Methods (LCOM)** metric, which calculates the number of pairs of methods in a class that do not share any attributes. A high LCOM value indicates low cohesion, while a low LCOM value indicates high cohesion. The formula for LCOM is:

```python
LCOM = P - Q
```

where P is the number of pairs of methods that do not share any attributes, and Q is the number of pairs of methods that share at least one attribute. If LCOM is negative, it is set to zero.

Another way to measure the cohesion of a module is to use the **Normalized Hamming Distance (NHD)** metric, which calculates the average dissimilarity between the methods of a class based on the attributes they access. A high NHD value indicates low cohesion, while a low NHD value indicates high cohesion. The formula for NHD is:

```python
NHD = 1 - (S / (M * A))
```

where S is the sum of the similarities between all pairs of methods, M is the number of methods, and A is the number of attributes. The similarity between two methods is the number of attributes they both access divided by the total number of attributes they access.

A third way to measure the cohesion of a module is to use the **Tight Class Cohesion (TCC)** metric, which calculates the ratio of the number of directly connected methods to the total number of possible connections in a class. A direct connection between two methods means that they access at least one common attribute. A high TCC value indicates high cohesion, while a low TCC value indicates low cohesion. The formula for TCC is:

```python
TCC = NDC / (M * (M - 1) / 2)
```

where NDC is the number of direct connections between methods, and M is the number of methods.