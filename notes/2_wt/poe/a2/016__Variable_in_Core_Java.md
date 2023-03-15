 Here is the formal content on the topic 'Variable in Core Java' in markdown format:

#### Variable in Core Java

1. A variable is a location/container which holds the value that can change.
2. In Java, there are three types of variables:
    - Local Variable: Declared inside the body of a method and usable only within that method.
    - Instance Variable: Declared inside a class but outside any method and are instantiated when an object of the class is created. They are shared by all instances (objects) of the class.
    - Static Variable: Also declared inside a class but with the static keyword. There is only one copy of a static variable shared by all instances of the class.
3. Variables must be declared before use. The declaration specifies the data type and name of the variable. For example: int count;
4. Values are assigned to variables using the assignment operator (=). For example: count = 5;
5. The valid names for variables are identifiers which must follow certain rules:
    - The first character must be a letter, underscore or dollar symbol.
    - Subsequent characters can be letters, digits or underscores.
    - Case sensitive: age and Age are different variables.
    - Cannot be a keyword (like int, float, etc.).
6. Data types in Java specify the size and type of values that can be stored in a variable. The most commonly used data types are:
    - int: For whole numbers
    - float: For fractional numbers
    - double: For fractional numbers with greater precision
    - char: For single character
    - boolean: For true/false values