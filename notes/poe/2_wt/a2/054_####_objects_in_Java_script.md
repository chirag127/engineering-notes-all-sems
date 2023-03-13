 Here is the content in markdown format on #### objects in JavaScript:

#### Objects in JavaScript
Objects in JavaScript are a collection of properties/methods. They are more complex data types than primitive data types like strings, numbers, booleans, etc.

Some key points about objects in JavaScript:

- Objects are denoted using curly braces { }.
- They can contain properties (variables) and methods (functions) inside the curly braces.
- Properties and methods are separated using commas ,.
- Properties are denoted using a name and a value pair name:value.
- Methods are denoted using a name and a function definition name:function().
- Objects can be created using object literals or the Object constructor.
- Objects are mutable, their properties can be changed or deleted after they are created.
- Objects can be nested, i.e. an object can contain other objects.
- Objects are passed by reference in JavaScript.

Examples of objects:

- Let's create an object using object literal:
{
    name: 'John',
    age: 30,
    greet: function() {
        console.log('Hello!');
    }
}

- Let's create an object using Object constructor:
let person = new Object();
person.name = 'John';
person.age = 30;
person.greet = function() {
    console.log('Hello!');
}

Advantages of using objects:
- Code reuse - Objects allow you to reuse methods/properties.
- Organized code - Objects help structure related data and functions together.
- Fewer global variables - Objects allow you to avoid using too many global variables by containing related variables/functions within objects.

Disadvantages of using objects:
- Additional overhead - There is some additional overhead in using objects vs simple variables and functions.
- Complexity - Object oriented code can be more complex to read and understand compared to simpler procedural code.

Applications of objects:
Objects are used extensively in JavaScript to model real world things and abstract data structures. Some examples are:

- DOM objects to model web pages
- Array objects to model lists
- Date objects to model dates and times
- And many more...

Hope this helps you learn about objects in JavaScript! Let me know if you would like me to explain anything in more detail.