#### Function Oriented Design in Software Design

Function Oriented Design is a software design methodology that focuses on the decomposition of the system into a set of interacting functions. This approach is based on the idea that software should be designed by identifying the functions that the system needs to perform and then organizing these functions into a hierarchy of control.

Here is an example of a simple program that uses Function Oriented Design:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    else:
        return a / b

def main():
    a = 10
    b = 5
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))

if __name__ == "__main__":
    main()
```

In this example, the main function controls the flow of the program and calls the other functions to perform the necessary calculations. Each function performs a specific task and can be reused in other parts of the program or in other programs. This modular design makes it easier to understand, maintain, and modify the code.