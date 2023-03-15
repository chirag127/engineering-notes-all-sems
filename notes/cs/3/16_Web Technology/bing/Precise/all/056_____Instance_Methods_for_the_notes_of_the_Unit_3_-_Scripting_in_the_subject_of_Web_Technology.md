### Instance Methods

- Instance methods are methods that are associated with an instance of a class.
- These methods are defined within the class and can be called on an instance of the class.
- Instance methods have access to the instance variables and other instance methods of the object on which they are called.
- The first parameter of an instance method is always the instance itself, which is referred to as `self` in Python and `this` in JavaScript.
- Instance methods can be used to modify the state of an object or to retrieve information about the object.
- To define an instance method in Python, simply define a function within the class and use the `self` parameter to refer to the instance.
- In JavaScript, instance methods are defined within the constructor function using the `this` keyword.

Example in Python:
```python
class MyClass:
    def __init__(self, x):
        self.x = x

    def my_method(self, y):
        self.x += y
        return self.x
```

Example in JavaScript:
```javascript
class MyClass {
    constructor(x) {
        this.x = x;
    }

    myMethod(y) {
        this.x += y;
        return this.x;
    }
}
```