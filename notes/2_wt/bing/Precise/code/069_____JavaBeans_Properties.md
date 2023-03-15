### JavaBeans Properties

JavaBeans properties are accessed through getter and setter methods. Here is an example of a simple Java class with a property called `name`:

```java
public class Person {
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

The `getName` method is the getter for the `name` property, and the `setName` method is the setter. These methods allow the `name` property to be read and modified. The `name` property itself is private, so it can only be accessed through these methods. This is a common pattern in JavaBeans.