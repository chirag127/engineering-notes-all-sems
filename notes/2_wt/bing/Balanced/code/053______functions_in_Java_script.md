#### Functions in JavaScript

A function is a block of code that performs a specific task and can be reused throughout a program. A function can take zero or more parameters as input and return a single value as output. A function can be defined using a function declaration or a function expression.

A function declaration consists of the keyword `function`, followed by the name of the function, a list of parameters enclosed in parentheses, and the function body enclosed in curly braces. For example:

```javascript
// A function declaration that calculates the area of a circle
function areaOfCircle(radius) {
  return Math.PI * radius * radius;
}
```

A function expression consists of the keyword `function`, followed by an optional name, a list of parameters enclosed in parentheses, and the function body enclosed in curly braces. A function expression can be assigned to a variable or passed as an argument to another function. For example:

```javascript
// A function expression that calculates the factorial of a number
var factorial = function(n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

// A function expression that is passed as an argument to another function
function map(array, func) {
  var result = [];
  for (var i = 0; i < array.length; i++) {
    result.push(func(array[i]));
  }
  return result;
}

// Calling the map function with the factorial function as an argument
var numbers = [1, 2, 3, 4, 5];
var factorials = map(numbers, factorial);
console.log(factorials); // [1, 2, 6, 24, 120]
```

To call a function, use the function name followed by a list of arguments enclosed in parentheses. For example:

```javascript
// Calling the areaOfCircle function with 5 as an argument
var area = areaOfCircle(5);
console.log(area); // 78.53981633974483
```

A function can also return another function as its output. For example:

```javascript
// A function that returns a function that adds a given number to its argument
function adder(n) {
  return function(x) {
    return x + n;
  };
}

// Calling the adder function with 10 as an argument
var addTen = adder(10);

// Calling the addTen function with 5 as an argument
var result = addTen(5);
console.log(result); // 15
```