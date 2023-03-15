#### Cohesion Measures in Software Design

Cohesion is a measure of how strongly related and focused the various responsibilities of a software module are . It shows the functional strength of a module of software. Modules with high cohesion tend to be preferable, because high cohesion is associated with several desirable traits of software including robustness, reliability, reusability, and understandability . In contrast, low cohesion is associated with complexity, confusion, and inefficiency.

There are different types of cohesion that can be used to measure the quality of a software module, such as:

- **Functional cohesion**: The highest and best type of cohesion, where a module performs a single and well-defined function .
- **Sequential cohesion**: A module performs a series of related actions, where the output of one action is the input of another .
- **Communicational cohesion**: A module performs a set of actions that are related by operating on the same data .
- **Procedural cohesion**: A module performs a set of actions that are related by the order of execution, but not by the data .
- **Temporal cohesion**: A module performs a set of actions that are related by time, such as initialization or cleanup .
- **Logical cohesion**: A module performs a set of actions that are logically related, but not by data or time, such as a menu or a switch statement .
- **Coincidental cohesion**: The lowest and worst type of cohesion, where a module performs a set of unrelated actions .

To measure the cohesion of a software module, one can use various metrics, such as:

- **Lack of cohesion in methods (LCOM)**: A metric that measures the degree to which the methods of a class are related to each other. It is calculated by subtracting the number of method pairs that share at least one attribute from the number of method pairs that do not share any attribute, and then dividing by the total number of method pairs. A lower LCOM value indicates higher cohesion.
- **Tight class cohesion (TCC)**: A metric that measures the ratio of the number of method pairs of a class that access in common at least one attribute to the total number of possible method pairs of the class. A higher TCC value indicates higher cohesion.
- **Loose class cohesion (LCC)**: A metric that measures the ratio of the number of directly or indirectly connected method pairs of a class to the total number of possible method pairs of the class. A higher LCC value indicates higher cohesion.

Here is an example of a Python class that has low cohesion and a high LCOM value:

```python
class LowCohesion:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

    def print_salary(self):
        print(self.salary)

    def calculate_tax(self):
        return self.salary * 0.1

    def greet(self):
        print(f"Hello, {self.name}!")

    def is_adult(self):
        return self.age >= 18
```

The LCOM value for this class is:

```python
LCOM = (6 - 3) / 6 = 0.5
```

This class has low cohesion because it performs a set of unrelated actions, such as printing, calculating, and greeting. It also has a high LCOM value, which indicates low cohesion.

Here is an example of a Python class that has high cohesion and a low LCOM value:

```python
class HighCohesion:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def greet(self):
        print(f"Hello, {self.name}!")

    def is_adult(self):
        return self.age >= 18
```

The LCOM value for this class is:

```python
LCOM = (3 - 3) / 3 = 0
```

This class has