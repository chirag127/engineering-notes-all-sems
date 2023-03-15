### Typecasting

- Typecasting is the process of converting one data type to another.
- Typecasting can be done implicitly or explicitly.
- Implicit typecasting is done automatically by the compiler when there is no loss of information or precision.
- Explicit typecasting is done by the programmer using a cast operator or a constructor when there is a possibility of loss of information or precision.
- The syntax of explicit typecasting is:

```cpp
(type) expression; // C-style cast
type(expression); // constructor-style cast
```

- For example, to convert an int to a double, we can write:

```cpp
int x = 10;
double y = (double) x; // C-style cast
double z = double(x); // constructor-style cast
```

- C++ also provides four named cast operators for different purposes:

```cpp
static_cast<type>(expression); // for ordinary type conversions
const_cast<type>(expression); // for removing const or volatile qualifiers
dynamic_cast<type>(expression); // for safe downcasting of polymorphic types
reinterpret_cast<type>(expression); // for low-level type conversions
```

- For example, to convert a pointer to a base class to a pointer to a derived class, we can write:

```cpp
class Base { /* ... */ };
class Derived : public Base { /* ... */ };

Base* b = new Derived();
Derived* d = static_cast<Derived*>(b); // static cast
Derived* e = dynamic_cast<Derived*>(b); // dynamic cast
```

- Static cast performs a compile-time check and does not guarantee the validity of the conversion.
- Dynamic cast performs a run-time check and returns a null pointer if the conversion is invalid.
- Typecasting should be used with caution as it can lead to unexpected results or errors if done incorrectly.