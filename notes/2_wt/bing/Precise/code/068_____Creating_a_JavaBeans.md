### Creating a JavaBeans

A JavaBean is a reusable software component that follows certain design conventions. Here is an example of how to create a simple JavaBean:

```java
public class MyBean implements java.io.Serializable {
    private String property1;
    private int property2;

    public MyBean() {
    }

    public String getProperty1() {
        return property1;
    }

    public void setProperty1(String property1) {
        this.property1 = property1;
    }

    public int getProperty2() {
        return property2;
    }

    public void setProperty2(int property2) {
        this.property2 = property2;
    }
}
```
