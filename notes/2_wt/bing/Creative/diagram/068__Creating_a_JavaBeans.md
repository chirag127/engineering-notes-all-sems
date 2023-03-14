A JavaBean is a Java class that follows some conventions, such as implementing Serializable, having a public no-arg constructor, and having private properties with public getter and setter methods. A JavaBean can be used as a data source for various components, such as tables, lists, or forms. To create a JavaBean, you need to write a Java class that adheres to the JavaBean conventions. For example, you can create a JavaBean class named Person with two properties: firstName and lastName. The class would look something like this:

```java
public class Person implements java.io.Serializable {
  private String firstName;
  private String lastName;

  public Person() {
    // no-arg constructor
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }

  public String getFirstName() {
    return firstName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }

  public String getLastName() {
    return lastName;
  }
}
```

To use a JavaBean as a data source, you need to create another class that acts as a service bean. A service bean is a class that provides business methods that return data from the JavaBean class. For example, you can create a service bean class named PersonService that has a method named getPersons that returns a list of Person objects. The class would look something like this:

```java
import java.util.ArrayList;
import java.util.List;

public class PersonService {
  public List<Person> getPersons() {
    // create some sample data
    List<Person> persons = new ArrayList<Person>();
    persons.add(new Person("Alice", "Smith"));
    persons.add(new Person("Bob", "Jones"));
    persons.add(new Person("Charlie", "Brown"));
    return persons;
  }
}
```

To generate a data control from the service bean, you need to use a tool that can create a data control definition file from the service bean class. A data control definition file is an XML file that describes the data and operations exposed by the service bean. For example, you can use Oracle JDeveloper to generate a data control from the PersonService class. The data control definition file would look something like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<dataControl name="PersonService" type="java" package="com.example" class="PersonService">
  <method name="getPersons" returnType="java.util.List" returnClass="Person" returnCollectionClass="java.util.List">
    <returnStructure>
      <attribute name="firstName" type="java.lang.String"/>
      <attribute name="lastName" type="java.lang.String"/>
    </returnStructure>
  </method>
</dataControl>
```

The following diagram illustrates the basic architecture of a JavaBean data control:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Data Consumer  | <--> |  Data Control   | <--> |  Service Bean   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
                             |      |
                             |      |
                             v      v
+-----------------+      +-----------------+
|                 |      |                 |
|  Data Control   | <--> |  JavaBean Class |
|  Definition     |      |                 |
|                 |      |                 |
+-----------------+      +-----------------+
```

The data consumer is a component that uses the data control to access the data and operations provided by the service bean. The data control is an object that implements the data control interface and acts as a mediator between the data consumer and the service bean. The data control definition is an XML file that describes the data and operations exposed by the service bean. The service bean is a class that provides business methods that return data from the JavaBean class. The JavaBean class is a class that follows the JavaBean conventions and encapsulates the data properties.