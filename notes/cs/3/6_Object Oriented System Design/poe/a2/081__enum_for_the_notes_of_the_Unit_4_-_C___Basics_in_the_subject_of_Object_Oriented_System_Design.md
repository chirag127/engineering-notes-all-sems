 Here are the notes on enum for Unit 4 - C++ Basics in Object Oriented System Design:

### enum

1. enum is a user-defined data type that consists of enumerators/constants.
2. enumerators are identifiers that are bound to integer values. By default, the first enumerator has a value 0, and each subsequent enumerator has an incremented value.
3. enum can be used to define constants that are related to a particular type and restrict the values to a specific range.
4. The enum declaration defines a new type name and introduces the enumerators.
5. syntax:
enum enum-name {
    enumerator-list
};

6. Example:
enum Color { Red, Green, Blue };

7. Accessing enumerators:
Color c = Red;     // assigns Red to c
c = Blue;          // assigns Blue to c

8. Implicit conversion to int: Since enumerators are bound to integer values, they can be implicitly converted to int. However, it is not recommended to rely on the implicit conversion.
9. Explicitly assigning integer values: We can assign specific integer values to enumerators as follows:
enum Color { Red=5, Green, Blue=10 };

10. Scope of enum: The scope of an enum is limited to the block in which it is declared. It is not possible to access enumerators of an enum outside its scope.