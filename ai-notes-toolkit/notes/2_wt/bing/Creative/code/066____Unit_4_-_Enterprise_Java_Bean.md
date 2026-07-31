## Unit 4 - Enterprise Java Bean

Enterprise Java Bean (EJB) is a technology that allows you to develop scalable, robust and secure enterprise applications in Java. EJB provides middleware services such as security, transaction management, concurrency, dependency injection, etc. to all EJB components. EJB components are server-side components that encapsulate the business logic of an application. There are three types of EJB components:

- Session beans: These are stateful or stateless components that handle the requests from clients. They can also access other EJB components or resources such as databases, messaging systems, etc.
- Entity beans: These are persistent components that represent the data stored in a database. They can be accessed by multiple clients and support concurrency and transactions.
- Message-driven beans: These are components that receive and process asynchronous messages from a message queue or a topic. They can also access other EJB components or resources.

To create an EJB component, you need to write a Java class with one or more annotations from the EJB specification. These annotations indicate the type and properties of the EJB component, such as its name, interface, transaction attributes, etc. For example, the following code snippet shows a simple stateless session bean that implements a Calculator interface:

```java
import javax.ejb.Stateless;

@Stateless
public class CalculatorBean implements Calculator {

    @Override
    public int add(int a, int b) {
        return a + b;
    }

    @Override
    public int subtract(int a, int b) {
        return a - b;
    }
}
```

To use an EJB component, you need to deploy it on an EJB container, which is a part of a Java EE application server. The EJB container manages the lifecycle, security, transactions, concurrency, etc. of the EJB components. It also provides a naming service that allows you to look up and invoke the EJB components. For example, the following code snippet shows how to access the CalculatorBean from a client:

```java
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class CalculatorClient {

    public static void main(String[] args) {
        try {
            // Obtain the JNDI initial context
            InitialContext ctx = new InitialContext();

            // Look up the CalculatorBean using its JNDI name
            Calculator calculator = (Calculator) ctx.lookup("java:global/CalculatorBean");

            // Invoke the methods of the CalculatorBean
            System.out.println("2 + 3 = " + calculator.add(2, 3));
            System.out.println("2 - 3 = " + calculator.subtract(2, 3));
        } catch (NamingException e) {
            e.printStackTrace();
        }
    }
}
```

For more details and examples on EJB, you can refer to the following sources:

- [EJB Tutorial - javatpoint](https://www.javatpoint.com/ejb-tutorial)
- [Tutorial: Enterprise JavaBeans - Oracle](https://docs.oracle.com/cd/E13226_01/workshop/docs81/doc/en/wls/tutorial/ejbtutorialIntro.html)
- [What Is an Enterprise Bean? - The Java EE 6 Tutorial - Oracle](https://docs.oracle.com/javaee/6/tutorial/doc/gipmb.html)
- [A Detailed Guide to Enterprise Java Beans w/Code Examples - Stackify](https://stackify.com/enterprise-java-beans/)
- [EJB Tutorial - tutorialspoint](https://www.tutorialspoint.com/ejb/index.htm)