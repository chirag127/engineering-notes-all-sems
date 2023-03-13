#### Coupling in Software Design

- Coupling is a measure of how much a module (a class, a method, a function, etc.) depends on other modules.
- Coupling can be classified into different types, such as content coupling, common coupling, control coupling, stamp coupling, data coupling, and message coupling.
- Content coupling occurs when a module directly accesses or modifies the content of another module. This is the highest degree of coupling and should be avoided.
- Common coupling occurs when two or more modules share the same global data. This can lead to unexpected side effects and make the modules difficult to test and maintain.
- Control coupling occurs when a module passes a control parameter to another module to influence its logic. This can reduce the modularity and reusability of the modules.
- Stamp coupling occurs when a module passes a composite data structure (such as a record, a structure, or an object) to another module, but the latter only uses a part of it. This can create unnecessary dependencies and increase the complexity of the modules.
- Data coupling occurs when a module passes simple data (such as primitive types or individual variables) to another module. This is the lowest degree of coupling and is desirable.
- Message coupling occurs when a module communicates with another module through message passing, such as using an interface, an abstract class, or a callback function. This can enhance the modularity and reusability of the modules.

- A mnemonic to remember the types of coupling is **C**ontent **C**oupling **C**auses **C**haos, **S**tamp **C**oupling **S**ucks, **D**ata **C**oupling **D**elights, **M**essage **C**oupling **M**akes **M**agic.
- A learning trick to understand the concept of coupling is to think of modules as people who work together on a project. The more they depend on each other, the more coupled they are. The less they depend on each other, the more independent they are. The goal is to make them as independent as possible, while still achieving the desired functionality.
- An example of high coupling and low coupling in software design is shown below:

```
// High coupling: content coupling
class A {
    int x;
    void foo() {
        // do something
    }
}

class B {
    void bar() {
        A a = new A();
        a.x = 10; // directly accesses the content of A
        a.foo(); // directly invokes the method of A
    }
}

// Low coupling: message coupling
interface C {
    void foo();
}

class D implements C {
    int x;
    void foo() {
        // do something
    }
}

class E {
    void bar(C c) {
        c.foo(); // communicates with C through message passing
    }
}
```