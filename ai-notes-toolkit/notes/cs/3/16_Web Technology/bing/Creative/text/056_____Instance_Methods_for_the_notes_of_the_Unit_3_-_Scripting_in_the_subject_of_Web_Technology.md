### Instance Methods

- Instance methods are functions that are defined inside a class and can be called on the objects of that class.
- Instance methods have access to the instance attributes and the class attributes of the object.
- Instance methods can modify the state of the object by changing the values of its attributes or calling other methods on it.
- Instance methods can also return values or other objects as the result of their computation.
- Instance methods are defined by using the `def` keyword followed by the method name and a list of parameters. The first parameter is usually named `self` and represents the object on which the method is called.
- Instance methods are called by using the dot notation on the object, followed by the method name and the arguments. For example, `obj.method(arg1, arg2)`.
- Instance methods can also be called by using the `getattr` function on the object and the method name as a string. For example, `getattr(obj, "method")(arg1, arg2)`.
- Instance methods can be overridden by subclasses to provide different or additional functionality. The `super` function can be used to access the parent class's method. For example, `super().method(arg1, arg2)`.
- Instance methods can be decorated by using the `@` symbol and the name of the decorator function. Decorators can modify the behavior or the output of the method. For example, `@staticmethod` or `@classmethod`.
- Instance methods can be documented by using docstrings, which are triple-quoted strings that appear right after the method definition. Docstrings can explain the purpose, the parameters, the return value, and the exceptions of the method. For example, `"""This is a docstring."""`.