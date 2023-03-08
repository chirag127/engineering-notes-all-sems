 Here is the content in markdown format for the topic ### static data and function members for the notes of the Unit 6 - Objects and Classes in the subject of Object Oriented System Design:

### Static Data Members

- Static data members are shared by all instances of a class.
- They are allocated memory only once, at the start of the program.
- They are accessed using the scope resolution operator ::. For example, `ClassName::staticDataMember`.
- They are useful when we want to maintain a common value shared across all instances of a class. For example, a counter to maintain the number of objects created.

### Static Function Members

- Static function members can only access static data members. They cannot access non-static data members.
- They are bound to the class, not the object. So they can be called without instantiating the class using the scope resolution operator ::. For example, `ClassName::staticFunction()`.
- They are useful for functions that do not need an object context to work. For example, utility functions to validate inputs etc.

**Advantages:**

- Memory efficient as static data is allocated only once.
- Provides a way to maintain common data or functions for a class.

**Disadvantages:**

- Static members are shared, so concurrent access needs to be properly handled to avoid race conditions.
- The relationship between static members and instances is not very explicit, which can make the code harder to understand.

**Examples:**

- A counter to keep track of the number of objects created of a class.
- Cache data - to avoid repetitive calculations etc.
- Utility functions to validate inputs, handle common logic etc.

**Applications:**

- Singleton patterns make use of static members to restrict a class to only one instantiated object.
- Factory methods are often static to create objects without instantiating a class.
- Common utility functions.
- When we need to share common data across all instances of a class.