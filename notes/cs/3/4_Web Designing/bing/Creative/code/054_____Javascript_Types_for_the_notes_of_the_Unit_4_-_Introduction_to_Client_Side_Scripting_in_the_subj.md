Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of Javascript Types for the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing.

### Javascript Types
- Javascript is a **dynamically typed** language, which means that the type of a variable is determined at runtime, not at compile time.
- Javascript has **seven** basic types: **string**, **number**, **boolean**, **null**, **undefined**, **symbol**, and **object**.
- A **string** is a sequence of characters enclosed in single or double quotes, such as `"Hello"` or `'World'`.
- A **number** is a numeric value that can be an integer or a floating-point, such as `42` or `3.14`. Javascript uses a **64-bit** floating-point format to represent all numbers, which means that some integers cannot be represented exactly.
- A **boolean** is a logical value that can be either `true` or `false`.
- A **null** is a special value that represents the absence of any value.
- An **undefined** is a special value that indicates that a variable has not been assigned a value.
- A **symbol** is a unique and immutable identifier that can be used as a property key or a constant.
- An **object** is a collection of properties that can be accessed by name or index, such as `{name: "Alice", age: 25}` or `[1, 2, 3]`.
- Javascript also has some **built-in objects** that provide additional functionality, such as **Math**, **Date**, **String**, **Array**, **Function**, **RegExp**, and **Error**.
- Javascript also supports **type conversion**, which means that a value of one type can be converted to another type, either implicitly or explicitly.
- Implicit type conversion, or **coercion**, happens when an operator or a function expects a value of a certain type, but receives a value of a different type. For example, `1 + "2"` will result in `"12"`, because the `+` operator will coerce the number `1` to a string.
- Explicit type conversion, or **casting**, happens when a programmer uses a function or a constructor to change the type of a value. For example, `Number("42")` will result in `42`, because the `Number` function will cast the string `"42"` to a number.
- Javascript also has a **typeof** operator that can be used to check the type of a value. For example, `typeof 42` will return `"number"`, and `typeof null` will return `"object"`. However, the `typeof` operator is not always reliable, as it can return misleading results for some values, such as arrays or functions.