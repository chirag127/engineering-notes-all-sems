JavaBeans Properties are named attributes that can be accessed by the user of the object. The attribute can be of any Java data type, including the classes that you define. A JavaBean property may be read, write, read only, or write only. To define a property in a bean class, you need to provide public getter and setter methods. For example, the following methods define a String property called name:

public class PersonBean {
  private String name;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }
}

### JavaBeans Properties

The following diagram illustrates the basic architecture of a JavaBean property:

```
+-----------------+       +-----------------+
|                 |       |                 |
|    User Code    |       |   Bean Class    |
|                 |       |                 |
+-----------------+       +-----------------+
|                 |       |                 |
|  getProperty()  |<----->|  getXXX()       |
|                 |       |                 |
|  setProperty()  |<----->|  setXXX()       |
|                 |       |                 |
+-----------------+       +-----------------+
```

The user code can access the property by calling the getProperty() and setProperty() methods, which in turn invoke the getter and setter methods of the bean class. The XXX in the getXXX() and setXXX() methods is the name of the property, with the first letter capitalized. For example, the name property has getName() and setName() methods. The getProperty() and setProperty() methods are defined by the java.beans.PropertyDescriptor class, which is used to describe a property of a bean class. The PropertyDescriptor class also provides information about the property type, read/write access, and bound/constrained status.