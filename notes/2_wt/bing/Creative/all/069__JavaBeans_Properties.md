### JavaBeans Properties

- A JavaBean property is a named attribute that can be accessed by the user of the object   .
- The attribute can be of any Java data type, including the classes that you define  .
- A JavaBean property may be read, write, read-only, or write-only   .
- To define a property in a bean class, supply public getter and setter methods.
- For example, the following methods define an int property called mouthWidth:

```java
public class FaceBean {
  private int mMouthWidth = 90;

  public int getMouthWidth () {
    return mMouthWidth;
  }

  public void setMouthWidth (int mw) {
    mMouthWidth = mw;
  }
}
```

- A builder tool like NetBeans recognizes the method names and shows the mouthWidth property in its list of properties.
- It also recognizes the type, int, and provides an appropriate editor so the property can be manipulated at design time.
- Various specializations of basic properties are available and described in the following sections.

#### Indexed Properties

- An indexed property is an array instead of a single value.
- In this case, the bean class provides a method for getting and setting the entire array.
- Here is an example for an int [] property called testGrades:

```java
public int [] getTestGrades () {
  return mTestGrades;
}

public void setTestGrades (int [] tg) {
  mTestGrades = tg;
}
```

- For indexed properties, the bean class also provides methods for getting and setting a specific element of the array.

```java
public int getTestGrades (int index) {
  return mTestGrades [index];
}

public void setTestGrades (int index, int grade) {
  mTestGrades [index] = grade;
}
```

#### Bound Properties

- A bound property notifies listeners when its value changes.
- This has two implications:
  - The bean class includes addPropertyChangeListener () and removePropertyChangeListener () methods for managing the bean's listeners.
  - When a bound property is changed, the bean sends a PropertyChangeEvent to its registered listeners.
- PropertyChangeEvent and PropertyChangeListener live in the java.beans package.
- The java.beans package also includes a class, PropertyChangeSupport, that takes care of most of the work of bound properties.
- This handy class keeps track of property listeners and includes a convenience method that fires property change events to all registered listeners.

#### Mnemonics and Learning Tricks

- A possible mnemonic to remember the types of JavaBean properties is **RWRW** (Read, Write, Read-only, Write-only).
- A possible learning trick to remember the getter and setter methods for JavaBean properties is to use the prefix **get** or **set** followed by the capitalized name of the property.
- For example, for a property called color, the getter method would be getColor () and the setter method would be setColor ().
- A possible learning trick to remember the getter and setter methods for indexed properties is to use the same prefix and name as for basic properties, but add an int parameter for the index.
- For example, for a property called scores, the getter method for the entire array would be getScores (), the setter method for the entire array would be setScores (int []), the getter method for a specific element would be getScores (int index), and the setter method for a specific element would be setScores (int index, int value).

: Properties (The Java™ Tutorials > JavaBeans(TM) - Oracle
: JSP - JavaBeans - tutorialspoint.com
: Java Bean - javatpoint
: What are JavaBeans? – Definition, Properties ... - BTech Geeks
: Self-generated