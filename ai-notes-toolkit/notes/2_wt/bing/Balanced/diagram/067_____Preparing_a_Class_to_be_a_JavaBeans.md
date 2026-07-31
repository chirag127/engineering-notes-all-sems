A JavaBean is a Java class that follows some conventions to be reusable as a component in a graphical user interface. To prepare a class to be a JavaBean, it should meet the following requirements  :

- It should implement the Serializable interface, which allows the bean to be saved and restored.
- It should have a public no-argument constructor, which allows the bean to be instantiated by a tool or a container.
- It should have private properties (member variables) with public getter and setter methods, which follow the naming convention of getPropertyName and setPropertyName. This allows the bean to expose its properties in a consistent way.
- It should optionally support events, which allow the bean to notify other components of changes in its state or properties.

To package a class as a JavaBean, it should be placed in a JAR file with a manifest file that specifies the bean's name, version, vendor, and other information. The JAR file may also contain other resources, such as icons, images, sounds, or localization files, that are used by the bean.

Here is an example of a JavaBean class that represents a person with a name and an age:

```java
import java.io.Serializable;

public class PersonBean implements Serializable {

  // Private properties
  private String name;
  private int age;

  // Public no-argument constructor
  public PersonBean() {
    // Initialize properties with default values
    name = "";
    age = 0;
  }

  // Public getter and setter methods
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }
}
```

Here is an example of a manifest file for the PersonBean class:

```text
Manifest-Version: 1.0
Name: PersonBean.class
Java-Bean: True
Bean-Name: Person
Bean-Vendor: Example
Bean-Version: 1.0
```

Here is an example of an ASCII diagram for the PersonBean class:

```
+-----------------+
|   PersonBean    |
+-----------------+
| -name: String   |
| -age: int       |
+-----------------+
| +PersonBean()   |
| +getName():String|
| +setName(String)|
| +getAge():int   |
| +setAge(int)    |
+-----------------+
```