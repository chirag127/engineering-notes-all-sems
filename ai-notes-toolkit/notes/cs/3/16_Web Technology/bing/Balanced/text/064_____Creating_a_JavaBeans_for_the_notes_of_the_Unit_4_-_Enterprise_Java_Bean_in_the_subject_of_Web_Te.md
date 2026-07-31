### Creating a JavaBeans for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- A JavaBean is a reusable software component that can be manipulated visually in a builder tool.
- A JavaBean follows some design patterns and conventions to expose its properties, methods, and events.
- A JavaBean can be used in various contexts, such as web applications, desktop applications, or distributed applications.
- To create a JavaBean, you need to follow these steps  :
  - Define a public class with a public no-argument constructor.
  - Declare the properties of the bean as private fields and provide public getter and setter methods for them.
  - Implement the java.io.Serializable interface to enable the bean to be saved and restored.
  - Optionally, implement the java.beans.Customizer interface to provide a custom GUI for editing the bean's properties in a builder tool.
  - Optionally, define one or more event types and register listeners for them using the java.beans.PropertyChangeSupport and java.beans.VetoableChangeSupport classes.
  - Optionally, provide a BeanInfo class that describes the bean's properties, methods, events, and customizer.
  - Optionally, package the bean in a JAR file with a manifest file that specifies the bean's name, class, and icon.
- An example of a simple JavaBean that represents a person is:

```java
import java.io.Serializable;

public class PersonBean implements Serializable {
  // Declare the properties of the bean
  private String name;
  private int age;
  private boolean married;

  // Provide a public no-argument constructor
  public PersonBean() {
    // Initialize the properties with default values
    name = "";
    age = 0;
    married = false;
  }

  // Provide public getter and setter methods for the properties
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

  public boolean isMarried() {
    return married;
  }

  public void setMarried(boolean married) {
    this.married = married;
  }
}
```
- To use a JavaBean in a web application, you can either instantiate it programmatically in a servlet or JSP, or use a tag library that supports JavaBeans, such as the JSTL.
- An example of using the PersonBean in a JSP page is:

```jsp
<%@ page import="PersonBean" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
  <title>PersonBean Example</title>
</head>
<body>
  <h1>PersonBean Example</h1>
  <c:set var="person" value="<%= new PersonBean() %>" />
  <c:set target="${person}" property="name" value="Alice" />
  <c:set target="${person}" property="age" value="25" />
  <c:set target="${person}" property="married" value="true" />
  <p>Name: ${person.name}</p>
  <p>Age: ${person.age}</p>
  <p>Married: ${person.married}</p>
</body>
</html>
```
- To use a JavaBean in a distributed application, you can either use the Java Remote Method Invocation (RMI) or the Java Naming and Directory Interface (JNDI) to locate and access the bean on a remote server.
- An example of using the PersonBean in a RMI client is:

```java
import java.rmi.Naming;

public class PersonClient {
  public static void main(String[] args) {
    try {
      // Locate the remote bean using the RMI registry
      PersonBean person = (PersonBean) Naming.lookup("rmi://localhost:1099/PersonBean");
      // Invoke the methods of the bean
      person.setName("Bob");
      person.setAge(30);
      person.setMarried(false);
      System.out.println("Name: " + person.getName());
      System.out.println("Age: " + person.getAge());
      System.out.println("Married: " + person.isMarried());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```
- An Enterprise