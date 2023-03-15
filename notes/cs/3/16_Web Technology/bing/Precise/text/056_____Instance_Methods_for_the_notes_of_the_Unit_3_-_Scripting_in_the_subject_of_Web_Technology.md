### Instance Methods

Instance methods are methods that are associated with an instance of a class. They are defined within the class and are called on an instance of the class. Here are some key points to remember about instance methods:

1. Instance methods can access and modify the instance variables of the object on which they are called.
2. Instance methods can call other instance methods on the same object.
3. Instance methods can use the `self` keyword to refer to the instance of the class on which the method is being called.
4. Instance methods are defined in the same way as other methods, but they must take at least one parameter, which is usually called `self`.
5. To call an instance method, you use the dot notation, specifying the name of the instance followed by the name of the method and any arguments in parentheses.

Here is an example of defining and using an instance method in Python:

```python
class MyClass:
    def __init__(self, x):
        self.x = x

    def print_x(self):
        print(self.x)

my_instance = MyClass(5)
my_instance.print_x() # prints 5
```

In this example, the `print_x` method is an instance method because it is called on an instance of the `MyClass` class (`my_instance`). The method accesses the `x` instance variable of the object on which it is called (`my_instance`) using the `self` keyword. The method is called using the dot notation (`my_instance.print_x()`).