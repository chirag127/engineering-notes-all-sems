
### Call and Return by Reference

* Call by reference is a method of passing arguments to a function where the argument is a reference to the variable passed in. This means that the value of the variable is changed within the function and the changes are reflected in the original variable. 
* In C++, when a reference is passed to a function, the function works directly on the original variable. This means that the function can modify the argument and the changes will be reflected in the original variable. 
* When a reference is returned from a function, the function returns a reference to the original variable. This means that the return value of the function is a reference to the original variable, and any changes to the variable will be reflected in the return value. 
* References are often used to pass large objects or structures between functions, as they are more efficient than passing the entire object. 
* References can also be used to create aliases for existing variables, allowing a single variable to be referred to by multiple names.