Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Designing. Here are some notes on the topic of Javascript Types for Unit 4 - Introduction to Client Side Scripting.

### Javascript Types

- Javascript is a **dynamically typed** language, which means that the type of a variable is determined at runtime, not at compile time.
- Javascript has **seven** basic types: **number**, **string**, **boolean**, **null**, **undefined**, **object**, and **symbol**.
- The **typeof** operator can be used to check the type of a variable or a value. For example, `typeof 42` returns `"number"`, and `typeof "Hello"` returns `"string"`.
- The **number** type represents both **integers** and **floating-point** numbers. There is no separate type for integers in Javascript. For example, `42` and `3.14` are both numbers.
- The **string** type represents a sequence of **characters** enclosed in **quotes**. Strings can be concatenated with the **+** operator, and their length can be accessed with the **.length** property. For example, `"Hello" + " World"` returns `"Hello World"`, and `"Hello".length` returns `5`.
- The **boolean** type represents a **logical** value that can be either **true** or **false**. Booleans can be used in **conditional** statements and **logical** operators. For example, `true && false` returns `false`, and `true || false` returns `true`.
- The **null** type represents a **special** value that indicates the **absence** of a value. For example, `var x = null;` declares a variable x and assigns it the value null.
- The **undefined** type represents a **special** value that indicates the **lack** of a value. For example, `var y;` declares a variable y but does not assign it any value, so its value is undefined.
- The **object** type represents a **collection** of **properties** and **methods**. Objects can be created with the **object literal** syntax, or with the **new** operator and a **constructor** function. For example, `var person = {name: "Alice", age: 25};` creates an object with two properties, name and age, and `var person = new Person("Alice", 25);` creates an object with the Person constructor function.
- The **symbol** type represents a **unique** and **immutable** identifier that can be used as a **key** for object properties. Symbols can be created with the **Symbol** function, and can have an optional **description**. For example, `var sym = Symbol("foo");` creates a symbol with the description "foo".