### Static Data and Function Members

- Static data members are class members that belong to the class rather than to its objects.
- Static data members are declared with the `static` keyword inside the class definition, but they are defined outside the class.
- Static data members have only one copy that is shared by all the objects of the class.
- Static data members can be accessed by both static and non-static member functions, as well as by the class name with the scope resolution operator `::`.
- Static data members are initialized to zero by default, but they can also be explicitly initialized with a constant expression.
- Static function members are class members that can be used to access static data members or other static function members.
- Static function members are declared and defined with the `static` keyword inside the class definition.
- Static function members do not have an implicit `this` parameter, so they cannot access non-static data members or non-static function members.
- Static function members can be called by both static and non-static member functions, as well as by the class name with the scope resolution operator `::`.
- Static function members are useful for performing operations that do not depend on the state of any object of the class.

: https://www.guru99.com/static-function-in-cpp.html
: https://stackoverflow.com/questions/37767847/stdsort-function-with-custom-compare-function-results-error-reference-to-non
: https://www.udemy.com/course/illustrating-oop-with-c/