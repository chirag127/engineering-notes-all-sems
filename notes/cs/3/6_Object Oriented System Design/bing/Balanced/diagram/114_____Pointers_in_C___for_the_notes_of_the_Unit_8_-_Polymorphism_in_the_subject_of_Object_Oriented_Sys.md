### Pointers in C++

- A pointer is a variable that holds the address of another variable.
- Pointers have a data type that indicates the type of the variable they point to.
- Pointers can be declared using the asterisk (*) symbol, for example: `int *p;`.
- Pointers can be assigned the address of a variable using the address-of (&) operator, for example: `p = &x;`.
- Pointers can be dereferenced using the asterisk (*) symbol, which means accessing the value of the variable they point to, for example: `cout << *p;`.
- Pointers can also point to arrays, strings, vectors, etc. by using the name of the array or the container as the address, for example: `int arr[5] = {1, 2, 3, 4, 5}; int *q = arr;`.
- Pointers can be used to pass variables by reference to functions, which means the function can modify the original value of the variable, for example: `void swap(int *a, int *b) { int temp = *a; *a = *b; *b = temp; }`.
- Pointers can also point to functions, which means they can store the address of a function and be used to call the function, for example: `int add(int x, int y) { return x + y; } int (*f)(int, int) = add; cout << f(2, 3);`.
- Pointers can be used to implement polymorphism in C++, which means the ability of an object to behave differently depending on its type.
- Polymorphism can be achieved by using virtual functions, which are functions that can be overridden by derived classes.
- Virtual functions are declared using the keyword `virtual` in the base class, and are redefined in the derived classes with the same signature.
- Pointers to the base class can point to objects of the derived classes, and can call the appropriate virtual function depending on the type of the object.
- For example: `class Shape { public: virtual void draw() { cout << "Drawing a shape\n"; } }; class Circle : public Shape { public: void draw() { cout << "Drawing a circle\n"; } }; class Square : public Shape { public: void draw() { cout << "Drawing a square\n"; } }; Shape *s1 = new Circle(); Shape *s2 = new Square(); s1->draw(); // calls Circle::draw() s2->draw(); // calls Square::draw()`.
- The `this` pointer is a special pointer that refers to the current object of the class.
- The `this` pointer is an implicit parameter to all member functions of the class.
- The `this` pointer can be used to access the data members and member functions of the current object, for example: `class Student { public: int roll; string name; void display() { cout << "Roll: " << this->roll << "\n"; cout << "Name: " << this->name << "\n"; } }; Student s; s.roll = 10; s.name = "Alice"; s.display(); // prints Roll: 10 Name: Alice`.
- The `this` pointer can also be used to return the current object from a function, for example: `class Vector { public: int x, y; Vector(int x, int y) { this->x = x; this->y = y; } Vector add(Vector v) { return Vector(this->x + v.x, this->y + v.y); } }; Vector v1(1, 2); Vector v2(3, 4); Vector v3 = v1.add(v2); // returns a new vector with x = 4 and y = 6`.