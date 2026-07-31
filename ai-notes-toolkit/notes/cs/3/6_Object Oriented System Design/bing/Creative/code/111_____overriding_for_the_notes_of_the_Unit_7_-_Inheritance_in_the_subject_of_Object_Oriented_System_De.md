### Overriding

- Overriding is an object-oriented programming feature that enables a child class to provide different implementation for a method that is already defined and/or implemented in its parent class or one of its parent classes .
- The overridden method in the child class should have the same name, signature, and parameters as the one in its parent class .
- Overriding is useful when the child class wants to modify or extend the behavior of the parent class method according to its own specific needs.
- Overriding allows the child class to achieve polymorphism, which means the ability to take different forms depending on the context.
- Overriding is different from overloading, which is the ability to define multiple methods with the same name but different parameters in the same class.
- Overriding is also different from hiding, which is the ability to define a method with the same name and signature as a parent class method, but in a different scope (such as static or private).
- Overriding can be prevented by using the final keyword in the parent class method, which means the method cannot be overridden by any child class.
- Overriding can also be enforced by using the abstract keyword in the parent class method, which means the method must be overridden by any concrete child class.
- Overriding can be checked by using the @Override annotation in the child class method, which indicates that the method is intended to override a parent class method.
- Overriding can be invoked by using the super keyword in the child class method, which refers to the parent class object and allows the child class to call the parent class method.