### JavaBeans Properties

- JavaBeans properties are attributes of a Java class that can be accessed by other classes or tools using a standard convention.
- A property can be of any Java data type, such as int, String, boolean, or an object of another class.
- A property can be read-only, write-only, or read-write, depending on the availability of getter and setter methods.
- A getter method is a public instance method that returns the value of a property. It follows the naming convention of `get<PropertyName>` or `is<PropertyName>` for boolean properties.
- A setter method is a public instance method that sets the value of a property. It follows the naming convention of `set<PropertyName>` and takes one parameter of the same type as the property.
- For example, a Java class that represents a person may have the following properties: name, age, and gender. The corresponding getter and setter methods are:

```java
public class Person {
  private String name;
  private int age;
  private boolean gender; // true for male, false for female
  
  // getter and setter for name
  public String getName() {
    return name;
  }
  
  public void setName(String name) {
    this.name = name;
  }
  
  // getter and setter for age
  public int getAge() {
    return age;
  }
  
  public void setAge(int age) {
    this.age = age;
  }
  
  // getter and setter for gender
  public boolean isGender() {
    return gender;
  }
  
  public void setGender(boolean gender) {
    this.gender = gender;
  }
}
```

- JavaBeans properties can be used by other classes or tools to manipulate or display the state of a Java object. For example, a graphical user interface (GUI) tool can use the properties to generate a form for editing the attributes of a person object.
- JavaBeans properties can also support events and listeners, which allow a Java object to notify other objects when its state changes. For example, a person object can fire a property change event when its name, age, or gender is modified, and other objects can register as listeners to receive the event and react accordingly.
- A mnemonic to remember the naming convention of getter and setter methods is: **get** the value, **set** the value, **is** the value (for boolean properties).