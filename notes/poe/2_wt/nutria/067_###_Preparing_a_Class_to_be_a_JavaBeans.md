
### Preparing a Class to be a JavaBeans

- To prepare a class to be a JavaBean, it must meet certain criteria. 
- The class must be public, it must have a public no-argument constructor, and it must implement the `Serializable` interface.
- The class must also provide accessor (getter) and mutator (setter) methods for each of its properties. 
- These methods must follow the standard naming conventions, i.e. `getPropertyName()` and `setPropertyName()`. 
- The class must also have an `equals()` method, as well as a `hashCode()` method. 
- Finally, the class should provide a `toString()` method, which should return a meaningful representation of the object.
- Mnemonic: 
    - P: Public
    - N: No-Arg Constructor
    - S: Serializable
    - G: Getters
    - S: Setters
    - E: equals()
    - H: hashCode()
    - T: toString()